import sys

data = open(sys.argv[1]).read().strip()
lines = data.split('\n')

stones = [int(n) for n in lines[0].split()]

for i in range(25):
    new_stones = []
    for j, stone in enumerate(stones):
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            left_half = int(str(stone)[:len(str(stone))//2])
            right_half = int(str(stone)[len(str(stone))//2:])
            new_stones.append(left_half)
            new_stones.append(right_half)
        else:
            new_stones.append(stone*2024)
    stones = new_stones
print(len(stones))

stones = [(int(n), 0) for n in lines[0].split()]
print(stones)
ans = 0
blinks = 75
while len(stones) > 0:
    stone, depth = stones.pop(0)
    assert (depth <= blinks)
    if depth == blinks:
        ans += 1
        continue
    if stone == 0:
        if depth + 4 > blinks:
            stones.append((1, depth+1))
        else:
            new_num = str(2024)
            for n in new_num:
                stones.append((int(n), depth+4))
    elif len(str(stone)) % 2 == 0:
        curcount = 0
        curlen = len(str(stone))
        while curlen % 2 == 0 and curcount+depth < blinks:
            curlen = curlen//2
            curcount += 1
        new_nums_len = len(str(stone))//(2**curcount)
        new_nums = [str(stone)[i:i+new_nums_len] for i in range(0, len(str(stone)), new_nums_len)]
        for new_num in new_nums:
            stones.append((int(new_num), depth+curcount))
    else:
        if (1 <= stone <= 4) and depth <= blinks-3:
            new_num = str(2024*stone)
            assert (len(new_num) == 4)
            for n in new_num:
                stones.append((int(n), depth+3))
        elif stone in [5, 6, 7, 9] and depth <= blinks-5:
            new_num = str(stone*2024*2024)
            assert (len(new_num) == 8)
            for n in new_num:
                stones.append((int(n), depth+5))
        elif stone == 8 and depth <= blinks-5:
            new_stones = [3, 2, 7, 7, 2, 6]
            for n in new_stones:
                stones.append((n, depth+5))
            stones.append((8, depth+4))
        else:
            new_num = str(stone*2024)
            new_depth = depth+1

            stones.append((stone*2024, depth+1))

print(ans)
