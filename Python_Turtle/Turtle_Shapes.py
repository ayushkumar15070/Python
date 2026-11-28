import turtle 

t = turtle.Turtle()



count = 1
for i in range(4):
    match count:
        case 1:
            t.color("red")
        case 2:
            t.color("yellow")
        case 3:
            t.color("green")
        case 4:
            t.color("blue")
        case _:
            print("Something is missing!!")

    t.forward(100)
    t.right(90)
    count = count + 1

anothercount = 1

for i in range(3):
    match anothercount:
        case 1:
            t.color("Red")
        case 2:
            t.color("yellow")
        case 3:
            t.color("green")
        case _:
            print("Something is wrong!!")

    t.forward(100)
    t.right(120)
    anothercount = anothercount + 1


sides = 8

for i in range(sides):
    t.forward(100)
    t.left(360 / sides)
t.penup()
t.right(120)
t.forward(10)
t.pendown()
t.left(120)


for i in range(sides):
    t.forward(108)
    t.left(360 / sides)



def polygon(sides, size):
    for i in range(sides):     
        t.forward(size)
        t.left(360 / sides)

polygon(3, 40)
polygon(8, 90)
polygon(9, 90)

t.penup()
t.goto(-100, -100)
t.pendown()
t.circle(45)

t.color("blue")
t.circle(100, 270)




turtle.done()
