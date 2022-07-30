mo="mon Nom Complet hidden Shakespeare JEAN BAPTISTE endpass Test 1 2"

mo2=mo.split(" ")
for i,karak in enumerate (mo2):
    if karak == "hidden":
        mo2=mo2[i+1:]

for i,karak in enumerate (mo2):
    if karak == "endpass":
        mo2=mo2[:i]
        print(mo2) 

str = ' '.join(mo2)
print(str)