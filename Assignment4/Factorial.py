number = int(input("Please enter number : "))

factorial = 1
i = 1

while factorial < number :
    i += 1
    factorial *= i


if factorial == number :
    print("Yes")

else :
    print("No")


