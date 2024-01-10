number1 = int(input("Please enter natural number (Number1): "))
number2 = int(input("Please enter natural number (Number2): "))

if number1 == number2:
        lcm = number1

if number1 > number2:
        lcm = number1

elif number2 > number1 :
        lcm = number2
        
while lcm > 1 :

        if  lcm % number1 == 0 and lcm % number2 == 0 :
            print("LCM: " , lcm)
            break
        
        else:

            lcm +=1
            
            if  lcm % number1 == 0 and lcm % number2 == 0 :
                print("LCM: " , lcm)
                break