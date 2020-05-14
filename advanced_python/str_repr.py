class Person():
    def __init__(self):
        self.fname = "Iman"
        self.lname = "Pua"
        self.age = 23

    def __str__(self):
        return "Hello {0} {1} who is {2} years old".format(self.fname, self.lname, self.age)

    def __bytes__(self):
        val = "Person: {0} {1} of {2} years".format(self.fname,self.lname,self.age)
        return bytes(val.encode('utf-8'))

iman = Person()
print(str(iman))
print(bytes(iman))
