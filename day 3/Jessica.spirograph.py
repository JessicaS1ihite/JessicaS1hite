import turtle

tt = turtle.Turtle()
tt.screen.bgcolor('black')
tt.pensize(2)
tt.speed(10)

colors = ('red', 'magenta', 'blue',
          'cyan', 'green', 'white',
          'yellow')

# Iterate six times
for i in range(6):
    for color in colors:
        tt.color(color)
        tt.circle(100)
        tt.left(10)

tt.hideturtle()
turtle.done()
