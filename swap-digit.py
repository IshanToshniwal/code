num = int(input("Enter the Number :"))
a = num
sum1 = 0
while num > 0:
    rem = num % 10
    sum1 = (sum1 * 10) + rem
    num = num // 10
if a == sum1:
    print("Equal..")
else:
    print("Not Equal..")
