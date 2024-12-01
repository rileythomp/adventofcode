import sys

data = open(sys.argv[1]).read().strip()
lines = data.split('\n')

lefts, rights = [], []
for line in lines:
    left, right = line.split('   ')
    lefts.append(int(left))
    rights.append(int(right))

sorted_lefts = sorted(lefts)
sorted_rights = sorted(rights)

print(sum(abs(sl - sr) for sl, sr in zip(sorted_lefts, sorted_rights)))
print(sum(sl * sorted_rights.count(sl) for sl in sorted_lefts))
