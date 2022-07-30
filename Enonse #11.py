lis=[1,6,9,3,2,6,8,3,4,0,7]
piGwo=lis[0]
piPiti=lis[0]
for i in lis:
    if i>piGwo:
        piGwo=i
    elif i<piPiti:
        piPiti=i
        
print(piGwo)
print(piPiti)