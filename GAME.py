import random
name1=input("Enter player 1: ")
name2=input("Enter player 2: ")
print(" 5 numbers have been fixed")
print("You have to guess it, Be Ready!!!")

nums=[]
while(len(nums)!=5):
    d=random.randint(1,10)
    if(d not in nums):
        nums.append(d)
print("----------")
s1=0
s2=0
player1=[]
player2=[]
for i in range(3):
    print("-----Round{}-------".format(i+1))
    print("Dear{} guess ur choice".format(name1))
    ch=int(input())
    while(ch in player1 or ch in player2):
        ch=int(input("Number is taken, choose something else: "))
    player1.append(ch)
    if(ch in nums):
        print("---->Correct")
        s1=s1+1
    else:
        print("------->Wrong")
        
    print("Dear{} guess ur choice".format(name2))
    ch=int(input())
    while(ch in player1 or ch in player2):
        ch=int(input("Number is taken, choose something else: "))
    player2.append(ch)
    if(ch in nums):
        print("---->Correct")
        s2=s2+1
    else:
        print("------->Wrong")
print("---------------")
print("Computer has chosen: ",nums)
print("{} has chosen {}".format(name1,player1))
print("{} has a score of {}".format(name1,s1))
print("{} has chosen {}".format(name2,player2))
print("{} has a score of {}".format(name2,s2))
if(s1>s2):
    print("Winner is Player 1")
elif(s2>s1):
    print("Winner is Player 2")
else:
    print("No one wins")

        