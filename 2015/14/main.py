import sys 
from collections import defaultdict

data = open(sys.argv[1]).read()

lines = data.split("\n")

reindeers = {
    vals[0]: (int(vals[3]), int(vals[6]), int(vals[6])+int(vals[-2]))
    for vals in [line.split() for line in lines]
}


pts = defaultdict(int)
duration = 2505
# duration = 1002
for t in range(1, duration):
    scores = []
    for reindeer, (speed, speed_dur, total_dur) in reindeers.items():
        dist = (t//(total_dur)*speed_dur + min(t % total_dur , speed_dur)) * speed
        scores.append((dist, reindeer))
    if t == duration-2:
        print(max(scores)[0])
    pts[max(scores)[1]] += 1

print(max(pts.values()))



