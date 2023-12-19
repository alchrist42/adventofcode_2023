from pathlib import Path
from collections import Counter, defaultdict, namedtuple
from utils import nbs

DIRECTIONS = {
    "D": (1, 0),
    "U": (-1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

Pos = namedtuple("Pos", "y x")

# part 1
def solve(data: list[str]):
    res = 0
    dct = dict() #
    ldct = dict()
    dot = [0, 0]
    for line in  data:
        d, steps, color = line.split()
        steps  = int(steps)
        for step in range(1, 1 + steps):
            dot[0] += DIRECTIONS[d][0]
            dot[1] += DIRECTIONS[d][1]
            dct[Pos(*dot)] = color
            if d == "D":
                ldct[Pos(*dot)] = color
                if prev_dot is not None:
                    ldct[prev_dot] = prev_color
                    prev_dot = None
            else:
                prev_dot, prev_color = Pos(*dot), color
            res += 1

    filled = 0
    direct = -1
    for pos in ldct:
        for i in range(1, 10**5):
            if Pos(pos.y, pos.x + i * direct) not in dct:
                filled += 1
            else:
                break
        else:
            raise Exception("need change direct to -1")

    return res + filled

DIRECTIONS_MATCH = {
    "1": "D",
    "3": "U",
    "2": "L",
    "0": "R"
}

# part 2
def solve(data: list[str]):
    res = 0
    ldct = defaultdict(list)
    rdct = defaultdict(list)
    dot = [0, 0]
    prev_d = ""
    for line in  data:
        d, steps, color = line.split()

        color = color.strip("#()")
        d = DIRECTIONS_MATCH[color[-1]]
        steps = int(color[:-1], base=16)
        for step in range(1, 1 + steps):
            dot[0] += DIRECTIONS[d][0]
            dot[1] += DIRECTIONS[d][1]

            
            if not step:
                if d == "D" and prev_d == "L":
                    ldct[prev_dot[0]].append(prev_dot[1])
                elif d == "U" and prev_d == "R":
                    rdct[prev_dot[0]].append(prev_dot[1])
                elif d == "R" and prev_d == "D":
                    ldct[prev_dot[0]].append(prev_dot[1])
                elif d == "L" and prev_d == "U":
                    rdct[prev_dot[0]].append(prev_dot[1])
            elif d == "D":
                ldct[dot[0]].append(dot[1])
            elif d == "U" and prev_d != "L":
                rdct[dot[0]].append(dot[1])

            prev_dot, prev_d = dot[:], d
            res += 1

    filled = 0
    direct = -1
    for pos in ldct:
        for i in range(1, 10**5):
            if Pos(pos.y, pos.x + i * direct) not in dct:
                filled += 1
            else:
                break
        else:
            raise Exception("need change direct to -1")

    return res + filled


path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

if example_data:
    print(f"Example answer: {solve(example_data)}\n")
# print(solve(my_data))
