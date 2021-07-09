import turtle
import random

#window setup
window=turtle.Screen()
window.setup(width=800,height=600)#window size
window.bgcolor("black")#background clr

moon=turtle.Turtle()
moon.hideturtle()


star=turtle.Turtle()
star.speed(0)
star.hideturtle()


text=turtle.Turtle()
text.speed(6)
text.hideturtle()
#draw moon with animation
def draw_moon(pos,color):
    x,y=pos
    moon.color(color)
    moon.begin_fill()
    moon.penup()
    moon.goto(x,y)
    moon.pendown()
    moon.circle(50)
    moon.end_fill()
draw_moon((-300,120),"white")


turtle.done()
#window.mainloop()