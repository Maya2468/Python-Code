import turtle
turtle.bgcolor("black")
t = turtle.Pen()
colors = ["hot pink","yellow","cyan","green"]
for x in range(100):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)
