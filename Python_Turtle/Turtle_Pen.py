import turtle

t = turtle.Turtle()

t.forward(100)
t.left(45)
t.penup()
t.forward(10)
t.pendown()
t.forward(100)
t.left(45)
t.penup()
t.forward(10)
t.pendown()
t.forward(100)
t.left(45)
t.penup()
t.forward(10)
t.pendown()
t.forward(100)
t.left(45)
t.penup()
t.forward(10)
t.pendown()
t.forward(100)
t.left(45)
t.penup()
t.forward(10)
t.pendown()
t.forward(100)
t.left(45)
t.penup()
t.forward(10)
t.pendown()
t.forward(100)
t.left(45)
t.penup()
t.forward(10)
t.pendown()
t.forward(100)
t.left(45)
t.penup()
t.forward(10)
t.pendown()
t.forward(100)
t.left(45)
t.penup()
t.forward(10)
t.pendown()
t.forward(100)
t.left(45)
t.penup()
t.forward(10)
t.pendown()

shortening the code by using the for loop

size = int(input("Enter the number of sides which you want to draw: "))

i = 0

while i < size:
    t.forward(100)
    t.left(45)
    t.penup()
    t.forward(10)
    t.pendown()
    i = i + 1


t.pensize(5)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

i = 0

while i < 4:
    t.pensize(3)
    t.forward(100)
    t.right(90)
    i = i + 1


t.hideturtle()
t.pensize(2)
t.forward(100)
t.right(90)
t.speed(1)
t.pensize(4)
t.right(90)
t.forward(344)
t.right(45)
t.speed(3)
t.pensize(10)
t.forward(100)
t.right(135)
t.pensize(11)
t.forward(200)

turtle.done()