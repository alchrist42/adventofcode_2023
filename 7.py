from functools import lru_cache
from pathlib import Path
from collections import Counter
from utils import nbs
from functools import cmp_to_key

CARDSS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
HLP = {val: i for i,val in enumerate(CARDSS)}

@lru_cache()
def cost_hand(hand, use_jokers=False):
    sh = sorted(hand, key = lambda x: (-hand.count(x), HLP[x]))
    jokers = 0
    if use_jokers:
        jokers = sh.count("J")
        sh = [val for val in sh if val != "J"]
    # print(sh, end = ": ")
    if not sh or sh[0] == sh[4 - jokers]:
        return 7
    if sh[0] == sh[3 - jokers]:
        return 6
    if sh[0] == sh[2 - jokers]:
        if sh[3 - jokers] == sh[4 - jokers]:
            return 5
        else:  
            return 4
    if sh[0] == sh[1 - jokers]:
        if sh[2 - jokers] == sh[3 - jokers]:
            return 3
        else:
            return 2
    return 1

def compare(item1, item2):
    (hand1, score1, _1) = item1
    (hand2, score2, _2) = item2
    if score1 < score2:
        return -1
    elif score1 > score2:
        return 1
    else:
        for a, b in zip(hand1, hand2):
            if a == b:
                continue
            if HLP[a] < HLP[b]:
                return 1
            else:
                return -1
    return 0


# part 1
CARDSS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
def solve(data: list[str]):
    res = 0
    game = [(line.split()[0], cost_hand(line.split()[0]), int(line.split()[1])) for line in data]
    game.sort(key=cmp_to_key(compare))

    for i in range(len(game)):
        res += (i + 1) * game[i][2]
    return res


# part 2
CARDSS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
def solve(data: list[str], use_jokers=True):
    res = 0
    game = [(line.split()[0], cost_hand(line.split()[0], use_jokers=use_jokers), int(line.split()[1])) for line in data]
    game.sort(key=cmp_to_key(compare))

    for i in range(len(game)):
        res += (i + 1) * game[i][2]
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
