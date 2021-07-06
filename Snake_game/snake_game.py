import turtle

#creating turtle screen
screen=turtle.Screen()
screen.title("SNAKE GAME")
screen.bgcolor("light gray")
screen.setup(width=600,height=600)
#screen.tracer(0)

#snake
snake=turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.speed(0)
snake.penup()
snake.goto(0,0)
snake.direction="stop"



screen.mainloop()