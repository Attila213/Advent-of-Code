with open("4.txt") as f:
    ids =  [[i.strip().split(',')[0].split("-"),i.strip().split(',')[1].split("-")] for i in f.readlines()]

print("part1:",len([i for i in ids if [str(min(int(i[0][0]),int(i[1][0]))),str(max(int(i[0][1]),int(i[1][1])))] in i ]))

print("part1:",len([i for i in ids if len(list(filter(lambda a: a in [j for j in range(int(i[0][0]),int(i[0][1])+1)], [j for j in range(int(i[1][0]),int(i[1][1])+1)]))) > 0 ]))
