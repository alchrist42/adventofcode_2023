from pathlib import Path
from collections import Counter
from utils import nbs

def mnh(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# part 1
def solve(data: list[str]):
    res = 0
    for i in range(len(data) -1, -1,  -1):
        if all(x =="." for x in data[i]):
            data.insert(i, data[i])
    for j in range(len(data[0]) -1, -1,  -1):
        if all(data[row][j] =="." for row in range(len(data))):
            for row in range(len(data)):
                data[row] = data[row][:j] + "." + data[row][j:]
    print(*data, sep = "\n")

    pairs = []
    for row, line in enumerate(data):
        for col, ch in enumerate(line):
            if ch == "#":
                pairs.append((row, col))

    for i, pair in enumerate(pairs):
        for pair2 in pairs[i:]:
            res += mnh(pair, pair2)

    return res


# part 2
def solve(data: list[str]):
    res = 0
    years = 1000000 - 1
    hlp = list(range(len(data[0])))
    dst_row = [[row] * len(data[0]) for row in range(len(data))]
    dst_col = [hlp[:] for row in range(len(data))]


    for row in range(len(data)):
        if all(x == "." for x in data[row]):
            for y in range(row + 1, len(data)):
                for z in range(len(data[0])):
                    dst_row[y][z] += years

    for col in range(len(data[0])):
        if all(data[row][col] == "." for row in range(len(data))):
            for y in range(len(data)):
                for z in range(col + 1, len(data[0])):
                    dst_col[y][z] += years

    pairs = {}
    ind = 1
    for row, line in enumerate(data):
        for col, ch in enumerate(line):
            if ch == "#":
                pairs[ind] = (row, col)
                ind += 1

    pairs_lst = list(pairs.values())
    for i, pair1 in enumerate(pairs_lst):
        for pair2 in pairs_lst[i + 1:]:
            res += abs(dst_row[pair1[0]][pair1[1]] - dst_row[pair2[0]][pair2[1]])
            res += abs(dst_col[pair1[0]][pair1[1]] - dst_col[pair2[0]][pair2[1]])

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
