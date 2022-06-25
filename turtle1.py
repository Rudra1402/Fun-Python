import turtle
siri = turtle.Turtle()
turtle.Screen().title("Star Pattern")
siri.speed(10)
siri.color("red")


def star():
    for i in range(30):
        siri.forward(200)
        siri.right(156)


star()
turtle.done()