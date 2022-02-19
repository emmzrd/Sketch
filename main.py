from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def move_backward():
    tim.backward(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.goto(0, 0)
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
