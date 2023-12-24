from pathlib import Path
from collections import Counter, namedtuple
from utils import nbs

# part 1
Ur = namedtuple("Ur", "x, y, z, dx, dy, dz")

def solve(data: list[str], lb=200000000000000, rb=400000000000000):
    res = 0
    urs: dict[tuple, Ur] = {}
    for line in data:
        koord, napr = line.split(" @ ")
        x, y, z = map(int, koord.split(", "))
        dx, dy, dz = map(int, napr.split(", "))

        k = dy / dx
        b = y - x * k
        urs[(k, b)] = Ur(x, y, z, dx, dy, dz)
    
    for i, ur1 in enumerate(list(urs.keys())):
        for ur2 in list(urs.keys())[i + 1:]:
            print(f"match {ur1 =} {ur2 =}")
            dk = ur1[0] - ur2[0]
            db = ur2[1]  - ur1[1]
            if not dk:
                if db:
                    print("parallels")
                else:
                    print("matches")
            else:
                x_cross = db/ dk
                y_cross = ur1[0] * x_cross + ur1[1]
                if lb <= x_cross <= rb and lb <= y_cross <= rb:
                    passed1 = (y_cross - urs[ur1].y) / urs[ur1].dy
                    passed2 = (y_cross - urs[ur2].y) / urs[ur2].dy
                    if passed1 >= 0 and passed2 >= 0:
                        print(f"across in dot {x_cross}, {y_cross}")
                        res += 1
                    else:
                        print("across in past")
    return res


# part 2
import numpy as np
from sympy import Symbol
from sympy import solve_poly_system





path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

if example_data:
    print(f"Example answer: {solve(example_data, lb=7, rb=27)}\n")
print(solve(my_data))
