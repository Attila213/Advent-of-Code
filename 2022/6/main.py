with open("6.txt","r") as f:
    sign = [i for i in f.read()]

size = 14
print([i+size for i in range(len(sign)-5) if len(set(sign[i:i+size])) ==size][0])
        