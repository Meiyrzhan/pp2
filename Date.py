import datetime as dt
#Exercise 1------------------------------------------------------
n = dt.datetime.now()
five_days_ago = now - dt.timedelta(days=5)

print(now)
print(five_days_ago)
#Exercise 2------------------------------------------------------
n = dt.datetime.now()
y = n - dt.timedelta(days=1)
t= n + dttimedelta(days=1)

print(y.strftime("%Y-%m-%d"))
print(n.strftime("%Y-%m-%d"))
print(t.strftime("%Y-%m-%d"))
#Exercise 3------------------------------------------------------
dat = dt.datetime.now()
dat = dat.replace(microsecond=0)

print(dat)
#Exercise 4------------------------------------------------------
d1 = dt.datetime(2024, 2, 10, 14, 30, 0)
d2 = dt.datetime(2024, 2, 15, 18, 45, 30)

diff = d2 - d1
secs = diff.total_seconds()

print(secs)
