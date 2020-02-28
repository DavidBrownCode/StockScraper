import timeit
import datetime


x = datetime.datetime.now()
today = x.strftime("%x")
print(today)
subDays = datetime.timedelta(days = 7)
weekAgo = (x - subDays)
print(weekAgo.strftime("%x"))