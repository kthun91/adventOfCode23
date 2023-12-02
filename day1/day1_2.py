import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

numbers = {"one":"1",
           "two":"2", 
           "three":"3", 
           "four":"4", 
           "five":"5", 
           "six":"6", 
           "seven":"7", 
           "eight":"8", 
           "nine":"9"}

def getNumbers(line: str) -> str:
    tmp = ""
    first = ""
    last = ""
    for t in line:
        if first != "":
            break
        if t.isdigit():
            first = t
            tmp = ""
            break
        tmp += t
        for element in numbers.keys():
            if element in tmp:
                first = numbers[element]
                tmp = ""
                break
    for u in reversed(line):
        if last != "":
            break
        if u.isdigit():
            last = u
            break
        tmp = u + tmp
        for element in numbers.keys():
            if element in tmp:
                last = numbers[element]
                break
    return first + last

with open(abs_file_path, "r") as f:
    input = []
    for l in f.read().splitlines():
        input.append(int(getNumbers(l)))
    print(sum(input))
