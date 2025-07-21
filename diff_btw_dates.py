from datetime import datetime

date1_str = input("Enter first date (e.g. your birthday) [DD-MM-YYYY]: ")
date2_str = input("Enter second date (e.g. today) [DD-MM-YYYY]: ")

date1 = datetime.strptime(date1_str, "%d-%m-%Y")
date2 = datetime.strptime(date2_str, "%d-%m-%Y")

diff = abs((date2 - date1).days)

print(f"\nDifference between {date1_str} and {date2_str} is {diff} days.")
