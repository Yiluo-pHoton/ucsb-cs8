# lab05.py Yiluo Li
import turtle
from math import *
import random

#######################################################################################################
##############                               Initiate                                 #################
#######################################################################################################

if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(0)
    s = t.getscreen()

#######################################################################################################
##############                       Fundmental Draw Functions                         ################
#######################################################################################################
    
def drawRectangle(width, height, tilt, penColor, fillColor):
    """
    draw rectangle. given width, height, penColor, and fillColor
    current location: lower left corner
    bottom side tilted by and angle, tilt in degrees
    relative to horizontal axis
    """
    x_start = t.xcor()
    y_start = t.ycor()
    cos_tilt = cos(radians(tilt))
    sin_tilt = sin(radians(tilt))
    x_right_bottom = x_start + cos_tilt * width
    y_right_bottom = y_start + sin_tilt * width
    x_right_top = x_right_bottom - sin_tilt * height
    y_right_top = y_right_bottom + cos_tilt * height
    x_left_top = x_start - sin_tilt * height
    y_left_top = y_start + cos_tilt * height

    t.down()
    t.pen(fillcolor=fillColor, pencolor=penColor, pensize=5)
    t.begin_fill()
    t.goto(x_right_bottom, y_right_bottom)
    t.goto(x_right_top, y_right_top)
    t.goto(x_left_top, y_left_top)
    t.goto(x_start, y_start)
    t.end_fill()
    t.up()

def drawTriangle(base, height, tilt, penColor, fillColor):
    """
    draw triangle. given base, height, penColor, and fillColor 
    current location: lower left corner
    bottom side tilted by and angle, tilt in degrees
    relative to horizontal axis
    """
    x_start = t.xcor() 
    y_start = t.ycor()
    x_top = x_start + cos(radians(tilt)) * base / 2 - sin(radians(tilt)) * height
    y_top = y_start + sin(radians(tilt)) * base / 2 + cos(radians(tilt)) * height
    x_right = x_start + cos(radians(tilt)) * base
    y_right = y_start + sin(radians(tilt)) * base
    
    t.down()
    t.pen(fillcolor=fillColor, pencolor=penColor, pensize=4)
    t.begin_fill()
    t.goto(x_top, y_top)
    t.goto(x_right, y_right)
    t.goto(x_start, y_start)
    t.end_fill()

#######################################################################################################
##############                        Draw Inidividual Object                          ################
#######################################################################################################
    
def drawTree(height, color):
    """
    This function draws a tree with a specific height and color
    with the bottom of the current location of the turtle
    The bark of the tree is always brown
    """
    x_start = t.xcor()
    y_start = t.ycor()
    rec_height = height / 4
    rec_width = height / 20
    tri_base = height / 2
    tri_height = height / 3
    tri_base_diff = (height - rec_height - tri_height) / 2
    tri_x_start = x_start - tri_base / 2 + rec_width / 2
    tri_y_start = y_start + rec_height
    
    drawRectangle(rec_width, rec_height, 0, "brown", "brown")
    t.goto(tri_x_start, tri_y_start)

    for i in range(3):
        drawTriangle(tri_base, tri_height, 0, color, color)
        t.up()
        t.goto(tri_x_start, t.ycor() + tri_base_diff)

def drawHut():
    '''
    Draw a brown hut of fixed dimensions purely composed of rectangles
    Use the random module to enhance your drawing by introducing irregularities in a controlled way
    '''
    x_start = t.xcor()
    y_start = t.ycor()
    plank_number = 10 + random.randint(-2, 2)
    plank_width = 10
    plank_height = 60
    shades_of_brown = ["#653221", "#653821", "#653d21", "#653d21", "#654321", "#654321"]
    shades_of_black = ["#000000", "#111111", "#151515", "#222222", "#151515", "#222222"]

    for i in range(1, plank_number + 1):
        t.down()
        drawRectangle(plank_width + random.randint(-2, 2), plank_height + random.randint(-5, 5),
                      random.randint(-5, 5), random.choice(shades_of_black), random.choice(shades_of_brown))
        t.up()
        t.goto(x_start + i * (plank_width) + random.randint(-1,1), y_start + random.randint(-5, 5))

    plank_width = 15
    plank_height = 80
    t.goto(x_start + plank_width * plank_number / 2.8, y_start + plank_height * 1.5 + random.randint(-5, 5))
    roof_plank_number = random.randint(15, 25)
    for i in range(roof_plank_number):
        t.down()
        tilt = 120 + i * 150 / roof_plank_number + random.randint(-5, 5) 
        drawRectangle(plank_width + random.randint(-2, 2), plank_height + random.randint(-5, 5),
                      tilt, random.choice(shades_of_black), random.choice(shades_of_brown))
        t.up()
        t.goto(x_start + plank_width * plank_number / 2.8, y_start + plank_height * 1.5 + random.randint(-5, 5))

#######################################################################################################
##############                         Draw Multiple Objects                           ################
#######################################################################################################

def drawForest(tree_num):
    '''
    draws a collection of trees placed at random locations within a rectangular region
    '''
    tree_x_diff = s.screensize()[0] / (tree_num / 2)
    screen_left = -s.screensize()[0]
    x_start = screen_left
    y_start = 0
    shades_of_green =["#006400", "#556b2f", "#8fbc8f", "#2e8b57", "#3cb371", "#20b2aa", "#32cd32"]

    t.up()
    t.goto(x_start, y_start)
    t.down()
    
    for i in range(1, tree_num + 1):
        t.down()
        drawTree(random.randint(150, 250), random.choice(shades_of_green))
        t.up()
        t.goto(x_start + i * tree_x_diff + random.randint(10, 40), y_start + random.randint(-100, 100))

def drawVillage():
    '''
    Draw a sequence of five huts, plzed randomly among a horizontal line
    '''
    x_start = -s.screensize()[1] - 10 * 10
    y_start = -s.screensize()[0] / 2
    hut_x_diff = s.screensize()[1] / 2
    
    t.up()
    t.goto(x_start, y_start)
    t.down()
    
    for i in range(1, 6):
        t.down()
        drawHut()
        t.up()
        t.goto(x_start + i * hut_x_diff + random.randint(-10, 10), -hut_x_diff + random.randint(-20, 20))
        
def randomPlay():
    '''
    Experiments with the random module
    '''
    t.pensize(10)
    shades_of_green =["#006400", "#556b2f", "#8fbc8f", "#2e8b57", "#3cb371", "#20b2aa", "#32cd32"]
    
    for i in range(36):
        t.up()
        radius = 200 + random.randint(-50, 50)
        x = radius * cos(i * 10 * pi / 180)
        y = radius * sin(i * 10 * pi / 180)
        tilt = 0
        color = random.choice(shades_of_green)
        
        t.goto(x, y)
        t.down()
        drawTriangle(50, 50, tilt, "black", color)

#######################################################################################################
##############                          Test Drawing Objects                          #################
#######################################################################################################
        
def testdrawTree():
    t.up()
    t.goto(0, -100)
    t.down()
    drawRectangle(200, 200, 0, "red", "")
    drawTree(200, "green")

def testRectangle():
    drawRectangle(50, 100, 0, "red", "")
    t.seth(0)
    t.up()
    t.forward(200)
    t.down()

    drawRectangle(50, 100, 20, "green", "yellow")
    t.seth(0)
    t.up()
    t.forward(200)
    t.down()

#######################################################################################################
##############                    Main Draw Village and Forest                        #################
#######################################################################################################
    
if __name__ == "__main__":
    drawForest(random.randint(15, 20))
    drawVillage()
