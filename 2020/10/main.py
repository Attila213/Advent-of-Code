import math,itertools

with open("10.txt","r") as f:
    jolts = [int(i.strip()) for i in f.readlines()]

jolts.append(0)
jolts.append(max(jolts)+3)

diff = [sorted(jolts)[i+1]-sorted(jolts)[i] for i in range(len(jolts)-1)]

print(diff.count(1)*diff.count(3))

sorted = sorted(jolts)

# megnézzük hogy mik kellenek feltétlenül
needit= []
i = 0
while sorted[i] != max(sorted):
    for j in range(3,0,-1):
        if sorted[i]+j in sorted:
            needit.append(sorted[i]+j)
            sorted[i] += j
            break

valami = list(set(sorted)-set(needit))




