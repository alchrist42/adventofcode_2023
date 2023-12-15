from pathlib import Path
from collections import Counter, defaultdict
from utils import nbs


# part 1
def solve(data: list[str]):
    res = 0
    

    def my_hash(s):
        ans = 0
        for ch in s:
            ans += ord(ch)
            ans *= 17
            ans %= 256
        return ans

    hashes = data[0].split(",")
    for h in hashes:
        lres = my_hash(h)
        res += lres

    return res

# part 2
def solve(data: list[str]):
    res = 0
    dct = defaultdict(dict)

    def my_hash(s):
        ans = 0
        s = s.split("-")[0]
        s = s.split("=")[0]
        print(s, end = ": ")
        for ch in s:
            ans += ord(ch)
            ans *= 17
            ans %= 256
        return ans


    hashes = data[0].split(",")
    for h in hashes:
        key_h = my_hash(h)
        
        if "=" in h:
            key, val = h.split("=")
            dct[key_h][key] = val
        else:
            key = h.rstrip("-")
            dct[key_h].pop(key, None)

    print(dct)
    for box, lens in dct.items():
        for slot, focal in enumerate(lens.values()):
            lres = (box + 1) * (slot + 1) * int(focal)
            # print(box, lens, slot, focal, "ans",  lres)
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
