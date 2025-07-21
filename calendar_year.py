
import calendar
year = int(input("Enter a year: "))
print("\nFull year calendar:")
print(calendar.calendar(year))
month = int(input("\nEnter month number (1-12): "))
print(f"\nCalendar for {calendar.month_name[month]} {year}:")
print(calendar.month(year, month))
