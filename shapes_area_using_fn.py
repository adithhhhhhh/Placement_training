def circle():
    r-int(input("Enter radius of circle :"))
    print("Area of circle is: ",3.14*r*r)
    
def square(a):
    print("Area of Square is: ",a*a)

def triangle():
    b=int(input("Enter base: "))
    h=int(input("Enter height: "))
    return 0.5*b*h 
    
def rect(a,b):
    return a*b
while(True):
    print("1.Circle")
    print("2.Square")
    print("3.Triangle")
    print("4.Rectangle")
    ch=int(input("Enter your choice: "))
    match ch:
        case 1:
            circle()
        case 2: 
            a=int(input("Enter side of Square"))
            square(a)
        case 3:
            res=triangle()
            print("Area of Triangle is ",res)
        case 4: 
            a=int(input("Enter length of Rectangle: "))
            b=int(input("Enter breadth of Rectangle: "))
            res=rect(a,b)
            print("Area of Rectangle is",res)
        case 5: 
            exit(0)
        case _:
            print("Invalid options")