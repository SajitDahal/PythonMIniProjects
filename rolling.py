# This is the game using basics of python where user can roll the dice and the number 
# they get in the dice adds up their score but iff they roll number 1 then they loose all the scores as a gamble 
# but if they sacrifice their turn after certain rolls they can save their score and the player with score 50 or more wins the game


import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll


while True:
    players = input("Enter the numbers of player(2 -4 ): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <=4:
            break
        else:
            print("Players must be between 2 to 4 !!")
    
    else:
        print("Invalid, Please try again!")

max_score = 50
players_score = [0 for _ in range(players)]


while max(players_score) < max_score:
    for i in range(players):
        print("\n PLayer number", i+1, "turn has just started! \n")
        print("Your total score is : " , players_score[i])
        current_score = 0 

        while True:
             should_roll = input("Would you like to roll (y): ")
             if should_roll.lower() != "y":
                 break
             
             value = roll()
             if value == 1 :
                  print("You rolled 1, Your turn ended!!")
                  current_score = 0
                  break
             else:
                current_score += value
                print("You rolled: ", value)
                    
        print("Your Score is: ", current_score )
            
    players_score[i] += current_score
    print("Your total score is : ", players_score[i])
                           
                 
max_score = max(players_score)
wining_index = players_score.index(max_score)

print("Player",wining_index+1 ,"is the winner with the score of: " , max_score)
