n = int(input("Please enter the row number: "))

def Khayyam_Triangle(n):

    list = []
    for i in range (n):
        pattern = []
        for j in range (i+1):
            if j==0 or j==i:
                pattern.append(1)
            else:
                pattern.append(list[i-1][j-1] + list[i-1][j])
        list.append(pattern)
    
    for i in range(n):
        for j in range(i+1):
            print(list[i][j] ,end="\t")
        print()


Khayyam_Triangle(n)
