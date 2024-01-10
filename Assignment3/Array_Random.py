import random

n = int(input("Please enter length of array: "))

for i in range(n) :
    numbers = random.sample(range(0,n*n),n)

print("array :" , numbers)



