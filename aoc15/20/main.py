
import sys

data = open(sys.argv[1]).read()
lines = data.split("\n")

def sum_factors(n):
    res = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            res += i
            if i != n // i:
                res += n // i
    return res 

cur = 1
while True:
    if sum_factors(cur) * 10 >= 33100000:
        print(cur)
        break
    cur += 1

def sum_factors2(n):
    first = n//50 + 1
    sqrt = int(n**0.5) + 1
    res = 0
    for i in range(min(first, sqrt), max(first, sqrt)):
        if n % i == 0:
            res += i
            if i != n // i:
                res += n // i
    return res 

cur = 1
while True:
    if sum_factors2(cur) * 11 >= 33100000:
        print('ans', cur)
        break
    cur += 1

