n = int(input("Please enter number of elements in the list : "))
list_main = []

for i in range (n) :
    number = int(input("Please enter number :"))
    list_main.append(number)

#simple way
# reverse_list = [list(reversed(list_main))]

reverse_list = []

for i in range (len(list_main)) :
    reverse_list.append(list_main[n-1])
    n -= 1


print(reverse_list)
