import os
from math import lcm

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path, "r") as f:
    input = f.read().splitlines()
    directions = [1 if s == "R" else 0 for s in input[0]]
    maps = dict()

    for l in input[2:]:
        key, values = l.split(" = ")
        val1 = values[1:4]
        val2 = values[6:9]
        maps[key] = [val1, val2]

    # get start nodes
    startnodes = []
    endnodes = []
    for x in maps.keys():
        if x[2] == "A":
            startnodes.append(x)
        if x[2] == "Z":
            endnodes.append(x)
    print(startnodes)

    # way too slow
    # tmp = "AAA"
    # counter = 0
    # while tmp != "ZZZZ":
    #     for i, s in enumerate(startnodes):
    #         startnodes[i] = maps[s][directions[counter % len(directions)]]
    #     if len(set(startnodes).difference(set(endnodes))) == 0:
    #         tmp = "ZZZZ"
    #     counter += 1
    # print(counter)

    # get lcm of first results
    res = []
    for s in startnodes:
        counter = 0
        while s != "ZZZZ":
            s = maps[s][directions[counter % len(directions)]]
            counter += 1
            if s in endnodes:
                s = "ZZZZ"
        res.append(counter)
    print(res)

    # lcm
    solution = res[0]
    for r in res:
        solution = lcm(r, solution)
    print(solution)

