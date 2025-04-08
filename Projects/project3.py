import turtle

t = turtle.Turtle()

t.color("cyan")
t.goto(100, 0)

for i in range (148):
    t.forward(100 + i)
    t.left(72 + 1)
    t.speed( 90 )
    t.color("cyan")
turtle.Screen().bgcolor("dark blue")

t.penup()
t.goto(-180, -150)
t.pendown()

for i in range (92):
    t.forward(60 + i)
    t.left(45 + 1)
    t.color("white")

t.penup()
t.goto(-180, 170)
t.pendown()

for i in range (28):
    t.color("blue")
    t.forward(20 + i)
    t.left(60 + 1)
    

turtle.exitonclick()