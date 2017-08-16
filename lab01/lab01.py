import turtle

t = turtle.Turtle()

def draw_y(height, width):
    start_x = t.xcor()
    start_y = t.ycor()
    mid_x = start_x + width / 2
    right_x = start_x + width
    top_y = start_y + height
    mid_y = start_y + height / 2
    
    t.up()
    t.goto(start_x, top_y)
    t.down()
    t.goto(mid_x, mid_y)
    t.goto(right_x, top_y)
    
    t.up()
    t.goto(mid_x, mid_y)
    t.down()
    t.goto(mid_x, start_y)

def draw_l(height, width):
    start_x = t.xcor()
    start_y = t.ycor()
    top_y = start_y + height
    right_x = start_x + width
    
    t.up()
    t.goto(start_x, top_y)
    t.down()
    t.goto(start_x, start_y)
    t.goto(right_x, start_y)

def draw_2(height, width):
    start_x = t.xcor()
    start_y = t.ycor()
    top_y = start_y + height
    mid_y = start_y + height / 2
    right_x = start_x + width
    
    t.up()
    t.goto(start_x, top_y)
    t.down()
    t.goto(right_x, top_y)
    t.goto(right_x, mid_y)
    t.goto(start_x, mid_y)
    t.goto(start_x, start_y)
    t.goto(right_x, start_y)
 
def draw_0(height, width):
    start_x = t.xcor()
    start_y = t.ycor()
    top_y = start_y + height
    right_x = start_x + width

    t.down()
    t.goto(start_x, top_y)
    t.goto(right_x, top_y)
    t.goto(right_x, start_y)
    t.goto(start_x, start_y)

def draw_1(height, width):
    start_x = t.xcor()
    start_y = t.ycor()
    mid_x = start_x + width / 2
    top_y = start_y + height

    t.up()
    t.goto(mid_x, start_y)
    t.down()
    t.goto(mid_x, top_y)

def draw_lab01(height, width, init_x, init_y):
    myString = "yl2021"
    for i in range(1, 7):
        eval("draw_" + myString[i-1:i] + "(height, width)")
        t.up()
        t.goto(init_x + (width +10) * i, init_y)

while True:
    height = int(input("Please input height for a character: "))
    width = int(input("Please input width for a character: "))
    init_x = int(input("Please input initial x-coordinate: "))
    init_y = int(input("Please input initial y-coordinate: "))
    draw_lab01(height, width, init_x, init_y)
