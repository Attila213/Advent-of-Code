matrix = []
with open("11.txt") as f:
    matrix = [i.strip() for i in f.readlines()]



def count_adjacents(i,j):
    counter = 0
    for col in range(3):
        for row in range(3):
            index =(i-1)+col
            jndex = (j-1)+row
            if 0 <= index <=len(matrix)-1 and 0 <= jndex <=len(matrix[0])-1 and [index,jndex] != [i,j] and matrix[index][jndex] == '#':
                counter +=1
    return counter

def update_results(results,i,switchto):
    temp_results = []
    
    for c in range(len(results)):
        if c == i and results[i] == "x":
            temp_results.append(switchto)
        elif results[c] == "L" or results[c] == "#" or results[c] == "o":
            temp_results.append(results[c])
        else:
            temp_results.append("x")
    return temp_results

def count_in_directions(i,j):
    # egyre nagyobb körben nézze és ami talál ABBAN AZ IRÁNYBAN először ott a tömbben módosítson egy értéket. 
    # Ugyanúgy megy tovább de ha egyszer már true vagy false akkor nem módosul. Ezekez számoljuk ha már mind bool
    circle_range =1
    results = ["x" for i in range(8)]
    while True:
        apparent = [
            [i+circle_range,j+circle_range],
                    [i-circle_range,j+circle_range],
                    [i+circle_range,j-circle_range],
                    [i-circle_range,j-circle_range],
                    [i,j+circle_range],
                    [i,j-circle_range],
                    [i+circle_range,j],
                    [i-circle_range,j]
                    ]
        
        for r in range(len(apparent)):
            if not (apparent[r][0] > len(matrix)-1 or apparent[r][0] < 0 or apparent[r][1] < 0 or apparent[r][1] > len(matrix[0])-1):
                if matrix[apparent[r][0]][apparent[r][1]] == "L" :
                    results = update_results(results,r,"L")
                if matrix[apparent[r][0]][apparent[r][1]] == "#" :
                    results = update_results(results,r,"#")
            else:
                results = update_results(results,r,"o")
        circle_range +=1
        
        
        if sum([x == "x" for x in results]) ==0:
            return sum([x == "L" for x in results])
        
            
# # part1
while True:
    arr = []
    changed = False
    for i in range(len(matrix)):
        newstr=""
        for j in range(len(matrix[i])):
            if matrix[i][j] == "L" and count_in_directions(i,j) >= 5:
                newstr +="#"
                changed = True
            elif matrix[i][j] == "#" and count_in_directions(i,j) == 0:
                newstr +="L"
                changed = True
            else:
                newstr += matrix[i][j]
        arr.append(newstr)
    if changed:
        matrix = arr
    else:
        break

print(sum([i.count("L") for i in matrix]))


