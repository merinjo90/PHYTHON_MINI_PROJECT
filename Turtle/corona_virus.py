from turtle import *
setup(width=800,height=700)
color("red")
bgcolor("black")
speed(11)
hideturtle()
goto(25,152)
b=0
while b<200:
    right(b)
    forward(b*3)
    b=b+1
done()