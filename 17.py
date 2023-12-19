from pathlib import Path
from collections import Counter, namedtuple
from utils import nbs

from queue import PriorityQueue
from dataclasses import dataclass, field

Pos = namedtuple("Pos", "y x")


@dataclass(order=True)
class PriItem:
    priority: int
    lava: field(compare=False)
    cur: field(compare=False)
    prev: field(compare=False)
    steps: field(compare=False)
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
    res = 0
    gy, gx = len(data), len(data[0])
    goal = Pos(gy - 1, gx - 1)
    # h = [[[] for x in range(gx)]  for y in range(gy)]

    queue = PriorityQueue()
    pr = sum(goal)
    lava = 0
    cur = Pos(0, 0)
    prev = Pos(-1, 0)
    steps = 0
    queue.put(PriItem(pr, lava, cur, prev, steps, []))
    cache = set()
    for iter_count in range(10**20):
        item: PriItem = queue.get()
        pr, lava, cur, prev, steps, his = item.priority, item.lava, item.cur, item.prev, item.steps, item.history
        if cur == goal:
            print_lava_way(data, his)
            return lava
        poss_moves = nbs(data, *cur, diag=False, coord=True)
        poss_moves.pop(prev, None)  # TODO save
        for move, cost in poss_moves.items():
            if any(abs(b - a) == 2 for a, b in zip(move, prev)):
                new_steps = steps + 1
            else:
                new_steps = 1
            if new_steps == 4:
                continue

            key_cache = (move, cur, new_steps)
            if key_cache in cache:
                continue
            cache.add(key_cache)
            n_his = his[:] + [move]

            new_lava = lava + int(cost)
            pr = new_lava + 2 * (sum(goal) - sum(move))
            queue.put(PriItem(pr, new_lava, move, cur, new_steps, n_his))

    return res


# part 2
def solve(data: list[str]):
    res = 0
    gy, gx = len(data), len(data[0])
    goal = Pos(gy - 1, gx - 1)
    rows_min = 0

    queue = PriorityQueue()
    pr = sum(goal)
    lava = 0
    cur = Pos(0, 0)
    prev = Pos(-1, 0)
    steps = 0
    queue.put(PriItem(pr, lava, cur, prev, steps, []))
    queue.put(PriItem(pr, lava, cur, Pos(0, -1), steps, []))
    cache = set()
    for iter_count in range(10**20):
        item: PriItem = queue.get()
        pr, lava, cur, prev, steps, his = item.priority, item.lava, item.cur, item.prev, item.steps, item.history
        if cur == goal:
            print_lava_way(data, his)
            return lava
        
        poss_moves = nbs(data, *cur, diag=False, coord=True)
        poss_moves.pop(prev, None)  # TODO save
        for move, cost in poss_moves.items():
            if any(abs(b - a) == 2 for a, b in zip(move, prev)):
                new_steps = steps + 1
            else:
                new_steps = 1
            if new_steps == 11:
                continue
            elif steps < 4 and new_steps != steps + 1:
                continue

            key_cache = (move, cur, new_steps)
            if key_cache in cache:
                continue
            cache.add(key_cache)
            # n_his = his
            n_his = his[:] + [move]

            new_lava = lava + int(cost)
            pr = new_lava + 2 * (sum(goal) - sum(move))
            queue.put(PriItem(pr, new_lava, move, cur, new_steps, n_his))

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
