# In this example we will ask date to user. After we take the date we will say what day it is in that year.
# If user give the date like 01.01.2020, then it is a first day of 2020 year. So it will return '1'.

while(True):
    date = input("Please enter the date (day.month.year):") # Example: 12.11.2003
    day = int(date[0] + date[1]) # Day value will be the first 2 characters (0th and 1st) of date value.
    month = int(date[3] + date[4]) # month value will be the 3rd and 4th characters of date value.
    year = int(date[6] + date[7] + date[8] + date[9]) # year value will be the 6th,7th,8th and 9th value of date value.
    if day > 31 or day < 0: # if day value is not between 0 and 31;
        print("Day cannot equal to this value.")
    if (month > 12 or month <= 0): # If month value is not between 0 and 12;
        print("Month cannot equal to this value.")
    # We need to do something special for February month.
    if (month == 2 and day >= 30): # If month is February, but day value is equal to 30
        print("February does not take more than 29.")
    if (year % 4 == 0 and month == 2 and day >= 29): # If month is February, and year can be divided to 4, then February should take 28 days.
        print("February does not take more than 28 in this year.")
    else:
        break

series = [31,29,31,30,31,30,31,31,30,31,30,31] # Days of months
# We need to do something special for February month again.
if year % 4 == 0: # If a year can be divided to 4;
    series[1] = 28 # Make february month 28 days.

# After everything is ready, we create our function;
def day_count(d,m,y): # d=day,m=month,y=year;
    day_value = 0
    for i in range(0,m-1):
        day_value += series[i] # Add i index of series value to day_value. Let's say the month value is 3. That means
        # for loop will continue until i value will be equal to 3. When the loop is over, day_value will be equal to
        # 31+29+31 = 91
    day_value = day_value + int(d) # We also need to add days to day_value. If the date is 23.03.2019, then day_value will
    # be equal to 31+29+31 = 91 + 23 (day) = 114. So we can say date 23.03.2019 is the 114th day of 2019 year.
    return (day_value)
a = day_count(d=day,m=month,y=year) # We are sending our day,month and year values to our function called day_count
print(a) # And we are printing the day_count.