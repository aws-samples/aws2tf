# Reverted PRs requiring rework: #155 and #158

## Summary




Summary

Running aws2tf.py in full-account fast mode (-f) across several regions
surfaced a set of independent robustness bugs that either abort the run or
produce invalid Terraform. This PR fixes them, grouped by root cause. Each fix
was reproduced and verified in isolation, and none change behaviour for cases
that already worked — they only prevent aborts / invalid output on edge cases.

1. Fatal TypeError on id=None (type + "." + id)

Two paths concatenate type + "." + id while processing a type with id=None
(normal "get everything" mode):

common.call_resource — the -e exclusion branch, so -e <type> crashed
any full-account run.
get_aws_kms_key — the empty-response branch, hit in a region with no
customer KMS keys.
Both now guard if id is not None: (mirrors the existing noimport branch).

2. handle_error turning benign/transient errors into fatal aborts

Removed a dead pkey = frame.split("get_")[1] in the AccessDeniedException
branch. For resources fetched via the generic path the frame is
call_boto3/getresource (no get_), so [1] raised IndexError — turning
an expected AccessDenied into a hard crash.
Added a transient-connection branch (SSLError, ConnectionError,
ConnectionClosedError, ConnectTimeoutError, ReadTimeoutError) → log and
skip instead of aborting on a flaky endpoint.
Added an UnsupportedCommandException branch (a global-only service queried
in another region) → skip instead of abort.
3. Dangling references to deleted route-table targets

Route-table / route-table-association handlers rewrote gateway_id,
nat_gateway_id, transit_gateway_id, vpc_peering_connection_id,
network_interface_id into aws_* references unconditionally. When the target
was deleted (blackhole route), the reference pointed at a resource that was
never imported → terraform validate failed with "Reference to undeclared
resource".

Mirrors the existing subnet / security-group guard: build igw / natgw / vpcpeer
/ eni presence lists in build_lists (transit gateways already had one) and
only emit a reference when the target exists; otherwise keep the literal id,
which matches the imported blackhole route.

4. Invalid Terraform labels from incomplete sanitization

tfname() / write_import() sanitize an id into a Terraform label with a fixed
.replace() chain that misses characters such as (, ), %. A resource whose
name contains them produced an unparseable label, and since Terraform parses all
.tf files before generate-config-out, one bad label failed the whole plan.
Added a catch-all after the existing chain — map any remaining character outside
[A-Za-z0-9_-] to _ — in both functions so labels and references stay in
lockstep. Existing conventions (e.g. *→star) are preserved.

5. Getter passing a non-string id to write_import

A getter passing a dict as the import id crashed write_import
('dict' object has no attribute 'replace') and aborted the run, with no hint
of which resource type was at fault. write_import now checks the id is a
string and, if not, logs the resource type and skips it — surfacing the culprit
instead of killing the run.

6. Terminal hangs after a fatal error

The status heartbeat used a non-daemon, self-rescheduling threading.Timer, and
the crash path never stopped it, so an uncaught exception left the interpreter
blocked on a live non-daemon thread forever (only Ctrl-C freed the terminal).
Made the timer a daemon and added finally: stop_timer() around the entry point
so the process exits on every path.

Files changed

aws2tf.py, code/common.py, code/context.py, code/build_lists.py,
code/fixtf_aws_resources/fixtf_ec2.py, code/timed_interrupt.py,
code/get_aws_resources/aws_kms.py

Not included (tracked separately)

