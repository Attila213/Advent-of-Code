parts = []
with open("14.txt","r") as f:
    parts = [i.strip() for i in f.readlines()]


numbers = {}
for i in parts:
    if "mask" in i:
        mask = i.split()[2]
    else:
        index,num = [int(i[i.index("[")+1:i.index("]")]), int(i.split()[2])]
    
        if mask != "":
            binarynum = "0"*(len(mask)-len(bin(num).replace("0b","")))+bin(num).replace("0b","")
            num = ""
            for i in range(len(binarynum)):
                num += binarynum[i] if mask[i] == "X" else mask[i]
            numbers[str(index)] = int(num,2)

sum = sum(i[1] for i in numbers.items())
print(sum)
