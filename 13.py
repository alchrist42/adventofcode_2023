from pathlib import Path
from collections import Counter
from utils import nbs


# part 1
def solve(data: list[str]):
    res = 0
    def find_pattern(lava: list[str]):
        horiz, vert = 0, 0
        for row in range(len(lava) - 1):
            if lava[row]  == lava[row + 1]:
                for i in range(1, min(len(lava) - row - 1, row + 1)):
                    if lava[row - i] == lava[row + 1 + i]:
                        continue
                    else:
                        break
                else:
                    horiz = row + 1
        
        for col in range(len(lava[0]) - 1):
            if all(lava[row][col]  == lava[row][col + 1] for row in range(len(lava))):
                for i in range(1, min(len(lava[0]) - col - 1, col + 1)):
                    if all(lava[row][col - i] == lava[row][col + 1 + i] for row in range(len(lava))):
                        continue
                    else:
                        break
                else:
                    vert = col + 1
        return horiz, vert


    for lava in data:
        h, v = find_pattern(lava)
        res += h * 100 + v
    # print(lava for lava in data)
    return res


# part 2
def solve(data: list[str]):
    res = 0
    def find_pattern(lava: list[str]):
        ans = 0
        hlp = [[-1] * len(lava) for _ in lava]
        for i, l1 in enumerate(lava):
            for j in range(i + 1, len(lava), 2):
                l2 = lava[j]
                hlp[i][j] = hlp[j][i] = sum(ch1 != ch2 for ch1, ch2 in zip(l1, l2))
        
        for row in range(1, len(lava)):
            if sum(hlp[row + i][row - 1 - i] + hlp[row - 1 - i][row + i] for i in range(min(row, len(lava) + (len(lava) % 2 == 0) - row))) == 2:
                if ans:
                    raise Exception()
                ans = row
        return ans


    for lava in data:
        h = find_pattern(lava)
        v = find_pattern(list(zip(*lava)))
        res += h * 100 + v
    return res


path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [data_block.split("\n") for data_block in f.read().split("\n\n")]
with open(f"{filename}.txt") as f:
    my_data = [data_block.split("\n") for data_block in f.read().split("\n\n")]

if example_data:
    print(f"Example answer: {solve(example_data)}\n")
print(solve(my_data))
