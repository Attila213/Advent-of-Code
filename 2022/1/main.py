with open("1.txt","r") as f:
    calories = [[int(x) for x in i.split("\n")] for i in f.read().split("\n\n")]
all = sorted([sum(i) for i in calories],reverse=True)
print("part 1:",all[0]);
print("part 2:",sum([cal for i,cal in enumerate(all) if i < 3]))