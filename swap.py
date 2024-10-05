c = int(input('enter c value: '))
d = int(input('enter d value: '))
print('before c value', c)
print('before d value', d)
a = c
c = d
d = a
print('after c value', c)
print('after d value', d)