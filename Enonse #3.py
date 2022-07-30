from posixpath import split


def fomaTit(non):
    lisNon=[]
    for karakte in non:
        lisNon.append(karakte.capitalize())
    return lisNon

bonNon=""
lisNon=[]
non=input("Antre non w:")
lisNon=non.split(" ")
lisBonNon=fomaTit(lisNon)
for karakte in lisBonNon:
    bonNon+=karakte+" "
    
print(bonNon)