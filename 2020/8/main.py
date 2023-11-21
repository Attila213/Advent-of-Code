commands = []

with open('8.txt') as fp:
    for line in fp:
        commands.append(line.strip())

value =0
i = 0

tried =[]
currentnope = None
currentnope_command = None

alreadyrunned = []

while i != len(commands):
    
    parts = commands[i].split()
    command = parts[0]
    operator = parts[1][0]
    number = parts[1][1:]
    
    #itt próbáld meg
    if command == "jmp" and i in alreadyrunned and i not in tried:
        if currentnope != None:
            commands[currentnope] = currentnope_command
        currentnope = i
        currentnope_command = commands[i]
        commands[i] = "nop "+str(operator)+str(number)
        
        tried.append(i)
        value =0
        i=0
        alreadyrunned.clear()
        continue
    
        
    if command == "jmp":
        alreadyrunned.append(i)
        i = eval(f'{i} {operator} {number}')

    if command == "acc":
        value = eval(f'{value} {operator} {number}')
        i+=1
    if command == "nop":
        i+=1
    

print(value)
    