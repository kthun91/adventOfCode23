import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path, "r") as f:
    input = f.read().splitlines()
    rows = len(input)    
    columns = max(len(x) for x in input)
    machines = [[]]
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            char_array[i][j] = char
