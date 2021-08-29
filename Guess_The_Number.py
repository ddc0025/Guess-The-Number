print("*************************************")
print("*         WLCOM TO D's GAME         *")
print("*************************************")
print("*         GUESS THE NUMBER          *")
print("*************************************")
import random
Number = random.randint(1, 100)

Guess = None
guesses = 0
while(Guess != Number):
    Guess = int(input("Enter your guess : "))
    guesses += 1
    if(Guess==Number):
        print("Congratulation,You guessed it right!")
    else:
        if(Guess>Number):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")  
    
print(f"You guessed the number in {guesses} guesses")        
