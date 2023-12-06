from pathlib import Path
from collections import Counter
from utils import nbs


# part 1
def solve(data: list[str]):
    res = 1
    ts = list(map(int, data[0].split(":")[1].split()))
    dsts = list(map(int, data[1].split(":")[1].split()))
    runs = {key: val for key, val in zip(ts, dsts)}
    res_dct = {}
    max_t = max(ts)
    for t in range(max_t):
        res_dct[t] = (max_t - t) * t
    for key, dst in runs.items():
        lres = 0
        for t in range(key):
            print(t, t * (key - t))
            if t * (key - t) > dst:
            # res_dct[t]  - (max_t - t) * 7 * t > dst:
                lres += 1
        print(lres, "\n")
        res *= lres
    return res


# part 2
def solve(data: list[str]):
    res = 0
    trace = int(data[0].split(":")[1].replace(" ", ""))
    dst = int(data[1].split(":")[1].replace(" ", ""))
    for t in range(trace + 1):
        # print(t, t * (dst - t))
        if t * (trace - t) > dst:
        # res_dct[t]  - (max_t - t) * 7 * t > dst:
            res += 1
    print(t, dst)
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
