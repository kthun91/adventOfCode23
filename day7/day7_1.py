import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path, "r") as f:
    input = f.read().splitlines()
    directions = [1 if s == "R" else 0 for s in input[0]]
    print(directions)
    maps = dict()

    for l in input[2:]:
        key, values = l.split(" = ")
        val1 = values[1:4]
        val2 = values[6:9]
        maps[key] = [val1, val2]
    print(maps)

    tmp = "AAA"
    counter = 0
    while tmp != "ZZZ":
        tmp = maps[tmp][directions[counter % len(directions)]]
        counter += 1
    print(counter)