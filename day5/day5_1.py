import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def useMap(dest:int, source:int, offset:int, seed:int) -> list:
    if seed >= source and seed <= source + (offset ): 
        return [True, dest + (seed - source)] 
    return [False, seed]

with open(abs_file_path, "r") as f:
    seeds = []
    maps = []
    tmp = []
    res = []
    input = f.read().splitlines()
    for i, l in enumerate(input):
        j = 1
        if "seeds:" in l:
            _, seedInput = l.split(":")
            seeds = [int(s) for s in seedInput.split(" ") if s.isdigit()]
        if "map" in l:
            while input[i + j] != "":
                tmp.append([int(x) for x in input[i + j].split(" ")])
                j += 1
            maps.append(tmp)
            tmp = []

    for s in seeds:
        for m in maps:
            for z in m:
                if useMap(z[0], z[1], z[2], s)[0]:
                    s = useMap(z[0], z[1], z[2], s)[1]
                    break
        res.append(s)
    print(min(res))









