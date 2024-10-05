temprature = input('what is the temprature')
if int(temprature) > 35: # {35 and above}
    print("it is a very hot day")
    print("drink alot of water")
elif int(temprature) > 20: # {20 and 35}
    print("it's a nice day")
elif int(temprature) > 10: # {10 and 20}
    print("it's a cool day")
else: # {0 and 10}
    print("its a very cool day")
print("done")