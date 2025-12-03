with open('in.txt', 'r') as file:
    data = [[int(n) for n in x.split('-')] for x in file.read().split(',')]
    ans = 0
    for lower, upper in data:
        for n in range(lower, upper + 1):
            if str(n)[:len(str(n))//2] == str(n)[len(str(n))//2:]:
                ans += n
    print(ans)

with open('in.txt', 'r') as file:
    data = [[int(n) for n in x.split('-')] for x in file.read().split(',')]
    ans = 0
    for lower, upper in data:
        for n in range(lower, upper + 1):
            strn = str(n)
            for i in range(1, len(strn)//2 + 1):
                parts = [strn[k:k+i] for k in range(0, len(strn), i)]
                if all(parts[0] == part for part in parts):
                    ans += n
                    break
    print(ans)
