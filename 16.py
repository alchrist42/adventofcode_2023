from pathlib import Path
from collections import Counter
from utils import nbs

import sys
sys.setrecursionlimit(1000000)
                      
# part 1
def solve(data: list[str], start=(0, 0), prev=(0, -1)):
    res = 0
    h = [[0] * len(data) for _ in range(len(data))]
    passed = set()

    def rec(p, d):
        y, x = p
        yp, xp = d
        if not ( -1 < y < len(data) and -1 < x < len(data[0])):
            return
        if (p, d) in passed:
            return
        h[y][x] = 1
        passed.add((p, d))
        ch = data[y][x]

        # for i, line in enumerate(data):
        #     for j, c in enumerate(line):
        #         if i == y and j == x:
        #             print('\033[31m' + c + '\033[39m', end = "")
        #         elif i == yp and j == xp:
        #             print('\033[32m' + c + '\033[39m', end = "")
        #         else:
        #             print(c, end = "")
        #     print()
        
        pass
        if ch == "." or ch == "|" and yp - y or ch == "-" and xp - x:
            np = (y + y - yp, x + x - xp)
            rec(np, p)
        elif ch in "/\\":
            ny =  y + (x - xp)  * ((-1) ** (ch == "/"))
            nx =  x + (y - yp)  * ((-1) ** (ch == "/"))
            np = (ny, nx)
            rec(np, p)
        elif ch in "|-":
            y1, y2 =  [y + (x - xp)  * (-1) ** i for i in (1,2)]
            x1, x2 =  [x + (y - yp)  * (-1) ** i for i in (1,2)]
            np1 = (y1, x1)
            np2 = (y2, x2)
            rec(np1, p)
            rec(np2, p)
        else:
            raise Exception("not recognize char")

    
    rec (start, prev)
    for line in h:
        # print(line)
        res += sum(line)
    return res


# part 2
def solve2(data: list[str]):
    res = 0

    for row in range(len(data)):
        lres = solve(data, (row, 0), (row, -1))
        rres = solve(data, (row, len(data[0]) - 1), (row, len(data[0])))
        res = max(res, lres, rres)
    for col in range(len(data[0])):
        ures = solve(data, (0, col), (-1, col))
        dres = solve(data, (len(data) - 1, col), (len(data), col))
        res = max(res, ures, dres)

    return res


path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

if example_data:
    print(f"Example answer: {solve2(example_data)}\n")
print(solve2(my_data))
