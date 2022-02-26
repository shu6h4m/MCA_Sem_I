'''
Program to use Turtle Module performing following task:
1. Print Rectangle
2. Print Square
3. Print Circle
4. Triangle
'''
import turtle #importing turtle module

turtle.bgcolor("black") #set bacground color to black
turtle.color("orange") #to set turtle color
turtle.pensize(8)

#Drawing Square
turtle.forward(200) #move turtle 200 pixels in direction of its current heading
turtle.left(90) #Rotate the turtle left by 90 degrees
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)

turtle.penup() #hide turtle line
turtle.backward(250) #going bckward from center
turtle.pendown() #show turtle line again
turtle.pensize(5)
turtle.bgcolor("green") #set bacground color to black
turtle.color("black")

#Drawing Rectangle
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.penup() #hide turtle line
turtle.goto(-150, -250) #going bckward from center
turtle.pendown() #show turtle line again
turtle.pensize(3)
turtle.bgcolor("pink") #set bacground color to black
turtle.color("red")


#Drawing Circle
turtle.circle(90)

turtle.penup() #hide turtle line
turtle.goto(10, -250) #going bckward from center
turtle.pendown() #show turtle line again
turtle.pensize(1)
turtle.bgcolor("white") #set bacground color to white
turtle.color("green")

turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(75)
turtle.write('shu6h4m')

turtle.showturtle()
turtle.exitonclick()