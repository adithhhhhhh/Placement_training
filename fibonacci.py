def fibo(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
a=int(input("Enter any number:"))
for i in range(a):
    print(fibo(i),end=" ")