with open('in.txt', 'r') as file:
    data = file.read()
    chunks = data.split('\n\n')
    ranges = chunks[0].split('\n')
    numbers = chunks[1].split('\n')
    ns = []
    for n in numbers:
        if n == '':
            continue
        ns.append(int(n))
    numbers = ns
    rs = []
    for r in ranges:
        parts = r.split('-')
        rs.append((int(parts[0]), int(parts[1])))
    ranges = rs
    ans = 0
    for number in numbers:
        for r in ranges:
            if r[0] <= number <= r[1]:
                ans += 1
                break
    print(ans)

with open('in.txt', 'r') as file:
    data = file.read()
    chunks = data.split('\n\n')
    ranges = chunks[0].split('\n')
    rs = []
    for r in ranges:
        parts = r.split('-')
        rs.append((int(parts[0]), int(parts[1])))
    ranges = rs

    ans = 0
    cur_ranges = []
    for cur_start, cur_end in ranges:
        new_ranges = []
        while cur_ranges:
            start, end = cur_ranges.pop()
            overlap_start = max(cur_start, start)
            overlap_end = min(cur_end, end)
            overlap_diff = overlap_end - overlap_start + 1
            if overlap_diff < 0:
                new_ranges.append((start, end))
            else:
                cur_start = min(cur_start, start)
                cur_end = max(cur_end, end)
        new_ranges.append((cur_start, cur_end))
        cur_ranges = new_ranges

    print(sum([e - s + 1 for s, e, in cur_ranges]))
