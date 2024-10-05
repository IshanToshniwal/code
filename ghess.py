import random
num = random.randrange(1, 100)
print('we will play guessing game')
no_of_guess = 0
while no_of_guess <= 10:
    no_of_guess +=1
    n = int(input('Enter a number:'))
    if num > n:
        print('the number is too low')
    elif num < n:
        print('the number is too high')
    elif num == n:
        break
if num == n :
    print('it is correct in this many tries', no_of_guess)
else:
    print('the number was', num)