class rect:
    def set_dim(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

nums = []
d = int(input("Enter number of rectangles: "))
for i in range(d):
    R = rect()
    a = int(input("Enter length of rectangle: "))
    b = int(input("Enter breadth of rectangle: "))
    R.set_dim(a, b)
    nums.append(R)

index = 1
for i in nums:
    print("Area of Rectangle {} is {}".format(index, i.area()))
    index += 1
