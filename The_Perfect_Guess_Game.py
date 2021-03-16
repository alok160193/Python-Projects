# *********************PROJECT-4 THE PERFECT GUESS************************
# To guess a no. from 1 to 100.

import random
randomNumber = random.randint(1, 100)
print(randomNumber)

userGuess = 0
guessNo = 0

while userGuess != randomNumber:
    userGuess = int(input("Enter your Guess from 1 to 100.\n"))
    guessNo += 1
    if(userGuess==randomNumber):
        print(f"You guessed it right in {guessNo} attempts !")
      
    elif userGuess > randomNumber:
        print("You gussed it wrong !")
        print("Lower No. Plz !")
        
    elif userGuess < randomNumber:
        print("You gussed it wrong !")
        print("Higher No. Plz !")
        
with open("hiscore.txt","r") as f:
    hiscore= int(f.read())
if guessNo<hiscore:
    print("You have just broken the previous record !!!")
    with open("hiscore.txt","w") as f:
        f.write(str(guessNo))
    


