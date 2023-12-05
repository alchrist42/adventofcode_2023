from pathlib import Path
from collections import Counter
from utils import nbs
from bisect import bisect


# part 1
def solve(data: list[str]):
    res = 100000000000000000
    dct = {}
    for line in data[1:]:
        if line[0].isalpha():
            val_dct = {}
            name_dict = line.rstrip(" :")
            dct[name_dict] = val_dct
            continue
        st_soil, left, rang = map(int, line.split())
        right = left + rang
        shift = st_soil - left
        val_dct[(left, right)] = shift
    print(dct)
    seeds = map(int, data[0].split(":")[1].split())
    for seed in seeds:
        loc = 100000000000000
        for name, val_dct in dct.items():
            for (left, right), shift in val_dct.items():
                if left <= seed < right:
                    seed = seed + shift
                    break
            else:
                val = seed

            # print(seed, name, loc, val_dct)
        res = min(res, seed)


    return res


# part 2


    

def solve(data: list[str]):

    def split_ranges(name: str, pairs: list[list[int]]) -> list[list[int]]:
        ans = []
        val_dct = dct[name]
        lst_val = dct_lst[name]
        for start, end in pairs:
            # start_ind = bisect(lst_val, (start , 0))
            # end_ind = bisect(lst_val, (end, float("inf")))
            # keys = lst_val[start_ind: end_ind]
            for left, right in lst_val:
                shift = val_dct[(left, right)]
                if start >= end:
                    break
                if start < left:
                    ans.append((start, min(end, left)))
                    start = min(end, left)
                elif left <= start <= right:
                    ans.append((start + shift, min(end, right) + shift))
                    start = min(end, right)
                elif start >= right:
                    continue
            if start < end:
                ans.append((start, end))
        return sorted(ans)

    res = 100000000000000000
    dct = {}
    for line in data[1:]:
        if line[0].isalpha():
            val_dct = {}
            name_dict = line.rstrip(" :")
            dct[name_dict] = val_dct
            continue
        st_soil, left, rang = map(int, line.split())
        right = left + rang
        shift = st_soil - left
        val_dct[(left, right)] = shift
    seeds = map(int, data[0].split(":")[1].split())

    dct_lst = {}
    for name, val_dct in dct.items():
        dct_lst[name] = sorted(list(val_dct.keys()))

    seeds = list(map(int, data[0].split(":")[1].split()))
    cnt_seed = 0
    for i in range(0, len(seeds), 2):
        start, rang = seeds[i:i + 2]
        pairs = [(start, start + rang)]
        for name in dct:
            pairs = split_ranges(name, pairs)
        local_min = min(start for start, end in pairs)
        res = min(local_min, res)
        cnt_seed += 1

        print(cnt_seed)
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
