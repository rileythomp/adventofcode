import sys 
from itertools import permutations

data = open(sys.argv[1]).read()

lines = data.split("\n")

reading = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

ans, ans2 = 0, 0
for i, line in enumerate(lines):
    parts = line.split(": ", 1)
    feats = parts[1].split(", ")
    broke1, broke2 = False, False
    for feat in feats:
        feat_parts = feat.split(": ")
        feat_name = feat_parts[0]
        feat_val = int(feat_parts[1])
        reading_val = reading[feat_name]
        if feat_name in reading:
            if reading_val != feat_val:
                broke1 = True
            if feat_name == 'cats' or feat_name == 'trees':
                if reading_val >= feat_val: broke2 = True
            elif feat_name == 'pomeranians' or feat_name == 'goldfish':
                if reading_val <= feat_val: broke2 = True
            elif reading_val != feat_val: broke2 = True
    if not broke1: ans = i + 1
    if not broke2: ans2 = i + 1

print(ans)
print(ans2)