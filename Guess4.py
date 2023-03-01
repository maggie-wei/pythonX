# GuessANumber4.py v1.0
import random

generatedNumber = random.randrange(1, 10)
userGuess = int(input('Guess a number in the range 1-10:'))
if userGuess == generatedNumber:
    print("You are correct")
elif userGuess < generatedNumber:
    print("Your guess is too LOW")
    
else:
    print("Your guess is too HIGH")
