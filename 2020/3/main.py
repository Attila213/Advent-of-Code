import math

lines = []
tests = [[1,1], [3,1], [5,1], [7,1], [1,2]]

with open("3.txt") as f:
    for i in f.readlines():
        lines.append(i.strip())



def countTrees(right,down):
    counter = 0
    col = 0
    
    for i in range(0,len(lines),down):
        if lines[i][col] == "#":
            counter += 1
        col = (col+right)%len(lines[i])

    return counter
        


print(math.prod([countTrees(pos[0],pos[1]) for pos in tests]))

