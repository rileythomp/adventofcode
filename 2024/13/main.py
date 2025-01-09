import sys
from math import lcm

data = open(sys.argv[1]).read().strip()
groups = data.split('\n\n')

ans, ans2 = 0, 0
for group in groups:
    lines = group.split('\n')
    ax = int(lines[0].split()[2][2:][:-1])
    ay = int(lines[0].split()[3][2:])
    bx = int(lines[1].split()[2][2:][:-1])
    by = int(lines[1].split()[3][2:])
    px = int(lines[2].split()[1][2:][:-1])
    py = int(lines[2].split()[2][2:])
    px2 = px + 10000000000000
    py2 = py + 10000000000000

    a_lcm = lcm(ax, ay)
    x_mult, y_mult = a_lcm//ax, a_lcm//ay

    if (x_mult*px - y_mult*py) % (bx*x_mult - by*y_mult) == 0:
        b = (x_mult*px - y_mult*py)//(bx*x_mult - by*y_mult)
        if (px-bx*b) % ax == 0:
            a = (px-bx*b)//ax
            if a <= 100 and b <= 100:
                ans += 3*a+b

    if (x_mult*px2 - y_mult*py2) % (bx*x_mult - by*y_mult) == 0:
        b = (x_mult*px2 - y_mult*py2)//(bx*x_mult - by*y_mult)
        if (px2-bx*b) % ax == 0:
            a = (px2-bx*b)//ax
            ans2 += 3*a+b

print(ans)
print(ans2)
