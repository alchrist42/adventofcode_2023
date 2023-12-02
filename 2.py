from pathlib import Path
from collections import Counter

dct = {"red": 12, "green": 13, "blue": 14}

# part 1
def solve(data: list[str]):
    res = 0
    for line in data:
        if ":" not in line:
            continue
        game, line = line.split(":")
        game_id = int(game.split()[1])
        for scores in line.split(";"):
            if any(dct[score.split()[1]] < int(score.split()[0]) or int(score.split()[0]) < 0 for score in scores.split(",")):
                break
        else:
            res += game_id


    return res

# part 2
def solve(data: list[str]):
    res = 0
    for line in data:
        if ":" not in line:
            continue
        _, line = line.split(":")

        dct2 = {"red": 0, "green": 0, "blue": 0}
        for scores in line.split(";"):
            for score in scores.split(","):
                dct2[score.split()[1]] = max(dct2[score.split()[1]], int(score.split()[0]))
        ans = 1
        for val in dct2.values():
            ans *= val
        res += ans


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
