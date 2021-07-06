import turtle
import time
import random

delay=0.1
segment=[]
score=0
high_score=0

#creating turtle screen
screen=turtle.Screen()
screen.title("SNAKE GAME")
screen.bgcolor("#FFF873")
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
food.color("red")
food.penup()
food.goto(0,150)
food.shapesize(0.5,0.5)

#score
scoring=turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,260)
scoring.write("Score=0   High Score:0",align="center",font=("corier",16,"normal"))

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

#snake and border collision
    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.xcor()<-290:
        time.sleep(2)
        snake.goto(0,0)
        snake.direction="stop"
        for seg in segment:
            seg.goto(1500,1500)
        segment.clear()
        score=0 #border touch,when game is over and score reset to zero
        scoring.clear()
        scoring.write("Score = {} High Score ={}".format(score, high_score), align="center",font=("corier", 16, "normal"))

    #food position changed
    if snake.distance(food)<15:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segment.append(new_segment)

#food touch when calculate score
        score=score+10
        if score>high_score:
            high_score=score
            scoring.clear()
            scoring.write("Score = {} High Score ={}".format(score,high_score),align="center",font=("corier",16,"normal"))

    for index in range(len(segment)-1,0,-1):
        x=segment[index-1].xcor()
        y=segment[index-1].ycor()
        segment[index].goto(x,y)

#snake length is increasing
    if len(segment)>0:
        x=snake.xcor()
        y=snake.ycor()
        segment[0].goto(x,y)

    snake_move()

#snake collision
    for seg in segment:
        if seg.distance(snake)<20:
            time.sleep(2)
            snake.goto(0,0)
            snake.direction="stop"
            for seg in segment:
                seg.goto(1500, 1500)
            segment.clear()
            score = 0  # body to body touch,when game is over and score reset to zero
            scoring.clear()
            scoring.write("Score = {} High Score ={}".format(score, high_score), align="center",font=("corier", 16, "normal"))

    time.sleep(delay)


screen.mainloop()
#turtle.Terminator()
