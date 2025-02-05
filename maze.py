row0 = ['#','#','#','#','#','#','#','#','#','#']
def row01():
    for item in row0:
        print(item, end = " ")

def row02():
    row0[3:5] = " "
    for item in row0:
        print(item, end = " ")
row = 0
col = 0
dir = "→"

mouse = [row,col,dir]

maze = [row][col]

exit = [row,col,dir]

row02()

"↓, ←, →, ↑"

