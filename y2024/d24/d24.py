from collections import deque
import copy
import sys
import os
# Add the root directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(root_dir)
from rich import print
# Print the current working directory and Python path for debugging
# print("Current working directory:", current_dir)
# print("Root directory added to Python path:", root_dir)
# print("Python path:", sys.path)

from utils.generic_functions import obtain_lines

# Print the Python path for debugging
# print("Python path:", sys.path)
from utils.generic_functions import obtain_lines

def extract_data(day_input: list[str]):
    store = {} 
    wires = []
    q = deque(day_input)
    while q:
        x = q.popleft()
        if not x:
            break
        a,b = x.split(': ')
        store[a] = (True, int(b ))
    
    
    while q:
        l = q.popleft().split()
        
        a = l[0]
        command = l[1]
        b = l[2]
        c = l[-1]
        store[c] = (False, (a, command, b))
        wires.append((a, command, b, c))
    return store, wires

ori_data, wires = extract_data(obtain_lines())


data = copy.deepcopy(ori_data) 

def get_number_value(data, c):
    assert c == 'x' or c == 'y'
    ans_keep = []
    for x in data:
        if x[0] == c:
            ans_keep.append(x)
    ans_keep.sort(reverse=True)
    ans = 0
    for x in ans_keep:
        ans = ans << 1
        ans += data[x][1] 
    return ans



X = get_number_value(data, 'x')
Y = get_number_value(data, 'y')

ZL = 47
def get_value(data, x=X, y=Y):
    def f(wire):
        if wire not in data:
            return 0
        done, value = data[wire]
        if done:
            if wire[0] == 'x':
                bt = int(wire[1:])
                return 1 if (x & (1 << bt) ) else 0
            if wire[0] == 'y':
                bt = int(wire[1:])
                return 1 if (y & (1 << bt)) else 0
            return value
        a, command, b = value
        match command:
            case 'AND':
                return f(a) & f(b)
            case 'OR':
                return f(a) | f(b)
            case 'XOR':
                return f(a) ^ f(b)

    for wire in data:
        f(wire)
    ans = 0
    for i in range(ZL, -1, -1):
        ans <<= 1
        if i < 10:
            ans += f(f'z0{i}')
        else:
            ans += f(f'z{i}')
    return ans

    


# print('Part 1:', get_value(data, 10424, 2))
'''
>>> get_value(data, 10424, 64)
10520
'''

def inspect(x, y):
    correct_z = x + y
    z = get_value(data, x ,y)
    if z == correct_z:
        # return True
        print(f'[green]Everything is fine, value z is {z}[/green]')
        return True

    bin_z = bin(z)[2:]
    bin_correct_z = bin(correct_z)[2:]
    max_len = max(len(bin_z), len(bin_correct_z))
    bin_z = bin_z.zfill(max_len)
    bin_correct_z = bin_correct_z.zfill(max_len)
    print(f'[red]{bin_z}[/red]')
    print(f'[green]{bin_correct_z}[/green]')
    # make a list of all the bits which are different between z and correct_z
    diff = []
    for i in range(48):
        if (z & (1 << i)) != (correct_z & (1 << i)):
            diff.append(i)
    
    if z != correct_z:
        print(f'{x}, {y},[red] {z}[/red],[green] {correct_z}[/green]')
        print(f'[red]Bits that are different: {diff}[/red]')
        return False



# X = 1
# Y = int('1' * 16, 2) 
X -= 18998999
Y -= 39585939

def range_inspect(a, b):
    for i in range(a - 2 , a + 2):
        for j in range(b - 10000, b + 10000, 144):
            if not inspect(i, j):
                break
# range_inspect(1 << 15, 146)
def find_value_of_wire(wire, x, y):
    if wire not in data:
        return 0
    done, value = data[wire]
    if done:
        if wire[0] == 'x':
            bt = int(wire[1:])
            return 1 if (x & (1 << bt) ) else 0
        if wire[0] == 'y':
            bt = int(wire[1:])
            return 1 if (y & (1 << bt)) else 0
        return value
    a, command, b = value
    match command:
        case 'AND':
            return find_value_of_wire(a, x, y) & find_value_of_wire(b, x,y)
        case 'OR':
            return find_value_of_wire(a, x, y) | find_value_of_wire(b, x,y)
        case 'XOR':
            return find_value_of_wire(a,x, y) ^ find_value_of_wire(b, x, y)

def f_wire(wire, depth = 0):
    if wire not in data:
        return 0
    done, value = data[wire]
    if done:
        if wire[0] == 'x' or wire[0] == 'y':
            bt = int(wire[1:])
            return wire 
            
    a, command, b = value
    if a[0] in 'xy' and b[0] in 'xy':
        return -1
    # print_a = find_value_of_wire(a, X, Y) if f_wire(a) != -1 else a
    # print_b = find_value_of_wire(b, X, Y) if f_wire(b) != -1 else b
    
    print('  ' * depth, f'{a}({find_value_of_wire(a, X, Y)}) {command} {b}({find_value_of_wire(b,X, Y)}) -> {wire}({find_value_of_wire(wire, X,Y)})') 
    match command:
        case 'AND':
            return f'({f_wire(a, depth + 1)}) & ({f_wire(b, depth + 1)})'
        case 'OR':
            return f'({f_wire(a, depth + 1)}) | ({f_wire(b, depth + 1)})'
        case 'XOR':
            return f'({f_wire(a, depth + 1)}) ^ ({f_wire(b, depth + 1)})'

f_wire('z00')
f_wire('z01')
    # f_wire('z20')
    # f_wire('z21')
    # f_wire('z22')
    # f_wire('z23')
    # f_wire('z24')

    # f_wire('rsk')
    # f_wire('z17')
answer = ['z05', 'frn']