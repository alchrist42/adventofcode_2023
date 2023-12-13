from pathlib import Path
from collections import Counter
from utils import nbs

# part 1
def solve(data: list[str]):
    res = 0

    def rec(s: str, cnt_s: int, cnt_h: int, ns):
        if cnt_h == 0 and not ns:
            return 1
        if cnt_s + cnt_h < sum(ns):
            return 0
        if cnt_h > sum(ns):
            return 0
        gr = 0
        for i, ch in enumerate(s):
            if ch == ".":
                if not gr:
                    continue
                else:
                    if gr != ns[0]:
                        return 0
                    return rec(s[i+1:], cnt_s, cnt_h - gr, ns[1:])
            elif ch == "#":
                gr += 1
                if gr > ns[0]:
                    return 0
            elif ch == "?":
                ans1 = rec(s[:i] + "#" + s[i+1:], cnt_s - 1, cnt_h + 1, ns)
                ans2 = rec(s[:i] + "." + s[i+1:], cnt_s - 1, cnt_h, ns)
                return ans1 + ans2
        if len(ns) == 1 and ns[0] == gr:
            return 1
        return 0
            
    for i, line in enumerate(data):
        s, ns = line.split()
        s = "?".join([s for _ in range(5)])
        ns = list(map(int, ns.split(","))) * 5
        cnt_s = s.count("?")
        cnt_h = s.count("#")
        lres = rec(s, cnt_s, cnt_h, ns)
        print(f"{round(i/len(data) * 100, 2)}%", s, ns, lres)
        res += lres

    return res


# part 2

def solve(data: list[str]):
    res = 0

    def rec(s: str, cnt_s: int, cnt_h: int, ns):
        if cnt_h == 0 and not ns:
            return 1
        if cnt_s + cnt_h < sum(ns):
            return 0
        if cnt_h > sum(ns):
            return 0

        ans = 0
        n = ns[-1]
        gr = 0
        for i, ch in enumerate(s):
            if ch == ".":
                if not gr:
                    continue
                else:
                    if gr != ns[0]:
                        return 0
                    return rec(s[i+1:], cnt_s, cnt_h - gr, ns[1:])
            elif ch == "#":
                gr += 1
                if gr > ns[0]:
                    return 0
            elif ch == "?":
                ans1 = rec(s[:i] + "#" + s[i+1:], cnt_s - 1, cnt_h + 1, ns)
                ans2 = rec(s[:i] + "." + s[i+1:], cnt_s - 1, cnt_h, ns)
                return ans1 + ans2
        if len(ns) == 1 and ns[0] == gr:
            return 1
        return 0

    def calc_left_border(grs, ns):
        starts = [0] * len(ns)
        i = j = 0
        for n_ind, n in enumerate(ns):
            while i < len(grs):
                if grs[i] -j >= n: # enought place
                    starts[n_ind] = (i, j)
                    j += n + 1
                    break
                i += 1
                j = 0
            if i == len(grs):
                return None
        return starts



            
    for i, line in enumerate(data):
        s, ns = line.split()
        s = "?".join([s for _ in range(5)])
        ns = list(map(int, ns.split(","))) * 5
        cnt_s = s.count("?")
        cnt_h = s.count("#")

        grs = []
        group = 0
        for i, ch in enumerate(line):
            if ch in "#?":
                group += 1
            elif group:
                grs.append(group)
                group = 0
        if group:
            grs.append(group)
            
        lres = rec(s, cnt_s, cnt_h, ns)
        print(f"{round(i/len(data) * 100, 2)}%", s, ns, lres)
        res += lres

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
