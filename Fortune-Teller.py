import turtle
import random
pointer = turtle.Turtle()
pointer.turtlesize(3, 3, 2)
pen = turtle.Turtle()
spin_amuont = random.randint(1,360)
pen.penup
pen.goto(200, 0)
pen.pendown()
pen.write("Of Course!!!!!", font=('Open Sans', 30))
pen.penup
pen.goto(-400, 0)
pen.pendown()
pen.write("NEVER IN A MILLION YEARS!!!", font=('Open Sans', 30))
pen.penup
pen.goto(-100, 300)
pen.pendown()
pen.write("Uhhhhhhhhhh, maybe??? ", font=('Open Sans', 30))
pen.penup
pen.goto(0, -200)
pen.pendown()
pen.write("Yes, but after 100 years!!!", font=('Open Sans', 30))
pen.penup