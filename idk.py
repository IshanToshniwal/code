import turtle
i = turtle.Turtle()
screen = turtle.Screen()
count = 0
i.color('')
while count < 90:
    count += 1
    i.forward(40)
    i.right(40.5)
    i.speed(-10000)
    i.circle(80)
    i.color('pink')
    screen.bgcolor('black')
while count < 140:
    count += 1
    i.forward(40)
    i.right(40.5)
    i.speed(-10000)
    i.circle(80)
    i.color('red')
turtle.done()