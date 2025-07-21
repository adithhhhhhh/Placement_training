#We want to make denominations of an amount to have least number of notes acc to Indian value and sort the lsit of money in descending order 

denomination = [1, 2, 5, 10, 20, 50, 100, 200, 500]
money = int(input("What is the amount you want to denominate: "))

# Sort in descending order
denomination.sort(reverse=True)

result = []

for note in denomination:
    if money >= note:
        count = money // note
        result.append((note, count))
        money = money % note

print("Denomination breakdown (note : count):")
for note, count in result:
    print(f"{note} : {count}")
