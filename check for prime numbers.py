a=int(input("Enter the number"))
count=0
for i in range(2,a):
    if(a%i==0):
        count=count+1
if(count==0):
        print("The number is a prime number")
else:
        print("The number is a composite number")