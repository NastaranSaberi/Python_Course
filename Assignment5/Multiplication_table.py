m = int(input("Enter number of row elements :"))
n = int(input("Enter number of column elements :"))

def Multiplication_table(m,n):

    for i in range(m+1):
        if i==0:
            for j in range(n+1):
                if j==0:
                    print("×", end="\t")
                else:
                    print(i + 1 ,end="\t")   
            print() 
                   
        else:
            for j in range(n+1):
                if j==0:
                    print(j + 1 , end="\t")
                else:
                    result = i * j
                    print(result, end="\t")
            print()   


Multiplication_table(m,n)