import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["cyan", "ghost white", "HotPink", "mint cream", "LimeGreen", "yellow2", "light cyan", "honeydew"]
sides = int(turtle.numinput("Number of sides",
                            "How many sides do you want (1-8)?", 4, 1, 8))
for x in range(360):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
    
