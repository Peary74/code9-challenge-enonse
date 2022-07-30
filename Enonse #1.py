def adresIP(adres):
    add=0;
    for i in adres:
        if i != ".":
            add+=int(i)
        
    pot=int(add)*int(adres[0])
    
    return str(pot)
    
adres=input("Atre adres IP a:")

potOuve=adresIP(adres)

print("pot ki ouve a se pot #",potOuve)