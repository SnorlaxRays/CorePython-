import datetime
D = datetime.datetime(2022,6,8,2,48,50)
s = '{: %Y-%m-%d %H:%M:%S}'.format(D)
print(s)