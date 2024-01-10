student_grades = []

while True :

    x = input("enter your grades or exit :")

    if x != "exit" :
        student_grades.append(float(x))

    elif x == "exit" :
        avg = sum(student_grades) / len(student_grades)
        print("average :",avg)
        break
        
