import math
from functools import reduce


with open("13.txt") as f:
    start = int(f.readline())
    buses = f.readline().strip().split(',')
 


numbers = [int(i) for i in buses if i != 'x']
print(numbers)

ID = 0
wait_time = 1000000000
for i in numbers:
    if wait_time > (((start//i)+1)*i)%start:
        wait_time = (((start//i)+1)*i)%start
        ID = i

print(wait_time)

#egy függvény ami meghatároz egy számot egy számok alapján amiknek van (mod x)-e
def chinese_remainder(m, a):
    sum = 0
    prod = reduce(lambda acc, b: acc*b, m)
    for n_i, a_i in zip(m, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


offsets = [int(b) - i for i,b in enumerate(buses) if b != 'x']

print(chinese_remainder(numbers,offsets))
