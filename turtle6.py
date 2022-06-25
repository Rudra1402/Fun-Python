import turtle
colorList = ["red", "blue", "yellow", "green", "purple", "orange"]
r = turtle.Turtle()
r.speed(10)
for i in range(64):
    r.pensize(i/5)
    r.color(colorList[i%6])
    r.forward(i*1.75 + 40)
    r.left(45)
turtle.done()