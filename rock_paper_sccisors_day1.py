#day 1
import pyfiglet, random
from time import sleep
running = True
print(pyfiglet.figlet_format('Rock Paper Sccisors- day1'))
options = [
    "rock",
    "paper",
    "scissors"
]
while running == True:
    player = input("Choose Rock Paper Sccisors type exit to exit: ")
    computer = random.choice(options)
    if player not in(options):
        print("indvalid choice")
    if player == computer:
        print("It's a tie!")
        print("computer choosed "+ computer)
    elif player == "rock" and computer == "scissors":
        print("You win!")
        print("computer choosed "+ computer)
    elif player == "paper" and computer == "rock":
        print("You win!")
        print("computer choosed "+ computer)
    elif player == "scissors" and computer == "paper":
        print("You win!")
        print("computer choosed "+ computer)
    else:
        print("You lose!")
        print("computer choosed "+ computer)
    if player == "exit":
        running = False
        break
