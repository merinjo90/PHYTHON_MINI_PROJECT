import turtle

flag=turtle.Turtle()
screen=turtle.Screen()

flag.speed(4)
flag.pensize(6)
flag.color("#000080")

def draw(x,y):
    flag.penup()
    flag.goto(x,y)
    flag.pendown()

#ashoka Chakra
for i in range(24): #24 strokes in ashok chakra
    flag.forward(80)
    flag.backward(80)
    flag.left(15) #360 divide by 24 then get 15
draw(0,-80)
flag.circle(80,360)

draw(0,-90)

#green rectangle
flag.color("green")
flag.begin_fill()

flag.forward(350)
flag.backward(700)
flag.right(90)
flag.forward(200)
flag.left(90)
flag.forward(700)
flag.left(90)
flag.forward(200)
flag.left(90)

flag.end_fill()


turtle.done()


screen.mainloop()