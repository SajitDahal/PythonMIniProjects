import random

user_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]

while True:
    print("Welcome to Rock Paper and Scissors game!!")
    user_choice = input("Please type in your choice (Rock/Paper/Scissors) or Q to quit:  ").lower()

    if user_choice == "q":
        break

    if user_choice not in options:
        continue

    random_number = random.randint(0, 2)

    computer_choice = options[random_number]
    print("Computer picked", computer_choice)


    if user_choice == computer_choice :
        print("It's a draw pick again..")
        continue

    elif user_choice == "rock" and computer_choice == "scissors":
        print("You won!!")
        user_score += 1

    elif user_choice == "paper" and computer_choice == "rock":
        print("You won!!")
        user_score += 1
    
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You won!!")
        user_score += 1

    else:
        print("Computer Won!!")
        
print("You scored:", user_score)
print("Computer scored:", computer_score)
print("Goodbyee! Have a nice day")

