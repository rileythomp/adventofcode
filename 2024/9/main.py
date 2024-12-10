import sys

data = open(sys.argv[1]).read().strip()
lines = data.split('\n')
disk_map = [int(n) for n in lines[0]]


def checksum(disk):
    return sum([i*val for i, val in enumerate(disk) if val >= 0])


disk = []
cur = 0
is_file = True
files, frees = [], []
files2, frees2 = [], []
for length in disk_map:
    if is_file:
        files.extend(i for i in range(len(disk), len(disk)+length))
        files2.append((len(disk), length))
        disk.extend([cur] * length)
        cur += 1
    else:
        frees.extend(i for i in range(len(disk), len(disk)+length))
        frees2.append((len(disk), length))
        disk.extend([-1] * length)
    is_file = not is_file

disk2 = disk[::]

while frees[0] <= files[-1]:
    file_idx, free_idx = files[-1], frees[0]
    disk[file_idx], disk[free_idx] = disk[free_idx], disk[file_idx]
    files.pop()
    frees.pop(0)

for file_idx, file_len in files2[::-1]:
    for i, (free_idx, free_len) in enumerate(frees2):
        if file_len <= free_len and file_idx > free_idx:
            for j in range(file_len):
                disk2[free_idx+j], disk2[file_idx+j] = disk2[file_idx+j], disk2[free_idx+j]
            frees2[i] = (free_idx+file_len, free_len-file_len)
            break

print(checksum(disk))
print(checksum(disk2))
