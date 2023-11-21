def convertToRPS(string):
    return string.replace("A","R_1").replace("B","P_2").replace("C","S_3").replace("X","R_1").replace("Y","P_2").replace("Z","S_3")

def sumByRule(array):
    return sum([int(i[1].split("_")[1])+6 if ("R" in i[1] and "S" in i[0]) or ("S" in i[1] and "P" in i[0]) or ("P" in i[1] and "R" in i[0]) else (int(i[0].split("_")[1])+3 if i[1]==i[0] else int(i[1].split("_")[1])) for i in array])

def LOSE(char):
    if "R" in char:
        return "S_3"
    if "S" in char:
        return "P_2"
    if "P" in char:
        return "R_1"
    
def WIN(char):
    if "R" in char:
        return "P_2"
    if "S" in char:
        return "R_1"
    if "P" in char:
        return "S_3"

with open("2.txt","r") as f:
    base =[i.split() for i in f.readlines()]
    
game = [[convertToRPS(i[0]),convertToRPS(i[1])] for i in base]

print("Part 1:",sumByRule(game))
print("Part 2:",sumByRule([[game[i][0],game[i][0] if base[i][1] == "Y" else (LOSE(game[i][0][0]) if base[i][1] == "X" else WIN(game[i][0][0]))] for i in range(len(game))]))

