import turtle

t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("yellow")
t.pendown()

# repeat these next two lines 5 times
for i in range(3):
    t.forward(100)
    t.left(150)
    t.forward(100)
    t.left(150)

turtle.exitonclick()