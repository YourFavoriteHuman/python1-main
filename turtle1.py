import turtle
turtle.speed(0)
# helpful info and commands that were going to be used but did not work out
# cube is (size * 2) tall
# cube is (size * 1.70) wide
# size = 50
# color1 =
# color2 =
# color3 =
# setpos()
# int(input("size?: "))
# print(x1)
# setpos(x1,y1)
# setheading(330)
'''
if j == 4:
                setheading(0)
                backward(size * (number_cubes * .60) + 5)
                setpos(xcor(),ycor() + size * 1.5)
            elif j == 7:
                setheading(0)
                backward(size * (number_cubes * .60) + 5)
                setpos(xcor(),ycor() + size * 1.5)
'''


# variables for cube size and height
size = int(input("size? (56 recommended): "))
height = 4 
number_cubes = (4) # this number cannot change (everything depends on this number to be 4)

def next_cube(): # function to move to next cube starting position
    turtle.penup()
    turtle.backward(size)
    turtle.left(60)
    turtle.fd(size)
    turtle.left(60)
    turtle.fd(size)
    turtle.left(30)
    
def move_2_to_1(size): # function to move from line 2 in the cube to line 1, might be  used for other purposes
    turtle.fd(size)
    
def move_2_to_3(size): # function to move from line 2 in the cube to line 3, might be  used for other purposes
    turtle.left(30)
    turtle.fd(size)
    
def move_2_to_4(size): # function to move from line 2 in the cube to line 4, might be  used for other purposes
    turtle.left(60)
    turtle.fd(size)
    
def move_1_to_2(size): # function to move from line 1 in the cube to line 2, might be  used for other purposes
    turtle.right(60)
    turtle.fd(size)
    
def move_3_to_2(size): # function to move from line 3 in the cube to line 2, might be  used for other purposes
    turtle.left(120)
    turtle.fd(size)
    
def right120(size): # function to turn right 120 degrees and the go forward because i needed a function for this
    turtle.right(120)
    turtle.fd(size)
    
def draw_cube(size, color1, color2, color3): # function to create tricolored cube, (took 2 days), it does this using the defined movement commands
   turtle.pendown()
   turtle.begin_fill()
   turtle.color(color2)
   move_2_to_3(size)
   move_2_to_4(size)
   move_3_to_2(size)
   turtle.left(120)
   turtle.end_fill()
   turtle.begin_fill()
   turtle.color(color1)
   move_2_to_1(size)
   right120(size)
   move_1_to_2(size)
   turtle.left(60)
   turtle.penup()
   turtle.fd(-size) 
   turtle.pendown()
   turtle.fd(size)
   turtle.end_fill()
   turtle.begin_fill()
   turtle.color(color3)
   right120(size)
   # these commands were to try and save the turtles position as a variable but it said it wasnt defined ):
   # print(pos())
   # print(pos())
   # x1 = xcor()
   # y1 = ycor()
   # print(x1)
   move_1_to_2(size)
   # heading is 330
   right120(size)
   turtle.end_fill()
   
def move_up_over(number_cubes): # function to move to next row using math that took 30+ minutes to figure out
    turtle.penup()
    turtle.setheading(0)
    if number_cubes == 4:
        turtle.fd((-size * 1.74) * 3.5)
    if number_cubes == 3:
        turtle.fd((-size * 1.74) * 2.5)
    if number_cubes == 2:
        turtle.fd((-size * 1.74) * 1.5)
    turtle.left(90)
    turtle.fd(size * 1.5)
    turtle.right(90)
# j is a counter to count how many cubes there are
j = 0
turtle.penup()
turtle.setpos(-200 + size,-200) # goes to corner of canvas and offsets based on size
turtle.pendown()
for i in range(height):
    for i in range(number_cubes):
        draw_cube(size, "light green", "dark green", "blue")
        next_cube()
        j = j + 1
        if j == number_cubes: # if the cubes reached the required amount, 
            move_up_over(number_cubes)
            number_cubes = number_cubes - 1
            print(number_cubes)
            j = 0 # j was reset to make it equal number_cubes
    turtle.pendown()
# it works!