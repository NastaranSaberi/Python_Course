m = int(input("Enter number of row elements :"))
n = int(input("Enter number of column elements :"))

def checkered_board(m,n):

    for i in range (m):
        
        if i % 2 == 0:
            for j in range (n):
                if j % 2 != 0 :
                    print("*" , end="")
                else :
                    print("#" , end="")
 
            print()

        else :
            for j in range (n):
                if j % 2 == 0 :
                    print("*" , end="")
                else :
                    print("#" , end="")

            print()


checkered_board(m,n)
