b=int(input("Enter num of blocks"))
l=int(input("Enter num of lines"))
s=int(input("Enter no of stars per line"))
sum=0
count=0
print("-----------------")
for i in range(b):
    print(f"------{i+1}------")
    count=0
    for i in range(l-i):
        for k in range(s):
            print("*",end=" ")
            count=count+1
        print()
    print(count)
    sum+=count
print(f"total:{sum}")
    