#part1
nums = []
with open("1.txt", "r") as f:
    for i in f.readlines():
        nums.append(int(i[:len(i)-1]))
    

szam = 0
for i in nums:
    if 2020 - i in nums:
        szam = i*(2020-i)
        break
    
print(szam)

#----------part2
nums = []
with open("1.txt", "r") as f:
    for i in f.readlines():
        nums.append(int(i[:len(i)-1]))


def find2020():
    for i in nums:
        for j in nums:
            if 2020-i-j in nums:
                return(i*j*(2020-i-j))

    
print(find2020())