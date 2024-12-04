card_pub_key = 5764801

door_pub_key = 17807724


cache = {
    7: {
        0: 1
    }
}

def transform(subject_num, loop_size):
    if subject_num not in cache: 
        cache[subject_num] = {0: 1}
    if loop_size in cache[subject_num]:
        return cache[subject_num][loop_size]
    v = cache[subject_num][loop_size-1]
    v *= subject_num
    v %= 20201227
    cache[subject_num][loop_size] = v
    return v

door_loop_size = 11
for i in range(1, door_loop_size+1):
    print(transform(7, i)) 
print()

card_loop_size = 8
for i in range(1, card_loop_size+1):
    print(transform(7, i))
print()

# exit()


for i in range(1, card_loop_size+1):
    print(transform(door_pub_key, i))
print()

for i in range(1, door_loop_size+1):
    print(transform(card_pub_key, i))
print()

######

card_pub_key = 5290733
door_pub_key = 15231938

card_loop_size = None
for i in range(1, 10_000_000):
    if transform(7, i) == card_pub_key:
        card_loop_size = i
        break
print('card loop', card_loop_size)

door_loop_size = None
for i in range(1, 10_000_000):
    if transform(7, i) == door_pub_key:
        door_loop_size = i
        break
print('door loop', door_loop_size)

ans = 0
for i in range(1, card_loop_size+1):
    ans = transform(door_pub_key, i)
print(ans)

ans = 0
for i in range(1, door_loop_size+1):
    ans = transform(card_pub_key, i)
print(ans)