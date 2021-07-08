import turtle
t=turtle.Turtle()
window=turtle.Screen()
t.up()
t.goto(200,0)

def circle1():
    t.up()
    t.goto(200, 0)
    list=["teal","lightcoral","darkviolet","saddlebrown"]
    for i in range(4):
        t.down()
        t.begin_fill()
        t.fillcolor(list[i])
        t.circle(100)
        t.end_fill()
        t.up()
        t.bk(120)
circle1()
t.reset()


def circle2():
    t.up()
    t.goto(200, 0)
    list=["yellow","red","blue","green"]
    for i in range(4):
        t.down()
        t.begin_fill()
        t.fillcolor(list[i])
        t.circle(50)
        t.end_fill()
        t.up()
        t.bk(100)
circle2()
t.reset()


def circle3():
    t.up()
    t.goto(200, 0)
    list=["yellow","red","blue","green"]
    for i in range(4):
        t.down()
        t.begin_fill()
        t.fillcolor(list[i])
        t.pensize(10)
        t.circle(50)
        t.end_fill()
        t.up()
        t.bk(100)
circle3()
t.reset()

def circle4():
    t.up()
    t.goto(200, 0)
    list=["yellow","red","blue","green"]
    for i in range(4):
        t.down()
        t.color(list[i])
        t.pensize(20)
        t.circle(100)
        t.up()
        t.bk(100)
circle4()

window.mainloop()