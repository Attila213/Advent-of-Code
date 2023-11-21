import re

with open("4.txt","r") as f:
    lines = f.read().split("\n\n")

ids = {
    "byr": r"byr:\s*(19[2-9]\d|200[0-2])\b",
    "iyr": r"iyr:\s*20(1\d|20)\b",
    "eyr": r"eyr:\s*20(2\d|30)\b",
    "hgt": r"hgt:\s*(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)",
    "hcl": r"hcl:\s*#[0-9a-f]{6}\b",
    "ecl": r"ecl:\s*(amb|blu|brn|gry|grn|hzl|oth)\b",
    "pid": r"pid:\s*\d{9}\b",
}

part1 = sum([all(id in line for id in ids) for line in lines])

part2 = sum([all(re.search(ids[id],line) for id in ids ) for line in lines])
print(part1)
print(part2)
