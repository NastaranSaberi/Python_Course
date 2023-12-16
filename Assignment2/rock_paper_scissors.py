import random

user_score = 0
computer_score = 0

print(" ---------- welcome to the game ---------- ")
  
  
x = random.randint(1,3)

if x == 1:
    computer_choice = "rock"
elif x == 2:
    computer_choice = "paper"
elif x == 3:
    computer_choice = "scissors"  


while computer_score < 5 and user_score < 5 :
  
    user_choice = input("rock or paper or scissors :")

    if computer_choice == "rock" and user_choice == "paper" :
        user_score += 1
        print("computer choice :",computer_choice)
        print("user_score:",user_score ,"|","computer_choice:",computer_score)

    elif computer_choice == "rock" and user_choice == "scissors" :
        computer_score += 1
        print("computer choice :",computer_choice)
        print("user_score:",user_score ,"|","computer_choice:",computer_score)

    elif computer_choice == user_choice :
        print("computer choice :",computer_choice)
        print("equal")
        print("user_score:",user_score ,"|","computer_choice:",computer_score)

    elif computer_choice == "paper" and user_choice == "rock" :
        computer_score += 1
        print("computer choice :",computer_choice)
        print("user_score:",user_score ,"|","computer_choice:",computer_score)

    elif computer_choice == "paper" and user_choice == "scissors" :
        user_score += 1
        print("computer choice :",computer_choice)
        print("user_score:",user_score ,"|","computer_choice:",computer_score)


    elif computer_choice == "scissors" and user_choice == "rock" :
        user_score += 1
        print("computer choice :",computer_choice)
        print("user_score:",user_score ,"|","computer_choice:",computer_score)

    elif computer_choice == "scissors" and user_choice == "paper" :
        computer_score += 1
        print("computer choice :",computer_choice)
        print("user_score:",user_score ,"|","computer_choice:",computer_score)


if computer_score < user_score :
    print("winner is : user")

elif computer_score > user_score :
    print("winner is : computer")

    