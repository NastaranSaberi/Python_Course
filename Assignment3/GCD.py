number1 = int(input("Please enter natural number (Number1): "))
number2 = int(input("Please enter natural number (Number2): "))

if number1 > number2 :
    gcd = number2

elif number2 > number1 :
    gcd = number1

elif number1 == number2 :
    gcd = number1

while gcd > 1 :

    if number1 % gcd == 0 and number2 % gcd == 0 :
        print("gcd: " , gcd)
        break

    else :
        gcd -= 1

        if number1 % gcd == 0 and number2 % gcd == 0 :
            print("gcd: " , gcd)
            break

