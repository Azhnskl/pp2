#task1
'''
from datetime import date , timedelta

current_date = date.today()
five_days_ago = current_date - timedelta(days=5)
print(current_date)
print (five_days_ago)
'''
#task2
'''
from datetime import date,timedelta
todays_day = date.today()
yesterdays_day = date.today()
tomorrows_day = date.today()

print(yesterdays_day - timedelta(days=1))
print(todays_day)
print(tomorrows_day + timedelta(days=1))
'''

#task3
'''
from datetime import datetime

current_datetime = datetime.now()
clean_datetime = current_datetime.replace(microsecond=0)

print(clean_datetime)
'''
#task4

from datetime import datetime

date1_str = input("Enter the first date : ")
date2_str = input("Enter the second date : ")


date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")


time_difference = abs((date2 - date1).total_seconds()) 


print(f"Difference between the two dates in seconds: {time_difference:.0f}")
