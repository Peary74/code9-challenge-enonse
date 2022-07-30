
def ranvese(chenn):
    reverse=chenn[::-1] 
    bonChenn=""
    for i in reverse:
        if i != " ":
            bonChenn+=i    
    return bonChenn
        
chenn=input("Antre chenn nan:")
reverseChenn= ranvese(chenn)

print(reverseChenn)