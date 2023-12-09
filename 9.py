from pathlib import Path
from collections import Counter
from utils import nbs


# part 1
def solve(data: list[str]):
    res = 0
    for line in data:
        line = list(map(int, line.split()))
        lst = [line]
        for  i in range(1000):
            line = lst[-1]
            new_line = [line[i] - line[i-1] for i in range(1, len(line))]
            lst.append(new_line)
            if len(set(new_line)) == 1:
                x = new_line[-1]
                break
        x = 0
        prev = 0
        for line in reversed(lst):
            x += line[-1]
        print(x)
        res += x

    return res


# part 2
def solve(data: list[str]):
    res = 0
    for line in data:
        line = list(map(int, line.split()))
        lst = [line]
        for  i in range(1000):
            line = lst[-1]
            new_line = [line[i] - line[i-1] for i in range(1, len(line))]
            lst.append(new_line)
            if len(set(new_line)) == 1:
                break
        x = 0
        prev = 0
        for line in reversed(lst):
            x  = line[0] - x
        print(x)
        res += x

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
