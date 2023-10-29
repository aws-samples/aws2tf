#!/usr/bin/python3
import fixtf2
import globals

def fixtf(ttft,tf):

  
    rf=tf+".out"
    tf2=tf+".tf"
    if globals.debug:
        print(ttft+" fixtf "+tf+".out") 
   
    try:
        f1 = open(rf, 'r')
    except:
        print("no "+rf)
        return
    Lines = f1.readlines()
    #print("getfn for fixtf2."+ttft+" "+tf2)
    with open(tf2, "a") as f2:
        skip=0
        flag1=False
        flag2=False
        f2.write("##START,"+ttft+"\n")
        for t1 in Lines:
            tt1=t1.split("=")[0].strip()
            try:
                tt2=t1.split("=")[1].strip()
            except:
                tt2=""

             
            try:              
                getfn = getattr(fixtf2, ttft)
            except Exception as e:
                print("The error is: ",e)
                print("** no fixtf2 for "+ttft+" calling generic fixtf2.aws_resource")
                print("t1="+t1) 
                getfn = getattr(fixtf2, "aws_resource")
          
            try:
                #print("calling fixtf2."+ttft+" "+tf2)
                skip,t1,flag1,flag2=getfn(t1,tt1,tt2,flag1,flag2)
            except Exception as e:
                print("The error is: ",e)
                print("--no fixtf2 for "+ttft+" calling generic fixtf2.aws_resource")
                print("t1="+t1) 
                skip,t1,flag1,flag2=fixtf2.aws_resource(t1,tt1,tt2,flag1,flag2)



            if skip == 0:
                f2.write(t1)
                
    #with open(tf2, "a") as f2:
    #    f2.write("##END,"+ttft+"\n")
    #splitf(tf2)


def splitf(file):
    lhs=0
    rhs=0
    print("split file:"+ file)
    with open(file, "r") as f:
        Lines = f.readlines()
    for tt1 in Lines:
        #print(tt1)
        if "{" in tt1: lhs=lhs+1
        if "}" in tt1: rhs=rhs+1
        if lhs > 1:
            if lhs == rhs:
                try:
                    f2.write(tt1+"\n")
                    f2.close()
                    lhs=0
                    rhs=0
                    continue
                except:
                    pass

        if tt1.startswith("resource"):
            #print("resource: " + tt1)
            ttft=tt1.split('"')[1]
            taddr=tt1.split('"')[3]
    
            f2=open(ttft+"__"+taddr+".tf","w")
            f2.write(tt1)

        elif tt1.startswith("#"):
            continue
        elif tt1=="" or tt1=="\n":
            continue
        else:
            try:
                f2.write(tt1)
            except:
                print("tried to write to closed file: >"+ tt1 + "<")
        
    #com="rm -f "+file
    #rout=common.rc(com)  
   


    










