class complex_number():
    real=0
    imaginary=0

class complex_number_calculator():

    def add(a,b):
        c.real = a.real + b.real
        c.imaginary = a.imaginary + b.imaginary
        print(str(c.real) + "+" + str(c.imaginary) + 'i')

    def sub(a,b):
        c.real = a.real - b.real
        c.imaginary = a.imaginary - b.imaginary
        print(str(c.real) + "+" + str(c.imaginary) + 'i')

    def mult(a,b):
        real1 = a.real * b.real
        real2 = -(a.imaginary * b.imaginary)
        c.real = real1 + real2
        imaginary1 = a.real * b.imaginary
        imaginary2 = b.real * a.imaginary
        c.imaginary = imaginary1 + imaginary2
        print(str(c.real) + "+" + str(c.imaginary) + 'i')

    def div(a,b):
        b.imaginary=-b.imaginary
        real1 = a.real * b.real
        real2 = -(a.imaginary * b.imaginary)
        c.real = real1 + real2
        imaginary1 = a.real * b.imaginary
        imaginary2 = b.real * a.imaginary
        c.imaginary = imaginary1 + imaginary2

        divisor1 = b.real*b.real
        divisor2 = b.imaginary*b.imaginary
        divisor = divisor1 + divisor2

        c.real = c.real / divisor
        c.imaginary = c.imaginary / divisor
        print(str(c.real) + "+" + str(c.imaginary) + 'i')

a = complex_number()
a.real=int(input("Enter real component of first complex number"))
a.imaginary=int(input("Enter imaginary component of first complex number"))

b=complex_number()
b.real=int(input("Enter real component of second complex number"))
b.imaginary=int(input("Enter imaginary component of second complex number"))

c = complex_number()

if __name__=="__main__":
    complex_number_calculator.add(a,b)
    complex_number_calculator.sub(a,b)
    complex_number_calculator.mult(a,b)
    complex_number_calculator.div(a,b)