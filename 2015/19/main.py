import heapq
import sys
from collections import defaultdict

data = open(sys.argv[1]).read().strip()
lines = data.split("\n")

word = lines[-1]

replacement_lines = [line.split(" => ") for line in lines[:-2]]
replacements = defaultdict(list)
for rl in replacement_lines:
    replacements[rl[0]].append(rl[1])

seen = {}
for i in range(len(word)):
    single_reps = replacements[word[i]]
    for rep in single_reps:
        new_word = word[:i] + rep + word[i+1:]
        seen[new_word] = True
    double_reps = replacements[word[i:i+2]]
    for rep in double_reps:
        new_word = word[:i] + rep + word[i+2:]
        seen[new_word] = True
print(len(seen))

# queue = [(1, -len(replace), replace) for replace in replacements["e"]]
queue = [(replace, 1) for replace in replacements["e"]]


print(queue)

seen = {}
queue_magnitude = 10
while queue:
    cur_word, steps = queue.pop()
    # steps, len_word, cur_word = heapq.heappop(queue)
    if cur_word in seen:
        continue
    seen[cur_word] = True
    if len(queue) > queue_magnitude:
        print(len(queue), steps, len(cur_word))
        queue_magnitude *= 2
    if cur_word == word:
        print("Found", steps)
        break
    for i in range(len(cur_word)):
        single_reps = replacements[cur_word[i]]
        for rep in single_reps:
            new_word = cur_word[:i] + rep + cur_word[i+1:]
            if new_word not in seen and len(new_word) <= len(word):
                # heapq.heappush(queue, ((steps+1, -len(new_word), new_word)))
                queue.append((new_word, steps+1))

        if i == len(cur_word) - 1:
            continue
        double_reps = replacements[cur_word[i:i+2]]
        for rep in double_reps:
            new_word = cur_word[:i] + rep + cur_word[i+2:]
            if new_word not in seen and len(new_word) <= len(word):
                # heapq.heappush(queue, ((steps+1, -len(new_word), new_word)))
                queue.append((new_word, steps+1))
