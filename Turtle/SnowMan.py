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



turtle.done
window.mainloop()
