

a = int(input("Enter the num1"))
b = int(input("Enter the num2"))
r = 0
while (b != 0):
    r = a % b
    a = b
    b = r

print(a)
