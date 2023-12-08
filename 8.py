from pathlib import Path
from collections import Counter
from utils import nbs
from itertools import cycle
from math import gcd, lcm


# part 1
def solve(data: list[str]):
    res = 0
    ins = data[0]
    dct = {line.split(" = ")[0]: line.split(" = ")[1].strip("()").split(", ") for line in data[1:]}
    key = "AAA"
    for i in cycle(ins):
        if i == "L":
            key = dct[key][0]
        else:
            key = dct[key][1]
        res += 1
        if key == "ZZZ":
            return res

    # print(dct)
    return res


# part 2
def solve(data: list[str]):
    res = 0
    ins = data[0]
    dct = {line.split(" = ")[0]: line.split(" = ")[1].strip("()").split(", ") for line in data[1:]}
    keys = [key for key in dct if key[2] == "A"]
    hlp = {key: [] for key in keys}
    zs = {}
    for key in keys:
        start_key = key
        step = 0
        for i in cycle(ins):
            key = dct[key][0 + (i == "R")]
            step += 1
            if key[2] == "Z":
                hlp[start_key].append(step)
                if len(hlp[start_key]) > 10:
                    break
    print(*[(key, [lst[i] - lst[i - 1] for i in range(1, len(lst))]) for key, lst in hlp.items()], sep="\n")
    pairs = [[lst[0], lst[-1] - lst[-2]] for lst in hlp.values()]
    print(pairs)
    for _ in range(10**10):
        if all(val == pairs[0][0] for val, p in pairs):
            return pairs[0][0]
        min_pair = min(pairs, key=lambda x: x[0] + x[1])
        min_pair[0] += min_pair[1]
        if _ % 1000:
            print(f"-{pairs[0][0]}-")
            break
    periods = [lst[-1] - lst[-2] for lst in hlp.values()]
    g = gcd(*periods)
    d = [p / g for p in periods]
    print("gcd=", g, d)
    ans = 1
    for digit in d:
        ans *= digit
    return ans, lcm(*periods)

    for i in cycle(ins):
        keys = [dct[key][0 + (i == "R")] for key in keys]
        res += 1
        if all(key[2] == "Z" for key in keys):
            return res

    print(dct)
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
