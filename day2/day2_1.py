import os
import re

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

colors = {"red":12, "green":13, "blue":14}

# max 12 red, 13 green, 14 blue
def gamePossible(line:str) -> int:
    gameID, cubes = line.split(":")
    _, iD = gameID.split(" ")

    for c in colors.keys():
        pattern = r'(\d+)(\s*' + c + r')'
        match = re.findall(pattern, cubes)

        for m in match:
            if int(m[0]) > colors[c]:
                return 0
    return iD

with open(abs_file_path, "r") as f:
    input = []
    for l in f.read().splitlines():
        input.append(int(gamePossible(l)))
    print(sum(input))
