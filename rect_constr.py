import random
class rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

nums = []
d = int(input("Enter number of rectangles: "))
for i in range(d):
    R = rect(random.randint(2,8),random.randint(4,10))
    nums.append(R)

index = 1
for i in nums:
    print("Area of Rectangle {} is {}".format(index, i.area()))
    index += 1
for i in nums:
    if i.area()%2==0:
        print(i.area())
