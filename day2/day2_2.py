import os
import re

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

# max r*g*b
def gamePossible(line:str) -> int:
    colors = {"red":0, "green":0, "blue":0}
    for c in colors.keys():
        pattern = r'(\d+)(\s*' + c + r')'
        match = re.findall(pattern, line)
        for m in match:
            if colors[c] < int(m[0]):
                colors[c] = int(m[0])
        
    return colors["red"] * colors["green"] * colors["blue"]

with open(abs_file_path, "r") as f:
    input = []
    for l in f.read().splitlines():
        input.append(gamePossible(l))
    print(sum(input))
