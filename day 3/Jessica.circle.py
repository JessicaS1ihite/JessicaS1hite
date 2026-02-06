import turtle

def tangentCircles(ttl):
    r = 10
    n = 10
    for i in range(1, n + 1):
        ttl.circle(r)
        ttl.penup()
        ttl.forward(2 * r)   # geser supaya saling menyinggung
        ttl.pendown()

def concentricCircles(ttl):
    r = 10
    for i in range(1, 11):
        ttl.penup()
        ttl.sety(-r * i)
        ttl.pendown()
        ttl.circle(r * i)

# turtle utama
Ben = turtle.Turtle()
Ben.speed(0)
Ben.pensize(2)

# Tangent circles (biru)
Ben.penup()
Ben.goto(-200, 150)
Ben.pendown()
Ben.pencolor("Blue")
tangentCircles(Ben)

# Concentric circles (merah)
Ben.penup()
Ben.goto(0, -50)
Ben.pendown()
Ben.pencolor("Red")
concentricCircles(Ben)

Ben.hideturtle()
turtle.done()