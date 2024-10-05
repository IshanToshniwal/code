def Factorial(num):
    factorial = 1
    if num < 0:
        return "Oops you have negative number"
    elif num == 0:
        return factorial
    else:
        for i in range(1,num+1):
            factorial = factorial*i
        return factorial
