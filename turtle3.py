import turtle
r = turtle.Turtle()
r.speed(5)
colorList = ["red", "green", "orange", "blue"]


def create(x,y,color):
    r.up()
    r.goto(x, y)
    r.down()
    r.begin_fill()
    r.fillcolor(color)
    r.circle(100)
    r.end_fill()
    r.up()
    r.home()
    r.down()


create(300, -100, colorList[0])
create(100, -100, colorList[1])
create(-100, -100, colorList[2])
create(-300, -100, colorList[3])
turtle.done()