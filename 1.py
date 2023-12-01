from pathlib import Path
from collections import Counter

# part 1
def solve(data: list[str]):
    res = 0
    for line in data:
        x = ""
        for ch in line:
            if ch.isdigit():
                x += ch
        print(x)
        res += int(x[0] + x[-1])

    return res

# part 2
lst = "one, two, three, four, five, six, seven, eight, nine".split(", ")
dct = {str(x): str(x) for x in range(1, 10)}
for x in range(1, 10):
    dct[lst[x-1]] = str(x)

def solve(data: list[str]):
    res = 0
    for line in data:
        first = None
        last = None
        for i in range(len(line)):
            for key in dct:
                if line[i:].startswith(key):
                    if first is None:
                        first = dct[key]
                    last = dct[key]
        print(first, last)
        res += int(first + last)

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
