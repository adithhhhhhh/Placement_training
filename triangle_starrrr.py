rows = int(input("Enter number of rows: "))
for i in range(rows):
    # Print spaces first
    for j in range(rows - i - 1):
        print(" ", end="")
    # Print stars: 2*i + 1 stars in each row
    for k in range(2 * i + 1):
        print("*", end="")
    print()
