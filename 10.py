from pathlib import Path
from collections import Counter
from time import sleep
from utils import nbs
from termcolor import colored

moves = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, -1), (1, 0)],
    "F": [(1, 0), (0, 1)],
    ".": [],
    "S": [],
}
# part 1
def solve(data: list[str]):
    res = 0
    for row, line in enumerate(data):
        data[row] = list(line)
        for col, v in enumerate(line):
            if v == "S":
                pos = (row, col)

    # found next move for "S"
    row, col = pos
    data[row][col] = "0"
    for nc, nv in nbs(data, row, col, diag=False, coord=True).items():
        possibles = [(nc[0] + y, nc[1] + x) for y, x in moves[nv]]
        if pos not in possibles:
            continue
        prev, pos = pos, nc
        break

    
    # move across the loop
    for res in range(1, 10**10):
        row, col = pos
        val = data[row][col]
        if val == "0": # for S
            print()
            print(*[''.join(line) for line in data], sep="\n")
            return res // 2 + res % 2
        data[row][col] = str(res)
               

    return res




# part 2
def pp(data, to_close, closed=set()):
    for row, line in enumerate(data):
        for col, v in enumerate(line):
            if (row, col) in closed:
                print(colored(v, 'red'), end="")
            elif (row, col) in to_close:
                print(colored(v, 'green'), end="")
            
            else:
                print(v, end="")
        print()
    sleep(0.02)

def solve(data: list[str]):
    res = 0
    for row, line in enumerate(data):
        data[row] = list(line)
        for col, v in enumerate(line):
            if v == "S":
                pos = (row, col)

    # found next move for "S"
    row, col = pos
    data[row][col] = "0"
    for nc, nv in nbs(data, row, col, diag=False, coord=True).items():
        possibles = [(nc[0] + y, nc[1] + x) for y, x in moves[nv]]
        if pos not in possibles:
            continue
        prev, pos = pos, nc
        break

    to_close = set()
    # move across the loop
    for step in range(1, 10**10):
        row, col = pos
        val = data[row][col]
        if val == "0": # for S
            break
        shift = -1 # or 1, depends from left or right closed part from direction move
        if prev[0] < pos[0]: # from up
            to_close.add((row-1, col + shift))
            to_close.add((row, col + shift))
        elif prev[0] > pos[0]:
            to_close.add((row+1, col - shift))
            to_close.add((row, col - shift))
        elif prev[1] < pos[1]: # from left
            to_close.add((row - shift, col-1))
            to_close.add((row - shift, col))
        else:
            to_close.add((row + shift, col+1))
            to_close.add((row + shift, col))

        data[row][col] = "#"
        nxt = [(row+y, col+x) for y, x in moves[val] if (row+y, col+x) != prev][0]
        pos, prev  = nxt, pos
        # pp(data, to_close)
        
    closed = set()

    def fill(row, col):
        nonlocal res
        if row < 0 or row == len(data) or col < 0 or col == len(data[0]):
            return
        if data[row][col] in "0OI#":
            return
        nears = set([(row, col),])
        # print(nears)
        while nears:
            pos = nears.pop()
            row, col = pos
            # print(nbs(data, row, col, diag=False, coord=True).items())
            res += 1
            closed.add(pos)
            data[row][col] = "I"
            nears.update(k for k, v in nbs(data, row, col, diag=False, coord=True).items() if v not in "0OI#")

    for row, col in to_close:
        fill(row, col)
    pp(data, to_close, closed)
    return res



path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

if example_data:
    print(f"Example answer: {solve(example_data)}\n")
print(solve(my_data))
