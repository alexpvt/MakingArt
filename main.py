import turtle as t
import random

tim = t.Turtle()
win = t.Screen()

color_list = ["light sea green", "cadet blue", "dark sea green", "medium sea green", "dark cyan", "dark slate gray"]

tim.speed(0)

def moving():
    tim.penup()
    tim.forward(30)
    tim.pendown()

def backward():
    tim.penup()
    tim.backward(30)
    tim.pendown()

def left():
    tim.left(30)

def right():
    tim.right(30)

def clean_screen():
    tim.reset()

def triagle():
    tim.color(random.choice(color_list))
    for i in range(20):
        tim.forward(100)
        tim.left(123)

def triagles():
    tim.color(random.choice(color_list))
    for i in range(20):
        tim.forward(50)
        tim.left(123)

    tim.color(random.choice(color_list))
    for i in range(50):
        tim.forward(100)
        tim.left(123)


win.listen()
win.onkey(moving, "w")
win.onkey(left, "a")
win.onkey(right, "d")
win.onkey(backward, "s")
win.onkey(triagles, "e")
win.onkey(triagle, "q")
win.onkey(clean_screen, "c")
win.exitonclick()

win.getcanvas().postscript(file="art01.eps")