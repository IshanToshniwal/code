import random

print('--------------------------instructions-------------------------- \n1. Choose ODD or EVEN \n2. If you win the '
      'Toss, opt bat or ball \n4. If number matches with AI number'
      'then it is out \n5. If u cheat the game restarts '
      '\n-----------------------------------------------------------------')

balls = int(input('Enter the number of ball 6 balls = 1 over: '))


def first_bating():
    print('You are all set to bat now: ')
    score = 0
    x = 0
    var = balls
    while x <= int(balls):
        x += 1
        ai = random.randint(1, 6)
        var = var - 1
        print(var, 'Balls left')
        mine = int(input('Bat: '))
        if mine > 6:
            print('Invalid--Restarting')
            toss()
        print('AI bowls', ai)
        score = score + mine
        print('Your score =', score)
        print('AI score 0')
        if ai == mine:
            print('Out')
            print('Score', score)
            break
    print('AI require to win', score + 1, 'runs to win')
    print('AI is ready')
    ai_score = 0
    ai_balls = balls
    var1 = ai_balls
    v = 0
    while v <= int(ai_balls):
        v += 1
        var1 = var1 - 1
        print(var1, 'Balls left')
        ai = random.randint(1, 6)
        mine = int(input('Bowl: '))
        if mine > 6:
            print('Invalid--Restarting')
            toss()
        print('AI bats', ai)
        ai_score = ai_score + ai
        print('AI score =', ai_score)
        print('Your score =', score)
        if ai_score > score:
            print('AI wins')
            print('Score of ai', ai_score, 'Your score =', score)
            exit()
        elif ai == mine:
            print('Out')
            print('You beat ai your score =', score, 'AI score =', ai_score)
            exit()
        elif ai_score == score:
            print('It is a tie')
            exit()


def second_bating():
    print('AI is ready to bat')
    ai_score = 0
    ai_balls = balls
    var1 = balls
    v = 0
    while v <= int(ai_balls):
        v += 1
        var1 = var1 - 1
        print(var1, 'Balls left')
        ai = random.randint(1, 6)
        mine = int(input('Bowl: '))
        print('AI bats', ai)
        if mine > 6:
            print('Invalid--Restarting')
            toss()
        ai_score = ai_score + ai
        print('AI score =', ai_score)
        print('Your score 0')
        if ai == mine:
            print('Out')
            print('AI score', ai_score)
            break
    print('You require to win', ai_score + 1, 'Runs to win')
    print('Player is ready to bat')
    score = 0
    x = 0
    var = balls
    while x <= int(balls):
        x += 1
        var = var - 1
        print(var, 'Balls left')
        ai = random.randint(1, 6)
        mine = int(input('Bat: '))
        if mine > 6:
            print('Invalid--Restarting')
            toss()
        print('AI bowls', ai)
        score = score + mine
        print('Your score =', score)
        print('AI score =', ai_score)
        if ai_score < score:
            print('You win')
            print('Score', score, 'AI score =', ai_score)
            exit()
        elif ai == mine:
            print('Out')
            print('AI beat you your score =', score, 'ai score =', ai_score)
            exit()
        elif ai_score == score:
            print('It is a tie')
            exit()


def toss():
    player = input('Toss time choose between odd or even: ')
    options = ('odd', 'even')
    player = player.lower()
    coin = ('odd', 'even')
    odd_even = random.choice(coin)
    if player == 'odd' and odd_even == 'odd' or player == 'even' and odd_even == 'even':
        print('You won the toss')
        bat_or_ball = input('What do you want to do |bat or ball|: ')
        bat_or_ball = bat_or_ball.upper()
        if bat_or_ball == 'BAT':
            first_bating()
        elif bat_or_ball == 'BALL':
            second_bating()
        else:
            print('Invalid--Restarting')
            toss()
    elif player == 'odd':
        computer = 'even'
        if computer == 'even' and coin == 'even':
            print('AI won the toss')
        bat_or_ball1 = ('bat', 'ball')
        tarball = random.choice(bat_or_ball1)
        if tarball == 'bat':
            second_bating()
        elif tarball == 'ball':
            first_bating()
    elif player == 'odd':
        computer = 'odd'
        if computer == 'odd' and coin == 'odd':
            print('AI won the toss')
        bat_or_ball1 = ('bat', 'ball')
        tarball = random.choice(bat_or_ball1)
        if tarball == 'bat':
            second_bating()
        elif tarball == 'ball':
            first_bating()
    else:
        print('No one won toss')
        toss()


toss()