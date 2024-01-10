array = []
n = int(input("Please enter length of array :"))
result = True


for i in range(n) :
    number_array = int(input("Please enter your array members :"))
    array.append(number_array)

for i in range (len(array)-1) :
    if array[i] > array [i + 1] :
        result = False


if result :
    print("Array is sorted from small to large.")
else :
    print("Array is not sorted from small to large.")