from pathlib import Path
from collections import Counter, defaultdict
from utils import nbs
from functools import lru_cache
from itertools import product

from multiprocessing import Process, Queue, cpu_count, set_start_method


# r_dct = dict()

def create_function(function_name, function_code):
    # function_string = f"@lru_cache\ndef {function_name}_my(x=0, m=0, a=0, s=0):\n    {function_code}"
    function_string = f"def {function_name}_my(r_dct, x=0, m=0, a=0, s=0):\n    {function_code}"
    # print(f"created:\n{function_string}")
    exec(function_string)
    return_value = eval(function_name + "_my")
    return return_value



# part 1
def solve(data: list[str]):
    res = 0
    i = data.index("")
    rules_lst, items = data[:i], data[i+1:]

    global r
    r["A"] = create_function("A", "return True")
    r["R"] = create_function("R", "return False")

    for line in rules_lst:
        key, rules = line.split("{")
        rules = rules.rstrip("}").split(",")
        lst = []
        func_code = ""
        func_code = f"print(f'call {key}" + " {(x, m, a, s)}')\n    "
        func_code = f"global r\n    "

        for rule in rules:
            if ":" in rule:
                e, key_next = rule.split(":")
                lst.append((e, key_next))
                func_code += f"if {e}:\n        return r['{key_next}'](r, x, m, a, s)\n    "
            else:
                func_code += f"return r['{rule}'](r, x, m, a, s)\n"
        r[key] = create_function(key, func_code)

    first_f = "in"
    print(first_f)

    for n_r, item in enumerate(items):
        x, m, a, s = [int(s.split("=")[1]) for s in item.strip("{}").split(",")]
        ans_f = r[first_f](r, x, m, a, s)
        print(f"row={n_r}: {ans_f} ()", x, m, a, s, "\n")
        if ans_f:
            res += x + m + a + s
    return res


# part 2
def heavy(r_dct, dct, q, slice_start, slice_stop):
    dct["x"] = dct["x"][slice_start:slice_stop]
    total = 1
    for x in dct.values():
        total *= len(x)
    print("total ", total)
    res = 0
    goal = 0
    passed = 0
    for diaps in product(*dct.values()):
        passed += 1
        kwargs = {ch: diap[0] for ch, diap in zip("xmas", diaps)}
        if r_dct['in'](r_dct, **kwargs):
            count = 1
            for diap in diaps:
                count *= diap[1] - diap[0] + 1
            res += count
        if passed > goal:
            print(slice_start, int(goal / total * 100), "%")
            goal += total / 10
    print(f"ended proc for range {slice_start, slice_stop}\n{res}")
    q.put(res)

def solve(data: list[str]):
    res = 0
    i = data.index("")
    rules_lst, items = data[:i], data[i+1:]

    r_dct = {}
    r_dct["A"] = create_function("A", "return True")
    r_dct["R"] = create_function("R", "return False")

    dct = {ch: [[1, 4000],] for ch in "xmas"}

    for line in rules_lst:
        key, rules = line.split("{")
        rules = rules.rstrip("}").split(",")

        func_code = f"print(f'call {key}" + " {(r_dct, x, m, a, s)}')\n    "
        # func_code = f"global r_dct\n    "
        func_code = f""

        for rule in rules:
            # create func
            if ":" in rule:
                exp, key_next = rule.split(":")
                func_code += f"if {exp}:\n        return r_dct['{key_next}'](r_dct, x, m, a, s)\n    "

                # split inpout border data for cache
                ch, eq, val = exp[0], exp[1], int(exp[2:])
                lst = dct[ch]
                for i, diap in enumerate(lst):
                    l, r = diap
                    if l <= val <= r:
                        if eq == "<" and val != l:
                            new_diap = [[l, val - 1], [val, r]]
                        elif eq == ">" and val != r:
                            new_diap = [[l, val], [val + 1, r]]
                        else:
                            break
                        lst.pop(i)
                        lst.extend(new_diap)
                        break
            else:
                func_code += f"return r_dct['{rule}'](r_dct, x, m, a, s)\n"
            
            
                
        r_dct[key] = create_function(key, func_code)


    q = Queue()
    processes = []
    n_proc = cpu_count()
    print("procceses count", n_proc)
    range_x = len(dct["x"]) // n_proc
    dx = [(range_x * i, range_x * (i + 1))  for i in range(n_proc)]
    for proc in range(n_proc):
        p = Process(target=heavy, args=(r_dct, dct, q, *dx[proc]))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
        
    while not q.empty():
        res += q.get()


    return res

def main():
    r_dct = {}
    path = Path(__file__)
    filename = path.name.rstrip(".py")

    with open(f"{filename}_temp.txt") as f:
        example_data = [line.rstrip("\n") for line in f.readlines()]
    with open(f"{filename}.txt") as f:
        my_data = [line.rstrip("\n") for line in f.readlines()]

    if example_data:
        print(f"Example answer: {solve(example_data)}\n")
    print(solve(my_data))
        
if __name__ == '__main__':
    main()
