
vwayel="aeiouyè"
def asteriks(chenn):
    bonChenn=""
    for i,el in enumerate(chenn):
        if el not in vwayel and chenn[i+1] in vwayel:
            bonChenn+="*"
        else:
            bonChenn+=el
    return bonChenn

chenn=input("Antre chenn nan:")
bonMo= asteriks(chenn)   
print(bonMo)
            