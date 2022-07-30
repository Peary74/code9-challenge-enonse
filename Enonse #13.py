def ranvese(lis):
    reverse=lis[::-1] 
    print(reverse)
    reverse=reverse[:-1:]
    reverse=reverse[::-1] 
    reverse.append(lis[0])
    print(reverse)
    reverse=reverse[:-2:]
    reverse=reverse[::-1] 
    reverse.append(lis[-1])
    reverse.append(lis[0])
    print(reverse)
    reverse=reverse[:-3:]
    reverse=reverse[::-1] 
    reverse.append(lis[1])
    reverse.append(lis[-1])
    reverse.append(lis[0])
    print(reverse)
    
    return reverse
        
lis=[ 0, 1, 2, 3, 4 ]
reverseChenn= ranvese(lis)
for i,el in enumerate(reverseChenn):
    if(el==3):
        print(el," nan pozisyon:",i)

