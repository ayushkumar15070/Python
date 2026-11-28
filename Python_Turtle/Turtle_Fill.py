import turtle

t = turtle.Turtle()

# t.fillcolor("blue") this will only fill the color inside the object

# t.color("red", "blue")

t.color("green")
t.begin_fill()

for i in range(4):
    if i == 3:
        t.forward(90)
        t.penup()
        t.forward(5)
        t.pendown()
        t.left(90)
    else:   
        t.forward(90)
        t.left(90)
t.end_fill()


t.color("yellow")
t.begin_fill()
for i in range(4):
        t.forward(90)
        t.right(90)
t.end_fill()

t.right(90)
t.right(90)
t.penup()
t.forward(5)
t.pendown()

t.color("blue")
t.begin_fill()
for i in range(4):
     t.forward(90)
     t.left(90)
t.end_fill()

t.right(90)
t.penup()
t.forward(5)
t.pendown()

t.color("red")
t.begin_fill()
for i in range(4):
    t.forward(90)
    t.left(90)
t.end_fill()
t.penup()
t.goto(-5, 100)

t.right(90)
t.pendown()
t.color("blue")
t.forward(105)
t.right(90)
t.forward(205)
t.right(90)
t.forward(205)
t.right(90)
t.forward(205)
t.right(90)
t.forward(105)

t.left(90)
t.penup()
t.forward(2)
t.right(90)
t.color("blue")
# t.begin_fill()

t.pendown()
t.forward(102)
t.right(90)
t.forward(209)
t.right(90)
t.forward(209)
t.right(90)
t.forward(208)
t.right(90)
t.forward(105)

# t.end_fill()


t.penup()
t.goto(-150, -180)
t.pendown()

t.color("orange")
t.begin_fill()
t.circle(50)
t.end_fill()



turtle.done()


