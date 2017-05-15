import turtle
t = turtle.Pen()
number = int(turtle.numinput("Number of sides or circles",
            "How many sides or circles in your shape?", 6))
shape = turtle.textinput("Which shape do you want?",
                         "Enter 'p' for polygon or 'r' for rosetty:")
for x in range(number):
    if shape == 'r':
        t.circle(100)
    else:
        t.forward (150)
    t.left(360/number)

for x in range(number):
    if shape == 'r':
        t.pencolor("white")
        t.circle(100)
    else:
        t.pencolor("white")
        t.forward (150)
        t.left(360/number)
    
