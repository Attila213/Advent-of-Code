lines = set()

with open("5.txt","r") as f:
    lines = f.read().strip().replace("B","1").replace("R","1").replace("L","0").replace("F","0").split("\n")

claimed = set()

max_id = 0
for line in lines:
    row = int(line[:7],2)
    col = int(line[7:],2)
    
    id_template = (row*8)+col
    
    claimed.add(id_template)
    
    if id_template > max_id:
        max_id = id_template
        

all_seats = set(range(128*8))

open_seats = all_seats-claimed

my_seat = [seat for seat in open_seats if seat+1 not in open_seats and seat-1 not in open_seats]

print(my_seat[0])
