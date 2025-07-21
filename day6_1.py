n=int(input("Enter any no."))
l=[]
while n not in l:
    l.append(n)
    n=sum([int(i)*int(i) for i in str(n)])
if(n==1):
    print("round num")
else:
    print("not round")