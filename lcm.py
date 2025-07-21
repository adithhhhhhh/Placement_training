a = int(input("Enter the 1st number"))
b = int(input("Enter the 2nd number"))
if (a > b):
    big = a
else:
    big = b
step = big
while True:
    if (big % a == 0 and big % b == 0):
        print("lcm is", big)
        break
    else:
        big = big + step