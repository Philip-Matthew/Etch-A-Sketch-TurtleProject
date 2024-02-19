from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def move_upwards():
    #tim.left(10)
    tim.setheading(tim.heading() + 10)
def move_downwards():
    tim.setheading(tim.heading() - 10)
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(move_forwards, "d")
screen.onkey(move_backwards, "a")
screen.onkey(move_upwards, "w")
screen.onkey(move_downwards, "s")
screen.onkey(clear_screen, "c")

screen.listen()
screen.exitonclick()