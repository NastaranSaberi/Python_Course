import math

def cubic_equation(a, b, c, d):

    delta = (18*a*b*c*d) - (4*b**3*d) + (b**2*c**2) - (4*a*c**3) - (27*a**2*d**2)
    delta0 = (b**2) - (3*a*c)
    delta1 = (2*b**3) - (9*a*b*c) + (27*a**2*d)

    c = ((delta1 + math.sqrt(delta1**2 - 4*delta0**3))/ 2) ** (1/3)
    
    u1 = 1
    u2 = (-1 + 1j * math.sqrt(3)) / 2
    u3 = (-1 - 1j * math.sqrt(3)) / 2

    x1 = (-1/(3*a)) * (b + u1*c + (delta0 / (u1*c)))
    x2 = (-1/(3*a)) * (b + u2*c + (delta0 / (u2*c)))
    x3 = (-1/(3*a)) * (b + u3*c + (delta0 / (u3*c)))


    print("x1:", x1, "\nx2:", x2, "\nx3:", x3)

print("Enter the following values into the cubic equation")
a = float(input("Please enter a: "))
b = float(input("Please enter b: "))
c = float(input("Please enter c: "))
d = float(input("Please enter d: "))

cubic_equation(a, b, c, d)
