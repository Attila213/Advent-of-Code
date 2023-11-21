import sys
with open("9.txt","r")as f:
    nums= [int(i.strip()) for i in f]

prev = 25
part1 = 0
for i in range(len(nums)):
    if i >= prev:
        found = False
        for j in nums[i-prev:i]:
            if nums[i]-j in nums[i-prev:i]:
                found = True
                break
        if not found:
            part1 = nums[i]
            break


print(part1)

part2 = 0
for i in range(len(nums)):
    found = False
    for j in range(i,len(nums)):
        if sum(nums[i:j]) > part1:
            if sum(nums[i:j-1]) < part1:
                break
            else:
                print(max(nums[i:j-1])+min(nums[i:j-1]))
                break

