with open('in.txt', 'r') as file:
    nums = file.read().splitlines()
    ans = 0
    for num in nums:
        first = -1
        first_i = -1
        for i in range(len(num[:-1])):
            if int(num[i]) > first:
                first, first_i = int(num[i]), i
        second = max([int(num[i]) for i in range(first_i + 1, len(num))])
        ans += 10*first + second
    print(ans)

with open('in.txt', 'r') as file:
    nums = file.read().splitlines()
    ans = 0
    for num in nums:
        max_num, max_i = 0, -1
        for pos in range(2, 0, -1):
            pos_max, pos_max_i = -1, -1
            for i in range(max_i+1, len(num)-pos+1):
                if int(num[i]) > pos_max and i > max_i:
                    pos_max, pos_max_i = int(num[i]), i
            max_num, max_i = max_num*10 + pos_max, pos_max_i
        ans += max_num
    print(ans)

with open('in.txt', 'r') as file:
    nums = file.read().splitlines()
    ans = 0
    for num in nums:
        max_num, max_i = 0, -1
        for pos in range(12, 0, -1):
            pos_max, pos_max_i = -1, -1
            for i in range(max_i+1, len(num)-pos+1):
                if int(num[i]) > pos_max and i > max_i:
                    pos_max, pos_max_i = int(num[i]), i
            max_num, max_i = max_num*10 + pos_max, pos_max_i
        ans += max_num
    print(ans)
