age1 = int(input("Enter the Age of 1 child: "))
age2 = int(input("Enter the Age of 2 child: "))
age3 = int(input("Enter the Age of 3 child: "))
if age1 < age2 and age1 < age3:
    print("The Youngest Age is 1 child")
elif age2 < age1 and age2 < age3:
    print("The Youngest Age is 2 child")
else:
    print("The Youngest Age is 3 child")