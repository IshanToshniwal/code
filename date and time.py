import datetime as t
x = t.datetime.now()
print(x)
print(x.year)
print(x.strftime('%A'))
print(x.strftime('%a'))
print(x.strftime('%B'))
print(x.strftime('%b'))
print(x.strftime('%Y-%m-%d %S:%M:%H'))
print(x.strftime('%m-%d-%Y %H:%M:%S'))