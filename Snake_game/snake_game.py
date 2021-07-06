import turtle
import time
import random

delay=0.1

#creating turtle screen
screen=turtle.Screen()
screen.title("SNAKE GAME")
screen.bgcolor("black")
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

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,150)
food.shapesize(0.5,0.5)

#snake head moving
def go_up():
    snake.direction="up"

def go_down():
    snake.direction="down"

def go_left():
    snake.direction="left"

def go_right():
    snake.direction="right"


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
screen.onkeypress(go_up,"Up")
screen.onkeypress(go_down,"Down")
screen.onkeypress(go_left,"Left")
screen.onkeypress(go_right,"Right")

while True:
    screen.update()
    #food position changed
    if snake.distance(food)<15:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

    snake_move()
    time.sleep(delay)


#turtle.Terminator()
screen.mainloop()