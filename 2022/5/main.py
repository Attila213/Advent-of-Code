with open("5.txt")as f:
    array = [i.split("\n") for i in f.read().split("\n\n")]
listarray =[list() for i in range(len(array[0]))]

[listarray[j].append(e2) for i,e1 in enumerate([i.replace("    ","-").replace(" ","").replace("[","").replace("]","").replace("][","").strip() for i in array[0][::-1] if '1' not in i]) for j,e2 in enumerate(e1) if e2 != "-"]
    
chars = None
for i in array[1]:
    arr = [int(j) for j in i.split() if j in [str(k) for k in range(100)]]
    
    if len(arr)>0:
        #part 1 with uncommented [::-1]
        #part 2 this
        chars = listarray[arr[1]-1][len(listarray[arr[1]-1])-arr[0]:len(listarray[arr[1]-1])]#[::-1]
        
        [listarray[arr[1]-1].pop() for i in range(arr[0])]
        listarray[arr[2]-1].extend(chars)
    
    
print("".join(i[len(i)-1] for i in listarray if len(i) >0))

