###import os
##
###os.getcwd()
##
##'''
###Loop Example
##
##import os
##import time
##import webbrowser
##
##total_breaks = 3
##breakCount = 0
##
##print("This program started on "+time.ctime())
##while(breakCount < total_breaks):
##    time.sleep(10) #7200
##    webbrowser.open("https://www.youtube.com/watch?v=xFedf-rVUwk")
##    breakCount = breakCount + 1
##
###Loop Example
##
##import os
##
##def rename_files():
##    files = []
##    #numbers = [0-9]
##    #path = r"C:\Users\vhawxhurst\AppData\Local\Programs\Python\Python36\prank"
##    path1 = "/Users/vhawxhurst/AppData/Local/Programs/Python/Python36/prank"
##    os.chdir(path1)
##    files = os.listdir(path1)#read in the list of files
##    
##    for fileName in files:
##        newName = ''.join([i for i in fileName if not i.isdigit()])
##        os.rename(fileName, newName)
##
##rename_files()
##'''

#Class Example
##import turtle
##
##
##def draw_square(some_turtle):
##    for i in range(1,5):
##        some_turtle.forward(100)
##        some_turtle.right(90)
##
##def draw_shape():
##    window = turtle.Screen() #create a window to draw on
##    window.bgcolor("red") #make this screen red
##
##    #create turtle brad - draws a square
##
##    brad = turtle.Turtle() #create an instance of a class called Turtle called brad
##    brad.shape("turtle")
##    brad.color("black")
##    brad.speed(2)
##    draw_square(brad) #calls the first function?

##    #create turtle angie - draws a circle
##    angie = turtle.Turtle()
##    angie.shape("arrow")
##    angie.color("blue")
##    angie.circle(100)

##    victoria = turtle.Turtle()
##    victoria.shape("classic")
##    victoria.color("yellow")
##    victoria.forward(60)
##    victoria.right(-60)
##    victoria.left(60)

##    window.exitonclick() #exit window on click
##
##draw_shape()


#Class Example 2
##import turtle
##
##
##def draw_square(some_turtle):
##    for i in range(1,5):
##        some_turtle.forward(100)
##        some_turtle.right(90)
##
##def draw_shape():
##    window = turtle.Screen() #create a window to draw on
##    window.bgcolor("white") #color window
##
##    #create turtle brad - draws a square
##
##    brad = turtle.Turtle() #create an instance of a class called Turtle called brad
##    brad.shape("turtle")
##    brad.color("yellow")
##    brad.speed(5)
##    brad.pensize(4)
##    for i in range(1,37):
##        draw_square(brad) #CALL THE FIRST DEF of drawing the square
##        brad.right(10)#angle 10 degrees to the right
##
##    window.exitonclick() #exit window on click
##
##draw_shape()


##Example - Draw Heart

from turtle import *
def curvemove():
    for i in range(1,200):
        right(1)
        forward(1)
shape('turtle')
color('pink','red')
pensize(10)
speed(5)
##begin_fill()
left(140)
forward(111.65)
curvemove()
left(120)
curvemove()
forward(111.65)
##end_fill()
done()
