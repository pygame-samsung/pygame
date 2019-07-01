import datetime

NOW = datetime.datetime.now()
print("-" * 25)
print(NOW)
print(NOW.year)
print(NOW.month)
print(NOW.day)
print(NOW.hour)
print(NOW.minute)
print(NOW.second)

print("-" * 25)
print("1 week ago was it: ", NOW - datetime.timedelta(weeks=1))
print("100 days ago was: ", NOW - datetime.timedelta(days=100))
print("1 week from now is it: ", NOW + datetime.timedelta(weeks=1))
print("In 1000 days from now is it: ", NOW + datetime.timedelta(days=1000))

print("-" * 25)
BIRTHDAY = datetime.datetime(2006, 11, 21, 16, 30)

print("Birthday in ... ", BIRTHDAY - NOW)
print("-" * 25)
