def getstack(stack_name,nested):
    #stackr=$($AWS cloudformation describe-stack-resources --stack-name $1 --query StackResources)
    #nested+=$(printf "\"%s\" " $as)
    
    
    return nested


def getstackresources():
  
    return

def get_stacks(stack_name):
  nested=[]
  print("level 1 nesting")
  nested=getstack(stack_name,nested)

  print("level 2 nesting")
  for nest in nested:
    print(nest)
    getstack(nest,nested)

  nested=nested+stack_name 

  print("Stacks Found:")
  for nest in nested:
    print(nest)

  for nest in nested:
    getstackresources(nest)

