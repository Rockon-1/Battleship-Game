import ship_location
seA=['a','b','c','d','e','f','g']
seN=['0','1','2','3','4','5','6']
class dotcom:
    def setloc(s):
        s.l=ship_location.place();
    def setname(s,n):
         s.name=n
    
    def check(s,i):
        s.result="miss"
        for x in s.l:
              if(x==i):
                  s.l.remove(x)
                  s.result="hit"
                  if(len(s.l)==0):
                      s.result="kill"
                      #print("oouch ! you sunk "+s.name)
                  return s.result
        return s.result

global d1;d1=dotcom();global d2;d2=dotcom();global d3;d3=dotcom()
d1.setloc();d1.setname("Pets.com")
d2.setloc();d2.setname("AskMe.com")
d3.setloc() ;d3.setname("Go2.com")
global dlll;dlll=[d1,d2,d3]
sz=len(dlll)

def ch(inp):
    lc=int(inp[0])
    ch=seA[lc]
    inp=ch+inp[1]
    for x in dlll:
        result=x.check(inp)
        if result=="kill":
            dlll.remove(x)
        if result!="miss":
            break
    sz=len(dlll)
    if sz==0:
        result="killsall"
    return result

def again():
    d1.setloc()
    d2.setloc()
    d3.setloc()
    global dlll;
    dlll=[d1,d2,d3]
    sz=len(dlll)
