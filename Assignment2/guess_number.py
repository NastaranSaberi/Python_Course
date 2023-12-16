import random

computer_number = random.randint(10,40)
user_guess = 0;
chances = 10

print(" ---------- welcome to the game ---------- ")
print("You only have ten chances (10❤️)")

for i in range(10):

    user_number = int(input("Please enter your guess:"))
    user_guess += 1
    chances -= 1

    if computer_number == user_number:
        print("You win 😍")
        print("Number of your guesses:",user_guess)
        break
    

    elif computer_number > user_number :
        print("goooo up")
        print("chances: ",chances,"❤️")

    elif computer_number < user_number :
        print("gooo down")
        print("chances: ",chances,"❤️")

    if chances == 0 :
        print("Game over")
