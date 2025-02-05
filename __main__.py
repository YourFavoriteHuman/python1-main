# *****************************************************************
# Maze Solver Project
# Starter Code supplied by Mr. Fuller on 11/21/2024
# Name: Jaynan Carrasquillo
# Date: December 11, 2024
# *****************************************************************


# *****************************************************************
# Required Import Statements
# *****************************************************************
from os import system, name
from time import sleep

mouse = [2, 0, 1]
# Mouse variable contains [row, column, direction]
# Valid directions: 1-East 2-South 3-West 4-North
maze = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['M', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#'],
        ['#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#', ' ', ' '],
        ['#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
        ['#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
exit = [4, 11]
# *****************************************************************
# Functions Section (Alphabetical Order)
# *****************************************************************
# Description: Clear the terminal window for different operating
# systems.
def clear_screen():
    # For Microsoft Windows
    if name == 'nt':
        _ = system('cls')
    
    # For Mac and Linux (here, os.name is 'posix')
    else:
        _ = system('clear')



# Description: Loads data from a text file and gives back
# maze, mouse, and exit locations
# Returns a list of lists
def load_data():
    # Teacher will provide a function later to load
    # other mazes and starting conditions 
    pass



# Description: Displays the maze on the terminal window
def print_maze(maze):
    # Use nested loops to print maze 
    for row in maze:    
        for each_item in row:
            print(each_item, end = " ")
        print()


# Description: Displays the maze on the terminal window
def turn_right(mouse):
    mRow, mCol, mDir = mouse

    mDir += 1

    if mDir == 5:
        mDir = 1

    mouse[0], mouse[1], mouse[2] = mRow, mCol, mDir
    # print(mouse[2])

def turn_left(mouse):
    mRow, mCol, mDir = mouse

    mDir -= 1

    if mDir == 0:
        mDir = 4

    mouse[0], mouse[1], mouse[2] = mRow, mCol, mDir
    # print(mouse[2])

def ishashbottom():
    mouse[0] = int(mouse[0]) + 1
    if "#" == maze[mouse[0]][mouse[1]]:
        mouse[0] = int(mouse[0]) - 1
        return True
    elif " " == maze[mouse[0]][mouse[1]]:
        mouse[0] = int(mouse[0]) - 1
        return False

def ishashright():
    mouse[1] = int(mouse[1]) + 1
    if "#" == maze[mouse[0]][mouse[1]]:
        mouse[1] = int(mouse[1]) - 1
        return True
    elif " " == maze[mouse[0]][mouse[1]]:
        mouse[1] = int(mouse[1]) - 1
        return False

def ishashtop():
    mouse[0] = int(mouse[0]) - 1
    if "#" == maze[mouse[0]][mouse[1]]:
        mouse[0] = int(mouse[0]) + 1
        return True
    elif " " == maze[mouse[0]][mouse[1]]:
        mouse[0] = int(mouse[0]) + 1
        return False

def ishashleft():
    mouse[1] = int(mouse[1]) - 1
    if "#" == maze[mouse[0]][mouse[1]]:
        mouse[1] = int(mouse[1]) + 1
        return True
    elif " " == maze[mouse[0]][mouse[1]]:
        mouse[1] = int(mouse[1]) + 1
        return False

def moveright():
    maze[mouse[0]][mouse[1]] = " "
    mouse[1] = int(mouse[1]) + 1
    maze[mouse[0]][mouse[1]] = "M"
    # input()
    sleep(0.1)
    clear_screen()
    print_maze(maze)

def moveleft():
    maze[mouse[0]][mouse[1]] = " "
    mouse[1] = int(mouse[1]) - 1
    maze[mouse[0]][mouse[1]] = "M"
    # input()
    sleep(0.1)
    clear_screen()
    print_maze(maze)

def moveup():
    maze[mouse[0]][mouse[1]] = " "
    mouse[0] = int(mouse[0]) - 1
    maze[mouse[0]][mouse[1]] = "M"
    # input()
    sleep(0.1)
    clear_screen()
    print_maze(maze)

def movedown():
    maze[mouse[0]][mouse[1]] = " "
    mouse[0] = int(mouse[0]) + 1
    maze[mouse[0]][mouse[1]] = "M"
    # input()
    sleep(0.1)
    clear_screen()
    print_maze(maze)

# Description: The function that starts the program
def main():
    # Variables local to the main() function
    # Will be passed to other functions
    # List data types are mutatable

    print_maze(maze)

    while mouse[0:2] != exit:
        if mouse[2] == 1: # east
            if ishashbottom() == True and ishashright() == False:
                moveright()
            elif ishashbottom() == False and ishashright() == True:
                turn_right(mouse)
            elif ishashbottom() == True and ishashright() == True:
                turn_left(mouse)
            elif ishashbottom() == False and ishashright() == False:
                moveright()
        elif mouse[2] == 2: # south
            if ishashright() == False:
                turn_left(mouse)
            elif ishashbottom() == False and ishashleft() == True:
                movedown()
            elif ishashbottom() == True and ishashleft() == False:
                turn_right(mouse)
            elif ishashbottom() == True and ishashleft() == True:
                turn_left(mouse)
            elif ishashbottom() == False and ishashleft() == False:
                movedown()
        elif mouse[2] == 3: # west
            if ishashtop() == True and ishashleft() == False:
                moveleft()
            elif ishashtop() == False and ishashleft() == True:
                turn_right(mouse)
            elif ishashtop() == True and ishashleft() == True:
                turn_left(mouse)
            elif ishashtop() == False and ishashleft() == False:
                moveleft()
        elif mouse[2] == 4: # north
            if ishashtop() == False and ishashright() == True:
                moveup()
            elif ishashtop() == True and ishashright() == False:
                turn_right(mouse)
            elif ishashtop() == True and ishashright() == True:
                turn_left(mouse)
            elif ishashtop() == False and ishashright() == False:
                moveup()




    """


    def move(): # while the mouse is not at the end, if it is facing east, if mouse y + 1 = # in the maze
        while mouse[0:2] != exit:
            ishashleft()
            ishashbottom()
            ishashright()
            ishashtop()
            if (ishashright() and (ishashtop() or ishashbottom())) == False:
                print("right", ishashright())
                if ishashright() == False:
                    moveright()
            elif (ishashbottom() and (ishashright() or ishashleft())) == False:
                print("bottom", ishashbottom())
                if ishashbottom() == False:
                    movedown()
            elif (ishashtop() and (ishashright() or ishashleft())) == False:
                print("top", ishashtop())
                if ishashtop() == False:
                    moveup()
            elif (ishashleft() and (ishashtop() or ishashbottom())) == False:
                print("left", ishashleft())
                if ishashleft() == False:
                    moveleft()
                

    """
    
           

# Uncomment when teacher has given load_data() code
# mouse, exit, maze = load_data()
# Until then, just use the 3 variables defined above
    
    """
    print_maze(maze)
    if mouse == [1, 3, 1]:
        print((ishashright() and ((ishashtop() and ishashbottom()) == False)) == False) # False
    print(mouse[0:2] != exit)
    move()

    """

# Runs the main() function if the file containing this code
# is directly executed by the Python interpreter.
if __name__ == "__main__":
    main()