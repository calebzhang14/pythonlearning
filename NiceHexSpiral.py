import turtle
t = turtle.Pen()
t.speed(0)
sides = 4
colors=['red', 'purple', 'blue', 'green', 'yellow', 'orange', 'black']
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3 / sides + x)
    t.left(360/sides + 91)
    #t.left(58635386568)
    t.width(x*sides/200)