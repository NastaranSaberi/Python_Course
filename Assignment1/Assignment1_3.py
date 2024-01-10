first_name = input("Please enter your first name :")
last_name = input("Please enter your last name :")

score1 = float(input("First score:"))
score2 = float(input("Second score:"))
score3 = float(input("Third score:"))

avg = (score1 + score2 + score3) /3

if avg >= 17 :
    result = "Great"

elif avg >= 12 and avg < 17 :
    result = "Normal"

elif avg < 12 :
    result = "Fail"

print(first_name , last_name, "your average is" , avg , ".")
print("Your educational status:" , result)

