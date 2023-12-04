from pathlib import Path
from collections import Counter, defaultdict
from utils import nbs


# part 1
def solve(data: list[str]):
    res = 0
    for line in data:
        wins, my = line.split(":")[1].split("|")
        wins, my = list(map(int, wins.split())), list(map(int, my.split()))
        print(wins, my)
        step = [x for x in my if x in wins]
        print(step)
        steps = len(step)
        if steps:
            res += 2 ** (steps - 1)
        print(res)

    return res


# part 2
def solve(data: list[str]):
    dct = defaultdict(int)
    for game, line in enumerate(data):
        game += 1
        wins, my = line.split(":")[1].split("|")
        wins, my = list(map(int, wins.split())), list(map(int, my.split()))
        step = [x for x in my if x in wins]
        steps = len(step)
        dct[game] += 1
        if steps:
            insts = list(range(game + 1, game + 1 + steps))
            for card in insts:
                dct[card] += dct[game]
            # print(dct)
            
    return sum(dct.values())



path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

if example_data:
    print(f"Example answer: {solve(example_data)}\n")
print(solve(my_data))
