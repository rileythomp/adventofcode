import sys 

data = open(sys.argv[1]).read().strip() 

lines = data.split("\n")

def increment_password(password):
    password = list(password)
    i = len(password) - 1
    if password[i] == 'z':
        password[i] = 'a'
        i -= 1
        while i >= 0 and password[i] == 'z':
            password[i] = 'a'
            i -= 1
        if i >= 0:
            password[i] = chr(ord(password[i]) + 1) 
        if i < 0:
            password = ['a'] + password
    else:
        password[i] = chr(ord(password[i]) + 1)
    return ''.join(password)

def valid_password(password):
    broke = False 
    for i in range(2, len(password)):
        if ord(password[i]) == ord(password[i-1]) + 1 and ord(password[i]) == ord(password[i-2]) + 2:
            broke = True 
            break
    if not broke:
        return False
    if 'i' in password or 'o' in password or 'l' in password:
        return False 
    pairs = set()
    for i in range(1, len(password)):
        if password[i] == password[i-1] and password[i] not in pairs:
            pairs.add(password[i])
    return len(pairs) >= 2      

def next_password(password):
    while True:
        password = increment_password(password)
        if valid_password(password):
            return password

for line in lines:
    ans = next_password(line)
    print(ans) 
    print(next_password(ans))