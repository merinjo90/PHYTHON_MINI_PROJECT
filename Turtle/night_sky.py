import turtle
import random

#window setup
window=turtle.Screen()
window.setup(width=800,height=600)#window size
window.bgcolor("black")#background color

colors=['red','blue','orange','yellow','magenta','purple','peru','ivory','silver','lightpink','snow','floralwhite','lavender','lime','limegreen','aqua','crimson','navy','darkviolet','darkgreen']

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

#Star creation
def draw_star(x,y,color,length):
    #x,y=pos
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

def rand_pos():
    return random.randint(-390,390),random.randint(-290,290)
def rand_length():
    return random.randint(5,25)

#text creation
def write_text(color):
    text.color(color)
    text.penup()
    text.goto(-180,-270)
    text.pendown()
    style=('Stencil Std Bold',50,'italic')
    text.write('Good Night',font=style,move=True)

#main program

draw_moon((-300,170),"white")#full moon
#draw_moon((-278,133),"black")#half moon

while True:
    color = random.choice(colors)
    x,y=rand_pos()
    length=rand_length()

    draw_star(x,y,color,length)
    write_text(color)


turtle.done()