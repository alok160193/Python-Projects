# ****************************************************************************
# PROJECT 1: SNAKE, WATER & GUN GAME !
#******************************************************************************

import random 
print("Comp turn:Snake(s),Water(w),Gun(g)?")
randno=random.randint(1,3)
if randno==1:
    comp="s"
elif randno==2:
    comp="w"
elif randno==3:
    comp="g"

you=input("Your Turn:Snake(s),Water(w),Gun(g)?: ")

print("Computer Turn is: ",comp)


def gamewin(comp,you):
    # If two values are equal, declare a tie !
    if comp==you:
        return ("Tie")
    # Check for all possibilities when comp choses s 
    elif comp=="s":
        if you=="g":
            return ("You Win !")
        elif you=="w":
            return ("You Lose!")
    # Check for all possibilities when comp choses w 
    elif comp=="w":
       if you=="s":
            return ("You Win !")
       elif you=="g":
            return ("You Lose!")  
    # Check for all possibilities when comp choses g 
    elif comp=="g":
        if you=="w":
            return ("You Win !")
        elif you=="s":
            return ("You Lose!")  

print(gamewin(comp,you))
