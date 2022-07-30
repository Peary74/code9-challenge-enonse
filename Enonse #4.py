

a=2
b=3
#enteval 1 jiska 20
enteval=20
kondisyon1=""
n1=0
kondisyon2=""
n2=0
kondisyon3=""
n3=0
kondisyon4=""
n4=0
for i in range(enteval):
    i+=1
    if i%a == 0 and i%b != 0:
        kondisyon1+=str(i)+","
        n1+=1
    elif i%a != 0 and i%b == 0:
        kondisyon2+=str(i)+","
        n2+=1
    elif i%a == 0 and i%b == 0:
        kondisyon3+=str(i)+","
        n3+=1
    else:
        kondisyon4+=str(i)+","
        n4+=1
        
kondisyon1=str(kondisyon1[0:-1]) 
kondisyon2=str(kondisyon2[0:-1])  
kondisyon3=str(kondisyon3[0:-1])  
kondisyon4=str(kondisyon4[0:-1])   
print(kondisyon1,"-> total nonb:",n1)
print(kondisyon2,"-> total nonb:",n2)
print(kondisyon3,"-> total nonb:",n3)
print(kondisyon4,"-> total nonb:",n4)