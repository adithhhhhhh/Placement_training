a=int(input("Enter the number"))
total=0
while(a>0):
    total=total+a%10
    a=a//10
print("The sum of digits is",total)