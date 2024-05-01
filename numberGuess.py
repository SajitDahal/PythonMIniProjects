import random

range = input("Enter the range of the number: ")
if range.isdigit():
    range = int(range)
    if range < 0 :
        print("Please type number greater than 0 ")
        quit()
    
         

else:
    print("Please type a number!!")
    quit()
        

random_num = random.randint(0, range)
guesses = 0
while True:
    guesses += 1
    guessed_num = input("Please type your guess: ")

    if guessed_num.isdigit():
     guessed_num = int(guessed_num)
    else:
        print("Please type a number!!")

    if guessed_num ==  random_num :
            print("You got it!")
            break
    elif guessed_num > random_num:
        print("Your guess is higher than the number!!")
    
    else:
        print("Your guess is lower than the number!!")


    continue

print("Congratulations!! you got it right in" , guesses , "guesses")