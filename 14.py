from pathlib import Path
from collections import Counter
from utils import nbs


# part 1
def solve(data: list[str]):
    res = 0
    data = [list(line) for line in data]
    for _ in range(10**10):
        moves = 0
        for row, line in enumerate(data):
            if not row:
                continue
            for col, ch in enumerate(line):
                if ch == "O" and data[row - 1][col] == ".":
                    data[row - 1][col], data[row][col] = "O", "."
                    moves += 1
        if not moves:
            break
    # print(*data, sep="\n")
    for i in range(1, len(data) + 1):
        res += i * sum(ch == "O" for ch in data[-i])
    return res


# part 2
def solve(data: list[str]):
    total_rounds = 1000000000
    interval = 300
    start_ind = 0
    res = 0
    data = [list(line) for line in data]

    def moving(line: list[str], revers=False):
        if revers:
            line = line[::-1]
        while True:
            moves = 0
            free = None
            for i, ch in enumerate(line):
                if ch == "#":
                    free = None
                elif ch == "." and free is None:
                    free = i
                elif ch == "O" and free is not None:
                    line[free], line[i] = "O", "."
                    free += 1
                    moves += 1
            if not moves:
                break
        if revers:
            line = line[::-1]
        return line
    
    lst_scores = []
    for round in range(total_rounds):
        # north
        for i in range(len(data[0])):
            line = [data[row][i] for row in range(len(data))]
            line = moving(line, revers=False)
            for row in range(len(data)):
                data[row][i] = line[row]
        # west
        for row, line in enumerate(data):
            line = moving(line)
            data[row] = line
        # south
        for i in range(len(data[0])):
            line = [data[row][i] for row in range(len(data))]
            line = moving(line, revers=True)
            for row in range(len(data)):
                data[row][i] = line[row]
        # east
        for row, line in enumerate(data):
            line = moving(line, revers=True)
            data[row] = line
    
        # print(*data, sep="\n", end="\n\n")
        score = 0
        for i in range(1, len(data) + 1):
            score += i * sum(ch == "O" for ch in data[-i])

        
        lst_scores.append(score)
        if len(lst_scores) % interval == 0:
            interval = int(interval * 1.2)
            start_ind = round
            print("update start_int and int", start_ind, interval)
        elif start_ind:
            if all(lst_scores[round - i] == lst_scores[start_ind - i] for i in range(42)):
                period = round - start_ind
                print(f"found period = {period}")
                period_lst = lst_scores[-period:]
                print(period_lst)
                print(lst_scores[-period * 2: -period])
                ans_ind = (total_rounds - round - 2) % period
                return period_lst[ans_ind]

                break

    for i in range(1, len(data) + 1):
        res += i * sum(ch == "O" for ch in data[-i])
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
