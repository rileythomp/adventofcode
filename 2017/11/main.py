import sys
from collections import Counter, defaultdict

data = open(sys.argv[1]).read().strip()
lines = data.split('\n')

moves = lines[0].split(',')
