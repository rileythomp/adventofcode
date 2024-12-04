import sys 
import re

print(sum([sum([int(n) for n in re.findall(r'-?\d+', line)]) for line in open(sys.argv[1]).read().split("\n")]))
