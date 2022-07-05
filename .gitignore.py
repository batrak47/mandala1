#save .py
import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
for i in range (10):
    for colours in ["blue", "green" ]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
        turtle.fillcolor('white')
turtle.forward(10)
turtle.left(10)
for j in range (10):
    for colours in ["red","white"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
        turtle.fillcolor('blue')
turtle.forward(10)
turtle.left(10)
for k in range (10):
    for colours in ["magenta", "gold"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
        turtle.fillcolor("gold")
turtle.hideturtle()
