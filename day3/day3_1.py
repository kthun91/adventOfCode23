import os
import re

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def transformNumbers(machines: list) -> list:
    for _ in range(2): # pretty lazy
        for j, line in enumerate(machines):
            for _ in range(len(line)): # pretty lazy 
                for i,pos in enumerate(line):
                    if pos.isdigit():
                        # X right of Number
                        if len(line) != i+1:
                            if line[i+1] == "X":
                                line[i] = "X"
                        # X left of Number
                        if i != 0:
                            if line[i-1] == "X":
                                line[i] = "X"  
                        # X over Number
                        if j != 0:
                            if machines[j-1][i] == "X":
                                machines[j][i] = "X" 
                        # X under Number
                        if len(machines) != j+1:
                            if machines[j+1][i] == "X":
                                machines[j][i] = "X" 
                        # X diagonal to Number
                        if (
                            len(line) != i+1 and len(machines) != j+1 and machines[j+1][i+1] == "X" or
                            i != 0 and len(machines) != j+1 and machines[j+1][i-1] == "X" or
                            len(line) != i+1 and j != 0 and machines[j-1][i+1] == "X" or
                            i != 0 and j != 0 and machines[j-1][i-1] == "X" 
                        ):
                            machines[j][i] = "X" 

def transformArray(machines: list) -> list:
    transformNumbers(machines)
    return machines

with open(abs_file_path, "r") as f:
    input = f.read().splitlines()

    # sum up all numbers
    allNumbers = 0
    for l in input:
        allNumbers += sum([int(s) for s in re.findall(r'\d+', l)])

    # declare 2d-array
    rows = len(input)    
    columns = max(len(x) for x in input)
    machines = [[' ' for _ in range(columns)] for _ in range(rows)]

    # turn special chars to X
    for i, line in enumerate(input):
        for j, char in enumerate(line):
            if char != "." and not char.isdigit():
                machines[i][j] = "X"
                continue
            machines[i][j] = char

    # turn machines to X
    machines = transformArray(machines)

    # turn back to string and sum up non machines
    lineStr = ""
    result = 0
    for r in machines:
        for c in r:
            lineStr += c
        tmp = sum([int(s) for s in re.findall(r'\d+', lineStr)])
        result += tmp
        lineStr = ""

    print(allNumbers - result)
    