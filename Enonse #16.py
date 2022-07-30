
karakte="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
kod=input("Antre kod lan:")
rezilta=""
output=""
bonKod=kod.split(" ")
# print(bonKod)
for i,el in enumerate (bonKod):
    kodd= ' '.join(el)
    kodd=kodd.replace(" ","")
    if kodd[0] == ">":
        if(len(kodd)==3):
            chif=int(kodd[1])
        elif (len(kodd)==4):
            chif=int(kodd[1:3])
        let=kodd[-1]
        endeks=karakte.index(let)
        rezilta=karakte[endeks+chif]
    
    elif kodd[0] == "<":
        if(len(kodd)==3):
            chif=int(kodd[1])
        elif (len(kodd)==4):
            chif=int(kodd[1:3])
        let=kodd[-1]
        endeks=karakte.index(let)
        rezilta=karakte[endeks-chif]
        
    output+=rezilta 
        
print(output)