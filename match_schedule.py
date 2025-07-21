import random

n = int(input("Enter number of teams: "))
teams = []
for i in range(n):
    team = input("Enter team {} name: ".format(i+1))
    teams.append(team)

meeting = int(input("Enter number of meetings between one team: "))

matches = []
for i in range(n-1):
    for j in range(i+1, n):
        for k in range(meeting):
            matches.append((teams[i], teams[j]))

random.shuffle(matches)

print("-------")
index = 1
for match in matches:
    print("Match {}: {} vs {}".format(index, match[0], match[1]))
    index += 1
