'''
Drawing patteren using Turtle
'''
import turtle as t 
t.penup() 
x = 0 
y = 0 
t.goto(x,y) #Move pen at location x and y 
t.penup()
for i in range(1,10):# value of i varies from 1 to 10 
    y = y - 10
    for j in range(1,10): # Value of j varies from 1 to 10 
        if j<=i:
            t.penup()
            t.speed(10)
            t.forward(20)
            t.write('^')
    t.goto(x, y)
t.mainloop()