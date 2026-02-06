import turtle

# Setup layar
screen = turtle.Screen()
screen.title("Segitiga Biru")
screen.bgcolor("white")

# Buat turtle
t = turtle.Turtle()
t.speed(5)
t.pensize(3)
t.color("black", "blue")  # garis hitam, isi biru
t.hideturtle()

# Mulai menggambar segitiga
t.penup()
t.goto(-100, -50)
t.pendown()

t.begin_fill()
for _ in range(3):
    t.forward(200)
    t.left(120)
t.end_fill()

turtle.done()