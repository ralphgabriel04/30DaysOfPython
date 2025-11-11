# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime, date
now = datetime.now()
print("Day:", now.day)
print("Month:", now.month)
print("Year:", now.year)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Timestamp:", now.timestamp())
# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted date:", formatted_date)
# Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("Converted datetime object:", date_object)
# Calculate the time difference between now and new year.
today = date.today()
new_year = date(today.year+1, 1, 1)
time_left = new_year - today
print("Time left until New Year:", time_left)
# Calculate the time difference between 1 January 1970 and now.
time_now = datetime.now()
time_before = datetime(1970,1,1)
time_difference = time_now - time_before
print("Time difference since 1970-01-01:", time_difference)