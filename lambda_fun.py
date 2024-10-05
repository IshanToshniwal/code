# x = lambda y: y / i
# i = int(input('Enter a number: '))
# print(x(int(input('Enter a number: '))))
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = list(filter(lambda x: (x % 2), list1))
print(odd, '<-- This is odd numbers')
even = list(filter(lambda x: (x % 2 == 0), list1))
print(even, '<-- This is a even numbers')