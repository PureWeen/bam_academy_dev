#This is the Template Repl for Python with Turtle.
#Python with Turtle lets you make graphics easily in Python.
#Check out the official docs here: https://docs.python.org/3/library/turtle.html
import turtle             # allows us to use the turtles library


wn= turtle.Screen()      # creates a graphics window
alex = turtle.Turtle()    # create a turtle named alex
alex.forward(150)         # tell alex to move forward by 150 units
alex.left(90)             # turn by 90 degrees
alex.forward(75)          # complete the second side of a rectangle

"""
t = turtle.Turtle()
x = 1
t.begin_fill()
while x < 4:
  t.color("red")
  t.forward(100)
  t.right(120)
  x = x+1
t.end_fill()

t.penup()
t.forward(-300)
t.pendown()
t.color("black")
t.forward(200)

"""


#t.forward(200)
#t.back(600)
#t.left(90) # 90 degree angle
#t.forward(200)



"""
# Set the background color to white

turtle.bgcolor("white")
t = turtle.Turtle()
# Set the turtle color to blue
t.color("blue")

import turtle
Window_ = turtle.Screen()
Window_.bgcolor("light green")
Window_.title("My Turtle")
#Window_.bgcolor("#FF7F00")
aaa = turtle.Turtle()
aaa.color("green")
aaa.forward(50)
aaa.right(90)
aaa.color("black")
aaa.forward(50)
Window_.exitonclick()
"""

"""

t = turtle.Turtle()
points = 1
while points < 5:
  t.right(200)
  t.forward(200)
  points += 1
"""


"""

## Solution to activity - make a microsoft logo in turtle
t = turtle.Turtle()

def square():
  for i in range(4):
    t.forward(200)
    t.right(90)

turtle.bgcolor("black")

t.color("blue")
t.begin_fill()
square()
t.end_fill()

t.penup()
#t.goto(100,-150)
t.backward(250)
#t.right(150)
t.pendown()
t.color("green")
t.begin_fill()
square()
t.end_fill()

t.penup()
t.left(90)
t.forward(250)
t.right(90)
t.pendown()
t.color("yellow")
t.begin_fill()
square()
t.end_fill()

t.penup()
#t.left(90)
#t.forward(300)
t.forward(250)
#t.right(90)
t.pendown()
t.color("red")
t.begin_fill()
square()
t.end_fill()




#t.forward(200)
#t.right(120)
#t.forward(200)
#t.right(120)
#t.right(90)
#t.forward(200)
#t.right(120)
#t.forward(200)
#t.right(120)
#t.backward(100)
#turtle.bgcolor("blue")
#t.left(90)
#t.forward(20)
"""
