import re
import sys

data = open(sys.argv[1]).read().strip()

ans, ans2 = 0, 0
for line in [data]:
    mults = re.finditer('mul\((\d+),(\d+)\)', line)
    dos = list(re.finditer('do\(\)', line))
    donts = list(re.finditer('don\'t\(\)', line))
    for mult in mults:
        do_idx = ([0]+[do.start() for do in dos if do.start() < mult.start()])[-1]
        dont_idx = ([0]+[dont.start() for dont in donts if dont.start() < mult.start()])[-1]
        if do_idx >= dont_idx:
            ans2 += int(mult.group(1)) * int(mult.group(2))
        ans += int(mult.group(1)) * int(mult.group(2))

print(ans)
print(ans2)
