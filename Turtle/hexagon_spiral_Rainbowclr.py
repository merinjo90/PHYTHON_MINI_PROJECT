import turtle #importing turtle
colors_list=["violet","Indigo","blue","green","yellow","orange","red"] #define list of clrs
t=turtle.Pen()
for x in range(360): #creating loop for repeating
    #t.pencolor(colors_list[x%6]) #pen color change in every run
    t.pencolor(colors_list[x%7]) #pen color change in every run
    t.width(x/100+1) # value of x will be change from 0 to 359
    t.forward(x) #use to move the turtle forward by the value
    t.left(59)#use to change the direction of circle
turtle.Terminator()

