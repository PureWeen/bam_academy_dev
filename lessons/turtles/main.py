import turtle
"""
Window_ = turtle.Screen()
#Window_.bgcolor("light green")
Window_.title("Phillip;s Turtle")
Window_.bgcolor("#FF7F00")
#Window_.bgcolor(225,127,0)
aaa = turtle.Turtle()
aaa.color("green")
aaa.forward(50)
aaa.right(90)
aaa.color("black")
aaa.forward(50)
#Window_.exitonclick()
"""

"""
import turtle             # allows us to use the turtles library
star = turtle.Turtle()
num_of_sides = 3
length_of_side = 50
each_angle = 720.0 / num_of_sides
star_color = ["green","orange","black","blue","red",
             "green","orange","black","blue","red",
             "green","orange","black","blue","red",
              "green","orange","black","blue","red"
             ]
for i in range(num_of_sides):
  #star.color(star_color[i])
  
  #print("current color of star side: ", star_color[i])
  star.forward(length_of_side)
  star.right(each_angle)
turtle.done()
"""


turtle.shapesize()

turtle.resizemode("user")
turtle.shapesize(5, 5, 12)
turtle.shapesize()

turtle.shapesize(outline=50)
turtle.shapesize()
