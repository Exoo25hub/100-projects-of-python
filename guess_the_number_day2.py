import time
import random
from pyfiglet import figlet_format

print(figlet_format("Guess The Number"))

while True:
    computer = random.randint(1, 100)  # Generate a random number each round
    
    while True:
        user_input = input("I have chosen a number from 1 to 100. Guess it: ")
        
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue
        
        user_guess = int(user_input)
        
        if user_guess == computer:
            print(f"Right! I guessed {computer}. You got it!")
            
        else:
            print(f"Wrong! Try again. i guessed {computer}")
    
    cont = input("Do you want to continue? (yes/no): ").strip().lower()
    if cont != "yes":
        print("Thanks for playing!")
        time.sleep(3)
        break
