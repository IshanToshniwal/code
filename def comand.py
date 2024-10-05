# def number(a, b):
#     print('the number =', a + b)


# x = int(input('enter 1 number'))
# y = int(input('enter 2 number'))
# number(x, y)
# def student(*t):
#     print(t[1])
#
#
# student('hi', 'by')
# def name(course='something'):
#     print('name of the course =', course)
#
#
# name('python')
# name('python beginner level')
# name()

# using for loop and while loop in def command
# class work def calculater
# def add(num1, num2):
#     print(num1, '+', num2, '=', num1 + num2)
#
#
# def sub(num1, num2):
#     print(num1, '-', num2, '=', num1 - num2)
#
#
# def divided(num1, num2):
#     print(num1, '÷', num2, '=', num1 / num2)
#
#
# def multiplication(num1, num2):
#     print(num1, '*', num2, '=', num1 * num2)
#
#
# num1 = int(input('Enter the first number: '))
# sing = input('Enter the sing +/-/*/÷ or /: ')
# num2 = int(input('Enter the second number: '))
# if sing == '+':
#     add(num1, num2)
# elif sing == '-':
#     sub(num1, num2)
# elif sing == '*':
#     multiplication(num1, num2)
# elif sing == '/' or sing == '÷':
#     divided(num1, num2)
# else:
#     print('ERROR__ERROR__RESTARTING__DO AGAIN')
#     exit()


def sum1(list1):
    s = 0
    for i in list1:
        if i % 2 == 0:
            s = s + i
    print(s)


l1 = [1, 3, 8, 7, 6, 4, 2, 0]
sum1(l1)
