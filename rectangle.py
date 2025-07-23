class rectangle:
    prop1="Sum of all angles is 360"
    prop2="Each angle is 90"
    def sides(self):
        length=int(input("Enter length of rectangle: "))
        breadth = int(input("Enter breadth of rectangle: "))
        self.length=length
        self.breadth=breadth
    def area_per(self):
        print("Area of the rectangle is:  ",self.length*self.breadth)
        print("Perimeter of the rectangle is:  ",2*(self.length+self.breadth))

print("The Rectangle properties are:")
print(rectangle.prop1)
print(rectangle.prop2)
print("---------------------------")
a1=rectangle()
a2=rectangle()
a1.sides()
a2.sides()
a1.area_per()
a2.area_per()