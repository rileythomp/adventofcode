def get_num(c, r):
    return (c*(c+1))//2 + (r-1)*c + ((r-1)*(r-2))//2

cache = {
    1: 20151125
}

def f(n):
    if n in cache:
        return cache[n]
    fn = (cache[n-1]*252533)%33_554_393
    cache[n] = fn
    return fn

ans = 0
for i in range(1, get_num(3029, 2947)+1):
    ans = f(i) 
print(ans)
    