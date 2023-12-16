import random


number_of_dice = random.randint(1,6)

if number_of_dice == 6 :

    print("Excellent 😍 You can try your luck again!")
    number_of_dice = random.randint(1,6)
    print(number_of_dice)

else :
       print(number_of_dice,"\n","Unfortunately you lost.")
    
