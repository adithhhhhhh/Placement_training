sum=0
while True:
    a=int(input("Enter marks"))
    if(a<100):
        sum+=a
    if(a==0):
        break
print("Sum is",sum)