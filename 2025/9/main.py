with open('in.txt', 'r') as file:
    data = file.read()
    lines = data.splitlines()
    pts = []
    for line in lines:
        x, y = line.split(',')
        pts.append((int(x), int(y)))
    ans = 0
    for i in range(len(pts) - 1):
        for j in range(i + 1, len(pts)):
            p1 = pts[i]
            p2 = pts[j]
            dx = abs(p1[0] - p2[0]) + 1
            dy = abs(p1[1] - p2[1]) + 1
            area = dx * dy
            ans = max(ans, area)
    print(ans)
