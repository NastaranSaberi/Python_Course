import math

class Fraction:
    def __init__(self, nn, dd):
        # properties
        self.numerator = nn
        self.denominator = dd

    # methods
    def show(self):
        print(self.numerator , "/" , self.denominator)

    def sum(self,other):
        result_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        result_denominator = self.denominator * other.denominator
        result = Fraction(result_numerator, result_denominator)
        return result
    
    def sub(self, other):
        result_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        result_denominator = self.denominator * other.denominator
        x = Fraction(result_numerator, result_denominator)
        return x

    def mul(self, other):
        result_numerator = other.numerator * self.numerator
        result_denominator = other.denominator * self.denominator
        x = Fraction(result_numerator, result_denominator)
        return x
 
    def div(self, other):
        result_numerator = self.numerator * other.denominator
        result_denominator = self.denominator * other.numerator
        x = Fraction(result_numerator, result_denominator)
        return x
 
    def convert_fraction_to_number(self):
        if self.denominator != 0:
            number = self.numerator / self.denominator
            return number
        else:
            return "The denominator of the fraction is 0."

    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        result_numerator = self.numerator // gcd
        result_denominator = self.denominator // gcd
        x = Fraction(result_numerator, result_denominator)
        return x

    

print("Fraction 1:")
a = Fraction(2, 4) 
a.show() 

print("Fraction 2:")
b = Fraction(1, 2) 
b.show()

print("Result of Mul:")
z = b.mul(a)
z.show()

print("Result of Sum:")
w = a.sum(b)
w.show()

print("Result of Sub:")
x = a.sub(b)
x.show()

print("Result of Div:")
t = b.div(a)
t.show()

print("Convert a fraction to number")
f = a.convert_fraction_to_number()
print(f)

print("Result of Simplify:")
g = a.simplify()
g.show()


