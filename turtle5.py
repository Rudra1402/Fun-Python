import turtle
turtle.Screen().title("Tiranga")
r = turtle.Turtle()
r.speed(10)
def gotofunction(x, y):
    r.up()
    r.goto(x, y)
    r.down()
def forwardleft(f, l):
    r.forward(f)
    r.left(l)
colorList = ["orange", "white", "green"]
gotofunction(-150, 150)
r.pensize(3)
for i in range(3):
    r.begin_fill()
    r.fillcolor(colorList[i])
    forwardleft(300, 90)
    forwardleft(75, 90)
    forwardleft(300, 90)
    if i != 2:
        forwardleft(150, 90)
    else:
        forwardleft(300, 90)
    r.end_fill()
r.color("blue")
gotofunction(0, 147.5)
r.circle(-35)
r.right(90)
r.pensize(0.5)
for i in range(12):
    forwardleft(70, 90)
    r.circle(35, 15)
    r.left(90)
forwardleft(31, -90)
r.begin_fill()
r.circle(5)
r.end_fill()
r.hideturtle()
turtle.done()