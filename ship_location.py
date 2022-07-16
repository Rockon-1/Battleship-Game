import random
li=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  

def place():
    result=[]
    alpha="abcdefg"
    gridlength=7
    gridsize=49
    ch=random.randint(0,1)
    incr=1
    if ch==0:
        incr=7
    size=3
    success=False
    coord=[]
    temp=0
    
    while (success==False):
        loc=random.randint(0,46)
        success=True
        
        while(success==True and temp<size):
            if(li[loc]==0):
               
                if(temp>0 and (loc%gridlength==0)):
                    success=False
                    coord.clear()
                    temp=0
                    break
                else:
                    coord.append(loc)
                    loc+=incr
                    temp+=1
                    if(loc>=gridsize):
                        pass
                        success=False
                        coord.clear()
                        temp=0
                        break 
                    
            else:
                success=False
                coord.clear()
                temp=0
    row=0;column=0
    #UNCOMMENT NEXT LINE IF U WANT TO SHOW LOCATION AS A NUMBER
    #print(coord)
    for x in coord:
        pass
        li[x]=1
        row=int(x/gridlength)
        column=x%gridlength
        temppp=alpha[row]
        res=temppp+str(column)
        result.append(res)
    #UNCOMMENT NEXT LINE IF U WANT TO SHOW EXACT LOCATION 
    #print(result)
    return result
#place()

