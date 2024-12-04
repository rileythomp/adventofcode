import sys

data = open(sys.argv[1]).read().strip()
lines = data.split('\n')

lengths = [int(n) for n in lines[0].split(',')]

size = 256

nums = [i for i in range(size)]

cur_pos = 0
skip_size = 0
for length in lengths:
    cur_nums = nums[cur_pos:min(cur_pos+length, size)] + nums[0:max(cur_pos+length-size, 0)]
    rev_nums = cur_nums[::-1]
    for i in range(cur_pos, cur_pos+length):
        nums[i % size] = rev_nums[i - cur_pos]
    cur_pos = (cur_pos + length + skip_size) % size
    skip_size += 1

print(nums[0]*nums[1])


lengths = [ord(c) for c in lines[0]] + [17, 31, 73, 47, 23]

size = 256

nums = [i for i in range(size)]

cur_pos = 0
skip_size = 0
for round in range(64):
    for length in lengths:
        cur_nums = nums[cur_pos:min(cur_pos+length, size)] + nums[0:max(cur_pos+length-size, 0)]
        rev_nums = cur_nums[::-1]
        for i in range(cur_pos, cur_pos+length):
            nums[i % size] = rev_nums[i - cur_pos]
        cur_pos = (cur_pos + length + skip_size) % size
        skip_size += 1

dense_hash = []
for i in range(16):
    cur_block = nums[i*16:(i+1)*16]
    dh = 0
    for num in cur_block:
        dh ^= num
    dense_hash.append(dh)

ans = ''
for dh in dense_hash:
    dh_hex = hex(dh)[2:]
    dh_hex = dh_hex if len(dh_hex) == 2 else '0' + dh_hex
    ans += dh_hex

print(ans)
