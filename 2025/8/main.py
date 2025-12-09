import heapq


def dist(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5

with open('in.txt', 'r') as file:
    data = file.read()
    lines = data.splitlines()
    pts = []
    for line in lines:
        x, y, z = line.split(',')
        pts.append((int(x), int(y), int(z)))
    min_heap = []
    for i in range(len(pts)-1):
        pt1 = pts[i]
        for j in range(i + 1, len(pts)):
            pt2 = pts[j]
            d = dist(pt1, pt2)
            heapq.heappush(min_heap, (d, pt1, pt2))
    group_to_pts = {}
    pts_to_group = {}
    groups = 0
    for i in range(1000):
        d, p1, p2 = heapq.heappop(min_heap)
        if p1 not in pts_to_group and p2 not in pts_to_group:
            pts_to_group[p1] = groups
            pts_to_group[p2] = groups
            group_to_pts[groups] = [p1, p2]
            groups += 1
        elif p1 in pts_to_group and p2 not in pts_to_group:
            g = pts_to_group[p1]
            pts_to_group[p2] = g
            group_to_pts[g].append(p2)
        elif p2 in pts_to_group and p1 not in pts_to_group:
            g = pts_to_group[p2]
            pts_to_group[p1] = g
            group_to_pts[g].append(p1)
        else:
            g1 = pts_to_group[p1]
            g2 = pts_to_group[p2]
            if g1 != g2:
                for pt in group_to_pts[g2]:
                    pts_to_group[pt] = g1
                    group_to_pts[g1].append(pt)
                del group_to_pts[g2]

    max_heap = []
    for g, pts in group_to_pts.items():
        heapq.heappush(max_heap, -len(pts))
    ans = 1
    for i in range(3):
        ans *= -heapq.heappop(max_heap)
    print(ans)

with open('in.txt', 'r') as file:
    data = file.read()
    lines = data.splitlines()

    pts = []
    pts_set = set()
    for line in lines:
        x, y, z = line.split(',')
        pts.append((int(x), int(y), int(z)))
        pts_set.add((int(x), int(y), int(z)))

    min_heap = []
    for i in range(len(pts)-1):
        pt1 = pts[i]
        for j in range(i + 1, len(pts)):
            pt2 = pts[j]
            d = dist(pt1, pt2)
            heapq.heappush(min_heap, (d, pt1, pt2))

    group_to_pts = {}
    pts_to_group = {}
    groups = 0
    while min_heap:
        d, p1, p2 = heapq.heappop(min_heap)
        if p1 not in pts_to_group and p2 not in pts_to_group:
            pts_to_group[p1] = groups
            pts_to_group[p2] = groups
            group_to_pts[groups] = [p1, p2]
            groups += 1
            pts_set.remove(p1)
            pts_set.remove(p2)
        elif p1 in pts_to_group and p2 not in pts_to_group:
            g = pts_to_group[p1]
            pts_to_group[p2] = g
            group_to_pts[g].append(p2)
            pts_set.remove(p2)
        elif p2 in pts_to_group and p1 not in pts_to_group:
            g = pts_to_group[p2]
            pts_to_group[p1] = g
            group_to_pts[g].append(p1)
            pts_set.remove(p1)
        else:
            g1 = pts_to_group[p1]
            g2 = pts_to_group[p2]
            if g1 != g2:
                for pt in group_to_pts[g2]:
                    pts_to_group[pt] = g1
                    group_to_pts[g1].append(pt)
                del group_to_pts[g2]
        if len(pts_set) == 0 and len(group_to_pts) == 1:
            print(p1[0] * p2[0])
            break
