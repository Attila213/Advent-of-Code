def get_num(char):
    return 97-ord(char)

with open("6.txt","r") as f:    
    answers = [answ for answ in f.read().split("\n\n")]
    
count_answers = sum([len(set(i.replace("\n",""))) for i in answers]) 
print(count_answers)

#-----------------------------------------------------------------------
with open("6.txt","r") as f:
    answers= [answ.split("\n") for answ in f.read().split("\n\n")]

count_answers = 0
for i in answers:
    letters = set()
    for j in i:
        letters.update(j)
    count_answers += len(letters)

#-----------------------------------------------------------------------

print(count_answers)
part2 = sum([len(set.intersection(*map(set,i))) for i in answers])

print(part2)




