import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path, "r") as f:
    input = []
    for l in f.read().splitlines():
        input.append(l)
    first = ""
    last = ""
    num = 0

    for e in input:
        for v in e:
            if v.isdigit():
                first = v
                break
        for h in reversed(e):
            if h.isdigit():
                last = h
                break
        num += int(first + last)
    print(num)
