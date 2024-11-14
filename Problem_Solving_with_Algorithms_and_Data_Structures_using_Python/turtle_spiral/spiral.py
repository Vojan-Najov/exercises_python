import turtle

my_turtle = turtle.Turtle()
myWin = turtle.Screen()

def draw_spiral(my_turtle, linelen):
    if linelen > 0:
        my_turtle.forward(linelen)
        my_turtle.right(90)
        draw_spiral(my_turtle, linelen - 5)

draw_spiral(my_turtle, 100)
myWin.exitonclick()
