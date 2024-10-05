# num = int(input('Enter the num of rows: '))
# for i in range(1, int(num) + 1):
#     space = num - i
#     for f in range(1, space + 1):
#         print(' ', end=' ')
#     for k in range(1, i + 1):
#         print('*', end=' ')
#     print()

# num = int(input('Enter the number of rows: '))
# for i in reversed(range(1, int(num) + 1)):
#     for k in reversed(range(1, i + 1)):
#         print('*', end=' ')
#     print('')

# rows = int(input('enter the number of rows: '))
# rows = rows // 2
# for k in range(rows):
#     spaces = rows - k - 1
#     for i in range(spaces):
#         print(end=' ')
#     for j in range(k + 1):
#         print('x', end=' ')
#     print()

# for k in reversed(range(rows)):
#     spaces = rows - k - 1
#     for i in reversed(range(spaces)):
#         print(end=' ')
#     for j in reversed(range(k + 1)):
#         print('x', end=' ')
#     print()

# rows = int(input('Enter a number: '))
# for i in range(rows):
#     print(' ' * (rows - i - 1) + 'x' * (2 * i + 1))
# for i in range(rows - 2, -1, -1):
#     print(' ' * (rows - i - 1) + 'x' * (2 * i + 1))