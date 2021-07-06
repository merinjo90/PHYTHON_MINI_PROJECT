import turtle
import time

delay=0.1

#creating turtle screen
screen=turtle.Screen()
screen.title("SNAKE GAME")
screen.bgcolor("light gray")
screen.setup(width=600,height=600)
screen.tracer(0)

#snake head
snake=turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.speed(0)
snake.penup()
snake.goto(0,0)
snake.direction="stop"

def go_up():
    snake.direction="up"

def go_down():
    snake.direction="down"

def go_left():
    snake.direction="left"

def go_right():
    snake.direction="right"


#snake head moving
def snake_move():
    if snake.direction=="up":
        y=snake.ycor()
        snake.sety(y+20)
    if snake.direction=="down":
        y=snake.ycor()
        snake.sety(y-20)
    if snake.direction=="left":
        x=snake.xcor()
        snake.setx(x-20)
    if snake.direction=="right":
        x=snake.xcor()
        snake.setx(x+20)

screen.listen()
screen.onkeypress(go_up,"w")
screen.onkeypress(go_down,"s")
screen.onkeypress(go_left,"a")
screen.onkeypress(go_right,"d")

while True:
    screen.update()
    snake_move()
    time.sleep(delay)


#turtle.Terminator()
screen.mainloop()