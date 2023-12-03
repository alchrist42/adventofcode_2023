from pathlib import Path
from collections import Counter


# part 1
def solve(data: list[str]):
    res = 0
    ds = set()
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch != "." and not ch.isdigit():
                # check near:
                for col in range(x - 1, x + 2):
                    if col < 0 or col == len(line):
                        continue
                    for row in range(y - 1, y + 2):
                        if row < 0 or row == len(data):
                            continue
                        if data[row][col].isdigit():
                            start, end = col, col
                            while start >= 0 and data[row][start].isdigit():
                                start -= 1
                            while end < len(line) and data[row][end].isdigit():
                                end += 1
                            x = int(data[row][start + 1 : end])
                            if (ch, x, row, start + 1) not in ds:
                                ds.add((ch, x, row, start + 1))
                                res += x
    return res


# part 2
def solve(data: list[str]):
    res = 0
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch == "*":
                ds = set()
                for col in range(x - 1, x + 2):
                    if col < 0 or col == len(line):
                        continue
                    for row in range(y - 1, y + 2):
                        if row < 0 or row == len(data):
                            continue
                        if data[row][col].isdigit():
                            start, end = col, col
                            while start >= 0 and data[row][start].isdigit():
                                start -= 1
                            while end < len(line) and data[row][end].isdigit():
                                end += 1
                            x = int(data[row][start + 1 : end])
                            if (ch, x, row, start + 1) not in ds:
                                ds.add((ch, x, row, start + 1))
                # print(ds)
                if len(ds) == 2:
                    mlt = 1
                    for ch, x, *_ in ds:
                        mlt *= x
                    res += mlt

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
