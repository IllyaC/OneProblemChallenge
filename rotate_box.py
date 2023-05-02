"""
You are given an m x n matrix of characters box representing a 
side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the 
stones to fall due to gravity. Each stone falls down until it l
ands on an obstacle, another stone, or the bottom of the box. 
Gravity does not affect the obstacles' positions, and the inertia 
from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another 
stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described 
above.
"""

def rotateTheBox(box):
    for i in range(len(box)):
            stone = 0
            for j in range(len(box[0])):
                if box[i][j] == '#':
                    stone += 1
                    box[i][j] = '.'
                elif box[i][j] == '*':
                    for m in range(stone):
                        box[i][j-m-1] = '#'
                    stone = 0
            if stone != 0:
                for m in range(stone):
                        box[i][j-m] = '#'
    rotated_box = [[None]*len(box) for i in range(len(box[0]))]
    for row in range (len(box)):
        for column in range (len(box[0])):
            rotated_box[column][len(box)-row-1] = box[row][column]
    return(rotated_box)
    
    
box = [["#",".","*","."],
              ["#","#","*","."]]
print(rotateTheBox(box))

    