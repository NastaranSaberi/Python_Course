a = int(input("Please enter first side :"))
b = int(input("Please enter second side :"))
c = int(input("Please enter third side :"))

if a + b > c and a + c > b and c + b > a :
    print("It is a triangle.")

else:
    print("It is not a triangle.")