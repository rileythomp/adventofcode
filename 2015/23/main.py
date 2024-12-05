import sys 
from itertools import permutations

data = open(sys.argv[1]).read()

lines = data.split("\n")

instructions = [line.split() for line in lines]

regs = {'a': 0, 'b': 0}

i = 0 
while i < len(instructions): 
    instr = instructions[i][0]
    if instr in ('hlf', 'tpl', 'inc'):
        reg = instructions[i][1]
        match instr:
            case 'hlf': regs[reg] //= 2
            case 'tpl': regs[reg] *= 3
            case 'inc': regs[reg] += 1
        i += 1
    elif instr == 'jmp':
        i += int(instructions[i][1])
    elif instr in ('jie', 'jio'):
        reg_val = regs[instructions[i][1][0]]
        jmp = int(instructions[i][2])
        if instr == 'jie' and reg_val % 2 == 0:
            i += jmp 
        elif instr == 'jio' and reg_val == 1:
            i += jmp 
        else:
            i += 1

print(regs['b'])

regs = {'a': 1, 'b': 0}

i = 0 
while i < len(instructions): 
    instr = instructions[i][0]
    if instr in ('hlf', 'tpl', 'inc'):
        reg = instructions[i][1]
        match instr:
            case 'hlf': regs[reg] //= 2
            case 'tpl': regs[reg] *= 3
            case 'inc': regs[reg] += 1
        i += 1
    elif instr == 'jmp':
        i += int(instructions[i][1])
    elif instr in ('jie', 'jio'):
        reg_val = regs[instructions[i][1][0]]
        jmp = int(instructions[i][2])
        if instr == 'jie' and reg_val % 2 == 0:
            i += jmp 
        elif instr == 'jio' and reg_val == 1:
            i += jmp 
        else:
            i += 1

print(regs['b'])
