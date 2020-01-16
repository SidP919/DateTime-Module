import datetime
import pytz #to install pytz type "pip install pytz" in the terminal window

today = datetime.date.today()
print("Today's date: " + str(today))

birthday = datetime.date(1995,10,21)
print("My birthday: "+str(birthday))

days_since_birth = (today-birthday).days
print("Days I've lived: " + str(days_since_birth))

ten_days_time_period = datetime.timedelta(days=10)

date_after_10days_from_today = today + ten_days_time_period
print("date after 10 days from today: " + str(date_after_10days_from_today))

date_before_10days_from_today = today - ten_days_time_period
print("date before 10 days from today: " + str(date_before_10days_from_today))

print(today.day)
print(today.weekday())# o/p 0 represents Monday, o/p 6 represents Sunday

print(datetime.time(7, 2, 20, 15))
#not recommended: datetime.time(h, m, s, ms)
#recommended: datetime.datetime(Y, M, D, h, m, s, ms)
#there's also: datetime.date(Y, M, D)

#time-delta
hour_delta = datetime.timedelta(hours=20)
after20hours = datetime.datetime.now() + hour_delta
print(datetime.datetime.now())
print(after20hours)
print()

#timezones
datetime_today = datetime.datetime.now(tz=pytz.UTC)
indian_datetime = datetime_today.astimezone(pytz.timezone('Asia/Kolkata'))
print(indian_datetime)
after10hours = indian_datetime + datetime.timedelta(hours=10)
print(after10hours)
print()

#to see the list of all timezones---------------->
# for timezone in pytz.all_timezones:
#   print(timezone)
print()

#String formatting with dates:--------------->
#convert 2020-01-16(a datetime object) to January 16, 2020
print(indian_datetime.strftime('%B %d, %Y'))#strftime for strING fORMATING time

#convert January 16, 2020 to 2020-01-16(a datetime object)
print(datetime.datetime.strptime('March 16, 2019', '%B %d, %Y'))#strptime for strING pARSING time
  