import turtle as t
colors=['red','purple','blue','green','orange','yellow']
t.bgcolor('black')
t.speed(10)
for i in range (360):
    t.pencolor(colors[i%6])
    t.width(i/100)
    t.forward(i+50)
    t.left(158)
t.exitonclick()    