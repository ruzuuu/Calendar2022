import calendar

# sets the calenday to start on sunday
calendar.setfirstweekday(calendar.SUNDAY)

# month (input 1, 2, ..., 12) and year
yy = 2022
mm = int(input("Enter month: "))

# calendar default pattern
print(calendar.month(yy, mm, w=3))