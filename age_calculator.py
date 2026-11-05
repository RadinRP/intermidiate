year = int(input("enter your age"))
month = int(input("enter your birth mounth"))
day = int(input("enter your day"))
current_year = 1405
current_month = 6
current_day = 29
if (current_day < day):
    current_month -= 1
    current_day += 30
if (current_month < month):
    current_year -= 1
    current_month += 12
result_year = current_year - year
result_month = current_month - month
result_day = current_day - day
print("you have",result_year,"year and",result_month,"month and",result_day,"day")