import re
import os

print(os.getcwd())
a, b, c, *prog = map(int, re.findall(r'\d+',
                     open('y2024/d17/2.txt').read()))

def run(a, b, c):
    i, R = 0, []

    while i in range(len(prog)):
        C = {0:0,1:1,2:2,3:3,4:a,5:b,6:c}
        op = prog[i+1]

        match prog[i]:
            case 0: a>>= C[op]
            case 1: b ^= op
            case 2: b  = 7 & C[op]
            case 3: i  = op-2 if a else i
            case 4: b ^= c
            case 5: R += [C[op] & 7]
            case 6: b  = a >> C[op]
            case 7: c  = a >> C[op]
        i += 2
    return R

print(*run(a, b, c), sep=',')


todo = [(1, 0)]
for i, a in todo:
    for a in range(a, a+8):
        if run(a, 0, 0) == prog[-i:]:
            todo += [(i+1, a*8)]
            if i == len(prog): print(a)
