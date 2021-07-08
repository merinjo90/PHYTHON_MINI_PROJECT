import turtle
screen=turtle.Screen() #pop up a new window

turtle.bgcolor("black") #change the backgrund clr of window
#turtle.color("black", "cyan") #stroke colour, Fill colour
#turtle.pensize(6)#change the stroke on the shape

turtle.up
turtle.goto(0,-100)
turtle.down
turtle.begin_fill()
turtle.fillcolor("cyan")
turtle.circle(100) #radius circle pixels
turtle.penup()
turtle.end_fill()
turtle.home()


turtle.up
turtle.goto(200,100)
turtle.down
turtle.begin_fill()
turtle.fillcolor("lime")
turtle.circle(120,steps=3) #draw triangle
turtle.penup()
turtle.end_fill()
turtle.home()

turtle.up
turtle.goto(-200,90)
turtle.down
turtle.begin_fill()
turtle.fillcolor("hotpink")
turtle.circle(100,steps=5) #draw pentagon
turtle.penup()
turtle.end_fill()
turtle.home()

turtle.up
turtle.goto(200,-250)
turtle.down
turtle.begin_fill()
turtle.fillcolor("coral")
turtle.circle(100,steps=6) #draw hexagon
turtle.penup()
turtle.end_fill()
turtle.home()

turtle.up
turtle.goto(-200,-250)
turtle.down
turtle.begin_fill()
turtle.fillcolor("crimson")
turtle.circle(100,steps=10)
turtle.penup()
turtle.end_fill()
turtle.home()
"""
def triangle():
    turtle.pensize(6)  # change the stroke on the shape
    turtle.begin_fill()
    turtle.fillcolor("orange")
    turtle.circle(100,steps=3) #radius circle pixels
    turtle.end_fill()
triangle()
turtle.reset()


def pentagon():
    turtle.pensize(6)  # change the stroke on the shape
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    turtle.circle(100,steps=5) #radius circle pixels
    turtle.end_fill()
pentagon()
turtle.reset()


"""


screen.exitonclick()
#screen=turtle.mainloop()
