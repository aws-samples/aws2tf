common.py



with open(tf2, "a") as f2:
line 387
chnage to:
with open(tf2, "w") as f2:



aws2tf.py
too broad a delete:
line 204:
com = "rm -f aws_*.tf *.out"   # problem for aws2tf.sh files - just the *.out ?



pyprocessed - only logs


for iam_role - never set true
globals.rproc[pkey]=True

../aws2tf.py -t aws_lambda_function -i dialycleanup
aws_iam_role.arn:aws:iam::566972129213:role/service-role/dialycleanup-role-bv6r9pdi


