with open("15.txt","r") as f:
    nums,arr =   [int(i) for i in f.readline().split(",")],[]

i,spoken = 0,0

while True:
    if i < len(nums):
        spoken = nums[i]
    else:
        spoken = arr[0:len(arr)-1][::-1].index(arr[i-1])+1 if arr[i-1] in arr[0:len(arr)-1] else 0
   
    arr.append(spoken)

    i+=1
    if i == 30000000:
        break
        
print(arr[len(arr)-1])



    