import turtle
import colorsys

window=turtle.Screen()
turtle.speed(0)

def draw_semi_circle(col,r,val):
    turtle.color(col)
    turtle.circle(r,-180)
    turtle.up()
    turtle.setpos(val,0)
    turtle.down()
    turtle.right(180)

col=["violet","indigo","blue","green","yellow","orange","red"]

window.bgcolor("black")
turtle.width(10)
turtle.speed(1)
turtle.right(90)
turtle.width(10)
for i in range(7):
    draw_semi_circle(col[i],10*(i+8),-10*(i+1))



turtle.done
window.mainloop()