The generate-config-out completeness issue — structural, deserves its own change.
One getter that passes a dict id (now skipped+logged by #5); the getter fix is a small follow-up.
You can view, comment on, or merge this pull request online at:

  https://github.com/aws-samples/aws2tf/pull/162

Commit Summary

0f43be4 fix: keep literal id for route-table targets that no longer exist
c96e83b fix: exit cleanly on a fatal error instead of hanging the terminal
162f60a fix: harden resource dispatch and error handling against fatal edge cases
File Changes (7 files)
M aws2tf.py (8)
M code/build_lists.py (92)
M code/common.py (19)
M code/context.py (4)
M code/fixtf_aws_resources/fixtf_ec2.py (40)
M code/get_aws_resources/aws_kms.py (9)
M code/timed_interrupt.py (1)
Patch Links:

https://github.com/aws-samples/aws2tf/pull/162.patch
https://github.com/aws-samples/aws2tf/pull/162.diff



-----


diff --git a/code/common.py b/code/common.py
index 554766d9..2ac6b743 100755
--- a/code/common.py
+++ b/code/common.py
@@ -822,9 +822,9 @@ def get_file_permissions_info() -> dict:
 def call_resource(type, id):
    #log.debug("--1-- in call_resources >>>>> "+type+"   "+str(id))
    if type in context.all_extypes:
-      log.debug("Common Excluding: %s %s %s",  type, id) 
-      pkey=type+"."+id
-      context.rproc[pkey] = True
+      log.debug("Common Excluding: %s %s", type, id)
+      if id is not None:
+         context.rproc[type+"."+id] = True
       return
    
    if type in aws_no_import.noimport:
@@ -1946,6 +1946,7 @@ def tfname(theid):
    # resource name. Names containing '.', '@', spaces etc. would otherwise produce
    # references Terraform parses as attribute access (aws_iam_user.first.last.id).
    tfid=theid.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_").replace(" ","_").replace("*","star").replace("\\052","star").replace("@","_").replace("\\64","_")
+   tfid = re.sub(r'[^A-Za-z0-9_-]', '_', tfid)  # any remaining char invalid in a TF label -> _
    if tfid[:1].isdigit(): tfid="r-"+tfid
    tfid = re.sub(r'\.\.', '_', tfid)
    tfid = tfid.replace('/', '_')
@@ -1955,6 +1956,9 @@ def tfname(theid):
 #generally pass 3rd param as None - unless overriding
 def write_import(type,theid,tfid):
    try:
+      if not isinstance(theid, str):
+         log.error("write_import: non-string id for type=%s (%s=%r) - skipping this resource", type, theid.__class__.__name__, theid)
+         return
       ## todo -  if theid starts with a number or is an od (but what if its hexdecimal  ?)
 
       if tfid is None:
@@ -1962,6 +1966,8 @@ def write_import(type,theid,tfid):
       else:
             tfid=tfid.replace("/", "_").replace(".", "_").replace(":", "_").replace("|", "_").replace("$", "_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_").replace(" ","_").replace("*","star").replace("\\052","star").replace("@","_").replace("\\64","_")
 
+      tfid = re.sub(r'[^A-Za-z0-9_-]', '_', tfid)  # any remaining char invalid in a TF label -> _
+
          #catch tfid starts with number
       if tfid[:1].isdigit(): tfid="r-"+tfid
 
@@ -2471,6 +2477,12 @@ def handle_error(e,frame,clfn,descfn,topkey,id):
    if exn == "EndpointConnectionError":
       log.debug("No endpoint in this region for "+descfn+" - returning")
       return
+   elif exn in ("SSLError", "ConnectionError", "ConnectionClosedError", "ConnectTimeoutError", "ReadTimeoutError"):
+      log.warning("Transient connection error ("+exn+") for "+descfn+" clfn="+clfn+" - skipping this resource type")
+      return
+   elif exn == "UnsupportedCommandException":
+      log.warning(descfn+" not supported in this region for "+clfn+" - returning")
+      return
    elif exn=="ClientError":
       if "does not exist" in str(e):
          log.warning(id+" does not exist " + fname + " " + str(exc_tb.tb_lineno) )
@@ -2488,7 +2500,6 @@ def handle_error(e,frame,clfn,descfn,topkey,id):
       return  
    
    elif exn=="AccessDeniedException":
-      pkey=frame.split("get_")[1]
       log.warning("AccessDeniedException exception for "+fname+" - returning")
       return
 


----

diff --git a/code/fixtf_aws_resources/fixtf_ec2.py b/code/fixtf_aws_resources/fixtf_ec2.py
index 52582fcd..e1561728 100644
--- a/code/fixtf_aws_resources/fixtf_ec2.py
+++ b/code/fixtf_aws_resources/fixtf_ec2.py
@@ -298,20 +298,35 @@ def aws_route_table(t1, tt1, tt2, flag1, flag2):
 	if "cidr_block" in tt1:
 		if tt2 == "": t1 = tt1 + " = null\n"
 	elif "nat_gateway_id" in tt1 and tt2.startswith("nat-"):
-		t1 = tt1 + " = aws_nat_gateway." + tt2 + ".id\n"
-		common.add_dependancy("aws_nat_gateway", tt2)
+		if context.natgwlist.get(tt2):
+			t1 = tt1 + " = aws_nat_gateway." + tt2 + ".id\n"
+			common.add_dependancy("aws_nat_gateway", tt2)
+		else:
+			log.warning("WARNING: nat gateway not in natgw list " + tt2 + " Resource may be referencing a nat gateway that no longer exists")
 	elif tt1 == "gateway_id" and tt2.startswith("igw-"):
-		t1 = tt1 + " = aws_internet_gateway." + tt2 + ".id\n"
-		common.add_dependancy("aws_internet_gateway", tt2)
+		if context.igwlist.get(tt2):
+			t1 = tt1 + " = aws_internet_gateway." + tt2 + ".id\n"
+			common.add_dependancy("aws_internet_gateway", tt2)
+		else:
+			log.warning("WARNING: internet gateway not in igw list " + tt2 + " Resource may be referencing an internet gateway that no longer exists")
 	elif tt1 == "vpc_peering_connection_id" and tt2.startswith("pcx-"):
-		t1 = tt1 + " = aws_vpc_peering_connection." + tt2 + ".id\n"
-		common.add_dependancy("aws_vpc_peering_connection", tt2)
+		if context.vpcpeerlist.get(tt2):
+			t1 = tt1 + " = aws_vpc_peering_connection." + tt2 + ".id\n"
+			common.add_dependancy("aws_vpc_peering_connection", tt2)
+		else:
+			log.warning("WARNING: vpc peering connection not in vpcpeer list " + tt2 + " Resource may be referencing a vpc peering connection that no longer exists")
 	elif tt1 == "transit_gateway_id" and tt2.startswith("tgw-"):
-		t1 = tt1 + " = aws_ec2_transit_gateway." + tt2 + ".id\n"
-		common.add_dependancy("aws_ec2_transit_gateway", tt2)
+		if context.tgwlist.get(tt2):
+			t1 = tt1 + " = aws_ec2_transit_gateway." + tt2 + ".id\n"
+			common.add_dependancy("aws_ec2_transit_gateway", tt2)
+		else:
+			log.warning("WARNING: transit gateway not in tgw list " + tt2 + " Resource may be referencing a transit gateway that no longer exists")
 	elif tt1 == "network_interface_id" and tt2.startswith("eni-"):
-		t1 = tt1 + " = aws_network_interface." + tt2 + ".id\n"
-		common.add_dependancy("aws_network_interface", tt2)
+		if context.enilist.get(tt2):
+			t1 = tt1 + " = aws_network_interface." + tt2 + ".id\n"
+			common.add_dependancy("aws_network_interface", tt2)
+		else:
+			log.warning("WARNING: network interface not in eni list " + tt2 + " Resource may be referencing a network interface that no longer exists")
 	return skip, t1, flag1, flag2
 
 
@@ -327,7 +342,10 @@ def aws_route_table_association(t1, tt1, tt2, flag1, flag2):
 		common.add_dependancy("aws_route_table", tt2)
 	elif tt1 == "gateway_id":
 		if tt2.startswith("igw-"):
-			t1 = tt1 + " = aws_internet_gateway." + tt2 + ".id\n"
+			if context.igwlist.get(tt2):
+				t1 = tt1 + " = aws_internet_gateway." + tt2 + ".id\n"
+			else:
+				log.warning("WARNING: internet gateway not in igw list " + tt2 + " Resource may be referencing an internet gateway that no longer exists")
 		if tt2 == "null":
 			skip = 1
 	return skip, t1, flag1, flag2

----



----
