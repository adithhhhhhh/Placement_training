legs=int(input("Enter the total num of legs:"))
heads=int(input("Enter total number of heads:"))
flag=False
for hen in range(heads):
    cow=heads-hen
    if(cow*4 + hen*2 == legs):
        print("Cows:",cow)
        print("Hens:",hen)
        flag=True
        break
if (not flag):
    print("No solution")
