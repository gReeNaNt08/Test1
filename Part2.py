from time import sleep
RED="red"
BLUE="blue"
YELLOW="yellow"

colors=[RED,BLUE,YELLOW]

color1=input("Enter the first primary color in lower case letters: ")
color2=input("Enter the first primary color in lower case letters: ")

if not(color1.islower() and color2.islower()):
    print("Enter data in valid form\n")
    sleep(2)
    quit()


if not (color1 in colors):
    print("Error:Invalid Color1")
    sleep(2)
    quit()
if not (color2 in colors):
    print("Error:Invalid Color2") 
    sleep(2) 
    quit()
if color1==color2:
    print("Error:The two colors you entered are same")
    sleep(2)  
    quit()

if color1==RED:
    if color2==BLUE:
        print("purple")   
    elif color2==YELLOW:
        print("orange")   
    else:
        print("Error")   
elif color1==BLUE:
    if color2==RED:
        print("purple")   
    elif color2==YELLOW:
        print("green")   
    else:
        print("Error")
elif color1==YELLOW:
    if color2==RED:
        print("orange")   
    elif color2==BLUE:
        print("green")   
    else:
        print("Error") 
else:
    print("-----")                            



    
    


