import math

print("---------- Welcome to my calculator ---------- ")

print ("Operations of this calculator :")
print ("+")
print ("_")
print ("*")
print ("/")
print ("sin")
print ("cos")
print ("tan")
print ("cot")
print ("sqrt")
print ("factorial")
print ("log")


op = input("op:")

if op == "+" or op == "-" or op == "/" or op == "*" :
    a = float(input("please enter number1:"))
    b = float(input("please enter number2:"))

elif op == "sin" or op == "cos" or op == "cot" or op == "tan" :
    d = int(input("please enter degree :"))
    r = (d * math.pi) / 180

else :
    a = int(input("please enter number:"))


if op == "+" :
    result = a + b

elif op == "-" :
    result = a - b

elif op == "*" :
    result = a * b;

elif op == "/" :
    if b == 0:
        result = "Not exist"
    else :
        result = a / b

elif op == "sin" :
    result = math.sin(r)

elif op == "cot" :
    result = math.cos(r)

elif op == "tan" :
    result = math.tan(r)

elif op == "cot" :
    result = 1 / math.tan(r)

elif op == "log" :
    result = math.log(a)

elif op == "sqrt" :
    result = math.sqrt(a)

elif op == "factorial" :
    result = math.factorial(a)


print("Result: ", result)