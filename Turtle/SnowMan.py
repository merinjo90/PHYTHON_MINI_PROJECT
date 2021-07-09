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


turtle.done
window.mainloop()
