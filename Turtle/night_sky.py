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
    moon.penup()
    moon.goto(x,y)
    moon.pendown()
    moon.begin_fill()
    moon.circle(50)
    moon.end_fill()
draw_moon((-300,120),"white")#full moon
draw_moon((-278,133),"black")#half moon

#Star creation
def draw_star(pos,color,length):
    x,y=pos
    star.color(color)
    star.penup()
    star.goto(x,y)
    star.pendown()
    star.begin_fill()
    for i in range(5):
        star.forward(length)
        star.right(144)
        star.forward(length)
    star.end_fill()
draw_star((100,100),"red",10)
draw_star((200,100),"yellow",30)

def write_text(color):
    text.color(color)
    text.penup()
    text.goto(-180,-270)
    text.pendown()
    style=('Stencil Std Bold',50,'italic')
    text.write('Good Night',font=style,move=True)
write_text("green")


turtle.done()
#window.mainloop()