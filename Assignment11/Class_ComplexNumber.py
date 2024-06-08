class Complex:
    def __init__(self, rr, ii):
        # properties
        self.real = rr
        self.image = ii

    # methods
    def show(self):
        print(self.real, "+", self.image, "i")

    def sum(self, other):
        result_r = self.real + other.real
        result_i = self.image + other.image
        result = Complex (result_r , result_i)
        return result

    def mul (self , other) :
        result_r = self.real * other.real - self.image * other.image
        result_i = self.real * other.image + self.image *other.real
        result = Complex (result_r , result_i)
        return result

    def sub(self, other):
        result_r = self.real - other.real
        result_i = self.image - other.image
        result = Complex(result_r, result_i)
        return result


r1 = 10
i1 = 5
com1 = Complex(r1,i1)
com1.show()

r2 = 7
i2 = 8
com2 = Complex(r2,i2)
com2.show()


print("Result of Sum:")
s1=com1.sum(com2)
s1.show()

print("Result of Mul:")
m=com1.mul(com2)
m.show()

print("Result of Sub:")
s2=com1.sub(com2)
s2.show()