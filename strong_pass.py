s=input("Enter your password")
up=0
dg=0
lo=0
spl=0
if(len(s)>0):
    for i in s:
         if(i.isupper()):
          up=up+1
         elif(i.islower()):
          lo=lo+1
         elif(i.isdigit()):
          dg=dg+1
         else:
          spl=spl+1
    if(up>0 and lo>0 and dg>0 and spl>0):
       print("Good Password")
    else:
      print("Bad password")
else:
    print("You need to increase the length of the password")