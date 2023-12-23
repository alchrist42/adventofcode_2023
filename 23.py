from pathlib import Path
from collections import Counter, namedtuple
from utils import nbs
from queue import PriorityQueue
from dataclasses import dataclass, field

Pos = namedtuple("Pos", "y x")


@dataclass(order=True)
class PriItem:
    priority: int
    cur: field(compare=False)
    steps: field(compare=False)
    # field: field(compare=False)
    # prev: field(compare=False)
    history: field(compare=False)

def print_lava_way(data, steps):
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if (i, j) in steps:
                print('\033[31m' + c + '\033[39m', end = "")
            else:
                print(c, end = "")
        print()

# part 1
def solve(data: list[str]):
    n, m = len(data), len(data[0])
    start = Pos(0, 1)
    end = Pos(n-1, m-2)
    res = 0

    hlp = [[0] * m for _ in range(n)]

    queue = PriorityQueue()
    pr = sum(start)
    steps = 0
    cur = Pos(0, 1)
    his = set([ Pos(0, 1),])
    steps = 0
    queue.put(PriItem(pr, cur, steps, his))
    cache = {}
    for iter_count in range(10**20):
        item: PriItem = queue.get()
        pr, cur, steps, his = item.priority, item.cur, item.steps, item.history
        if cur == end:
            print("end", steps)
            print_lava_way(data, his)
            continue
        y, x = cur
        if cache.get(cur, -1) >= steps:
            continue
        cache[cur] = steps

        poss_moves = nbs(data, *cur, diag=False, coord=True)
        for (ny, nx), val in poss_moves.items():
            nsteps = steps + 2
            if val == ">" and nx > x:
                nx += 1
            elif val == "<" and nx < x:
                nx -= 1
            elif val == "^" and ny < y:
                ny -= 1
            elif val == "v" and ny > y:
                ny += 1
            else:
                nsteps -= 1
            if data[ny][nx] == "." and Pos(ny, nx) not in his:
                npos = Pos(ny, nx)
                pr = nx + ny - nsteps
                nhis = set.copy(his)
                nhis.add(npos)
                queue.put(PriItem(pr, npos, nsteps, nhis))

    return cache[end]


# part 2
def solve(data: list[str]):
    n, m = len(data), len(data[0])
    start = Pos(0, 1)
    end = Pos(n-1, m-2)
    res = 0

    hlp = [[0] * m for _ in range(n)]

    queue = PriorityQueue()
    pr = sum(start)
    steps = 0
    cur = Pos(0, 1)
    his = set([ Pos(0, 1),])
    steps = 0
    queue.put(PriItem(pr, cur, steps, his))
    cache = {}
    while not queue.empty():
        item: PriItem = queue.get()
        pr, cur, steps, his = item.priority, item.cur, item.steps, item.history
        cache[cur] = max(cache.get(cur, -1), steps)
        if cur == end:
            print("end", steps, "max=", cache[end])
            # print_lava_way(data, his)
        # if cache.get(cur, -1) >= steps:
        #     continue

        poss_moves = nbs(data, *cur, diag=False, coord=True)
        for npos, val in poss_moves.items():
            nsteps = steps + 1
            if val != "#" and npos not in his:
                pr = sum(npos) * 2 - nsteps
                nhis = set.copy(his)
                nhis.add(npos)
                queue.put(PriItem(pr, npos, nsteps, nhis))

    

    return cache[end]



path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

if example_data:
    print(f"Example answer: {solve(example_data)}\n")
print(solve(my_data))
