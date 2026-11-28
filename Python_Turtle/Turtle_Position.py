import turtle 


t = turtle.Turtle()

t.speed(1)
t.goto(100, 0)
t.goto(50, 100)
t.goto(0, 0)
t.speed(3)
t.color("red")
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)


t.color("blue")
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)


t.color("purple")
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

t.color("blue")
t.forward(100)
t.penup()
t.forward(10)
t.pendown()
t.left(90)
t.circle(110)

t.color("orange")
t.right(90)
t.penup()
t.forward(10)
t.pendown()
t.left(90)
t.circle(120)


t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

t.penup()
t.goto(-100, 50)
t.pendown()
t.forward(200)


t.setheading(90)
t.forward(100)

t.forward(100)
t.right(90)
t.forward(100)

t.home()

print(t.position())



turtle.done()