numbers = int(input("number of sentences in your Fibonacci :"))

n1 = 1
n2 = 1
count = 0

if numbers == 1 :
    print(n1)

elif numbers <= 0:
    print("Please enter the correct number!")

else :
    while numbers > count:
        print(n1)
        n3 = n1 + n2
        n1 = n2 
        n2 = n3
        count += 1
        