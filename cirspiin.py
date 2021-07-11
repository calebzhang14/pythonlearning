import turtle
t=turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
colors=['red', 'orange', 'gold', 'yellow', 'yellow green', 'green', 'sea green', 'sky blue', 'blue', 'indigo', 'purple', 'magenta', 'pink', 'white']
sides = int(turtle.numinput("number of circles", "How many circles do you want (1-14)?", 8, 1, 14))
for x in range(180):
    t.pencolor(colors[x % sides])
    t.fillcolor(colors[x % sides])
    t.begin_fill()
    t.circle(x)
    t.end_fill()
    t.left(360 / sides + 1)
    t.width(x * sides / 200)