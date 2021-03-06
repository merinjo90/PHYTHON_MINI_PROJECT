import turtle

window=turtle.Screen()
#turtle=turtle.Turtle()
turtle.speed(0)
turtle.setup(width=800,height=700)

#blue background
turtle.penup()
turtle.goto(0,-320)
turtle.pendown()
turtle.color("lightskyblue")
turtle.begin_fill()
turtle.circle(300)
turtle.end_fill()

#body- bottom of body
turtle.penup()
turtle.goto(0,-280)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.circle(110)
turtle.end_fill()

#body- middle of body
turtle.penup()
turtle.goto(0,-110)
turtle.pendown()
turtle.begin_fill()
turtle.circle(90)
turtle.end_fill()

#head of snow man
turtle.penup()
turtle.goto(0,20)
turtle.pendown()
turtle.begin_fill()
turtle.circle(70)
turtle.end_fill()

#function to draw small black circe
def black_circle():
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

x=-20 #eyes
for i in range(2):
    turtle.penup()
    turtle.goto(x,110)
    turtle.pendown()
    black_circle()
    x=x+40

y=0 #buttons
for i in range(5):
    turtle.penup()
    turtle.goto(0,y)
    turtle.pendown()
    black_circle()
    y = y -55

#mouth
turtle.penup()
turtle.goto(0,70)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.circle(17)
turtle.end_fill()

turtle.penup()
turtle.goto(0,75)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.circle(17)
turtle.end_fill()

#right arms
turtle.penup()
turtle.goto(75,0)
turtle.pendown()
turtle.color("brown")
turtle.begin_fill()
turtle.left(40)
for i in range(2):
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(7)
    turtle.left(90)
turtle.end_fill()

#right finger1
turtle.penup()
turtle.goto(115,38)
turtle.pendown()
turtle.begin_fill()
turtle.left(40)
for i in range(2):
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(5)
    turtle.left(90)
turtle.end_fill()

#left arms
turtle.penup()
turtle.goto(-75,0)
turtle.pendown()
turtle.color("brown")
turtle.begin_fill()
turtle.left(40)
for i in range(2):
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(7)
    turtle.right(90)
turtle.end_fill()

#left finger1
turtle.penup()
turtle.goto(-110,47)
turtle.pendown()
turtle.begin_fill()
turtle.left(20)
for i in range(2):
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
turtle.end_fill()

window.mainloop()
