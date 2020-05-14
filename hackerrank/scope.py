class Difference:
    def __init__(self, a):
        self.__elements = a

    maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        result = []
        for i in range(0, len(self.__elements)):
            for j in range(i+1, len(self.__elements)):
                result.append(abs(a[i]-a[j]))
        # print(result)
        for i in range(0, len(result)):
                if result[i] > self.maximumDifference:
                    self.maximumDifference = result[i] 
            

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)