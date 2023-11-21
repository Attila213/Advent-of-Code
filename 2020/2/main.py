count = 0
count2 = 0
passwords =[]
with open('2.txt') as fp:
    for line in fp:
        passwords.append(line.strip())

for i in passwords:  
    parts = i.split()
    min,max = int(parts[0].split("-")[0]),int(parts[0].split("-")[1])
    letter = parts[1][0]
    password = parts[2]
    
    if password.count(letter) in range(min, max+1):
        count+=1
    
    if len(password) > max-1:
        if [password[min-1],password[max-1]].count(letter) == 1:
            count2+=1

print("part 1:",count)
print("part 2:",count2)