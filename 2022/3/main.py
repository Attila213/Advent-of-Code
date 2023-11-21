with open("3.txt") as f:
    rucksacks = [i.strip() for i in f.readlines()]
    
def letterToAscii(letter):
    return ord(letter)-96 if not letter.isupper() else ord(letter)-38

print("part1: ",sum(letterToAscii(i) for i in [list(set(i[0:len(i)//2]).intersection(set(i[len(i)//2:len(i)])))[0] for i in rucksacks]))
print("part2: ",(sum([letterToAscii(list((i[0].intersection(i[1])).intersection(i[2]))[0]) for i in [[set(j) for j in rucksacks[i*3:(i*3)+3]] for i in range((len(rucksacks)//3))]])))
    




