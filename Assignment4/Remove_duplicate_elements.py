n = int(input("Please enter number of elements in the list : "))
list_main = []

for i in range (n) :
    number = int(input("Please enter number :"))
    list_main.append(number)


new_list = []

for element in list_main :
    if element not in new_list :
        new_list.append(element)

print(new_list)