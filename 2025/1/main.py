with open('in.txt', 'r') as f:
    data = f.read()
    lines = data.splitlines()
    ans = 0
    cur = 50
    for line in lines:
        direction = line[0]
        num = int(line[1:])
        cur = (cur + (num if direction == 'R' else -num)) % 100
        if cur == 0:
            ans += 1
    print(ans)


with open('in.txt', 'r') as f:
    data = f.read()
    lines = data.splitlines()
    ans = 0
    cur = 50
    for line in lines:
        direction = line[0]
        num = int(line[1:])
        for i in range(num):
            cur += 1 if direction == 'R' else -1
            cur %= 100
            if cur == 0:
                ans += 1
    print(ans)
