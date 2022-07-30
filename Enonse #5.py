
def kalkilDigit(chenn):
    total=0
    totalX=[]
    for i in chenn:
        if i != " ":
            total+=int(i)
        else:
            totalX.append(total)
            total=0
        print(total)  
    print(totalX) 
    return totalX
        
pwodui=1
chenn=input("Antre chenn karakte a:")
chenn=chenn+" "

lis=kalkilDigit(chenn)
for i in lis:
    pwodui*=int(i)

print("ki bay total:",pwodui)