import turtle
r = turtle.Turtle()
r.speed(10)
r.penup()
r.right(180)
r.forward(250)
r.right(180)
r.pendown()
for i in range(5):
    r.forward(500)
    r.right(144)
    for j in range(5):
        r.forward(150)
        r.right(144)
        r.color("#123456", "orange")
        r.begin_fill()
        for k in range(5):
            r.forward(25)
            r.right(144)
        r.end_fill()
turtle.done()