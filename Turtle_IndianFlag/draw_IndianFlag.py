import turtle

flag=turtle.Turtle()
screen=turtle.Screen()

flag.speed(4)
flag.pensize(6)
flag.color("#0541B7")

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
#turtle.done()





screen.mainloop()