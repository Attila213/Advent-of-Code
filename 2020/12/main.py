import math

with open("12.txt") as f:
    commands = [i.strip() for i in f]


degree = 0
curr_direction = "E"

directions ={"E":{"degree":0,"value":0},"W":{"degree":180,"value":0},"S":{"degree":90,"value":0},"N":{"degree":270,"value":0}}

for i in commands:
    d = i[0]
    num = int(i[1:])
    
    if d =="R" or d=="L":
        if d=="R":
            degree += num
        if d=="L":
            degree -= num
        
        degree %= 360
        
        for i in directions:
            if directions[i]["degree"] == degree:
                curr_direction = i
            
    for j in directions:
        if j == d:
            directions[j]["value"] += num
    
    if d=="F":
        for j in directions:
            if j == curr_direction:
                directions[j]["value"] = directions[j]["value"]+num

ew = directions["E"]["value"]-directions["W"]["value"] if directions["E"]["value"]>directions["W"]["value"] else directions["W"]["value"]-directions["E"]["value"]
sn = directions["S"]["value"]-directions["N"]["value"] if directions["S"]["value"]>directions["N"]["value"] else directions["N"]["value"]-directions["S"]["value"]

print(ew+sn)