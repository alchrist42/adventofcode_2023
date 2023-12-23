from pathlib import Path
from collections import Counter
from utils import nbs
from queue import SimpleQueue

# low, high = 0, 0

class Module:
    low = 0
    high = 0

    def __init__(self, name, next_modules) -> None:
        self.name = name
        self.on = False
        self.out: list[str | Module] = next_modules
        self.input: dict[Module, bool] = {}

    def run(self, imp, **kwargs):
        if imp:
            Module.high += 1
        else:
            Module.low += 1
        # print(f"call {imp} {self.name}")
        return self.press(imp, **kwargs)
        
    def press(self, imp, **kwargs):
        return None

class ModuleFlipFlop(Module):
    def press(self, imp, **kwargs):
        if imp:
            return None
        self.on = not self.on
        return (self.on, self.out)
    
class ModuleConjunction(Module):
    def press(self, imp, prev):
        self.input[prev] = imp
        if all(self.input.values()):
            return (False, self.out)
        return (True, self.out)

class ModuleBroadcast(Module):
    def press(self, imp, **kwargs):
        return (imp, self.out)
    



# part 1
def solve(data: list[str]):
    res = 0
    modules_dct: dict[str, Module] = {}
    for line in data:
        input, output = line.split(" -> ")
        kind, name = input[0], input[1:]
        output = output.split(", ")
        if kind == "b":
            name = kind + name
            module = ModuleBroadcast(name, output)
        elif kind == "%":
            module = ModuleFlipFlop(name, output)
        elif kind == "&":
            module = ModuleConjunction(name, output)
        else:
            raise Exception()
        modules_dct[name] = module
    
    new_out_modules = set()
    for name, module in modules_dct.items():
        new_modules_lst = [n for n in module.out if n  not in modules_dct]
        new_out_modules.update(new_modules_lst)
    for mod_name in new_out_modules:
        modules_dct[mod_name] = Module(mod_name, [])
            
    for name, module in modules_dct.items():
        module.out = [modules_dct[n] for n in module.out]
        if isinstance(module, ModuleConjunction):
            for name2, module2 in modules_dct.items():
                if name in module2.out:
                    module.input[module2] = 0
    
    def press_buton():
        q = SimpleQueue()
        q.put((0, [modules_dct["broadcaster"]], None))

        while not q.empty():
            imp, modules, prev = q.get()
            for module in modules:
                ans = module.run(imp, prev=prev)
                if ans is not None and ans[1]:
                    next_imp, next_modules = ans
                    q.put((next_imp, next_modules, module))

        print(Module.high, Module.low)

    for _ in range(1000):
        press_buton()
        print()
    return Module.high * Module.low


# part 2



path = Path(__file__)
filename = path.name.rstrip(".py")

with open(f"{filename}_temp.txt") as f:
    example_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]
with open(f"{filename}.txt") as f:
    my_data = [line.rstrip("\n") for line in f.readlines() if line.rstrip()]

if example_data:
    print(f"Example answer: {solve(example_data)}\n")
# print(solve(my_data))
