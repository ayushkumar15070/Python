import turtle

turtle.bgcolor("lightblue")

t = turtle.Turtle()

t.forward(100)
t.pencolor("red")
t.forward(100)

t.penup()
t.right(90)
t.forward(10)
t.pendown()
t.pencolor("red")
t.forward(100)
t.right(90)
t.pencolor("yellow")
t.forward(100)
t.right(90)
t.pencolor("green")
t.forward(100)
t.right(90)
t.pencolor("blue")
t.forward(100)

t.pencolor("#04AA6D")
t.penup()
t.left(90)
t.forward(10)
t.pendown()
t.circle(100)

turtle.done()

