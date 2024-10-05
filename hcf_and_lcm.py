hcf_or_lcm = input('Enter HCF or LCM: ')
hcf_or_lcm = hcf_or_lcm.lower()
if hcf_or_lcm == 'hcf':
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    HCF = 1
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            HCF = i
    print("First Number is: ", a)
    print("Second Number is: ", b)
    print("HCF of the numbers is: ", HCF)
elif hcf_or_lcm == 'lcm':
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    HCF = 1
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            HCF = i
    LCM = (a * b) // HCF
    print("First Number is: ", a)
    print("Second Number is: ", b)
    print("LCF of the numbers is: ", LCM)