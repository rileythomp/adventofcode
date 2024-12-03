import sys 
from itertools import permutations

data = open(sys.argv[1]).read()

lines = data.split("\n")

ingredients = {
    parts[0]: tuple(int(f.split()[-1]) for f in parts[1].split(', '))
    for parts in [line.split(': ') for line in lines]
}

def find_combos(total, n):
    if n == 1:
        return [(total,)] 
    return [(i,) + c for i in range(1, total//2+1) for c in find_combos(total-i, n-1)]

tsp_combos = find_combos(100, len(ingredients))
ingr_perms = list(permutations(ingredients.keys()))
ans = 0
ans2 = 0
for tsp_combo in tsp_combos:
    for ingr_perm in ingr_perms: 
        feats = [0, 0, 0, 0, 0]
        for tsp, ingr in zip(tsp_combo, ingr_perm):
            for i in range(len(feats)):
                feats[i] += tsp * ingredients[ingr][i]
        feats = [max(0, feat) for feat in feats]
        score = 1
        for feat in feats[:-1]: score *= feat
        ans = max(ans, score)
        if feats[-1] == 500:
            ans2 = max(ans2, score)
print(ans)
print(ans2)
