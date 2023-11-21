lines =[]
with open('7t.txt') as fp:
    for line in fp:
        lines.append(line.strip())

bags = {}

for i in lines:
    splitted = i.split()
    
    bags[splitted[:2][0]+" "+splitted[:2][1]] = {}
    for j in range(len(splitted)):
        if (splitted[j] == "contain" or "," in splitted[j]) and splitted[j+1] != "no":
            parts = splitted[j+1:j+4:1]
            bags[splitted[:2][0]+" "+splitted[:2][1]][parts[1]+" "+parts[2]] = parts[0]

#megszámolni hogy hány db zsák tartalmazza a shiny goldot
print(bags)