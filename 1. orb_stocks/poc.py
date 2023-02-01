import datetime

now = datetime.datetime.now();
today9_15am = now.replace(hour=9, minute=15, second=0, microsecond=0)

print(now < today9_15am)