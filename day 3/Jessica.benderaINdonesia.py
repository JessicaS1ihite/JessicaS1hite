import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Bendera Indonesia")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(5)
t.hideturtle()

# Fungsi gambar persegi panjang + outline
def draw_rectangle(x, y, width, height, fill_color, border_color="black"):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(border_color, fill_color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Ukuran bendera (rasio 2:3)
width = 300
height = 200

# Merah (atas)
draw_rectangle(-150, 100, width, height/2, "red")

# Putih (bawah)
draw_rectangle(-150, 0, width, height/2, "white")

# Outline hitam luar
t.penup()
t.goto(-150, 100)
t.pendown()
t.color("black")
for _ in range(2):
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)

turtle.done()