import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def calcPoints(resSet:set) -> int:
    return pow(2, len(resSet) - 1)

def gettingResultSet(result:set) -> set:
    tmp, have = l.split("|")
    haveSet = set(have.split())
    _, win = tmp.split(":")
    winSet = set(win.split())
    return haveSet.intersection(winSet) 

with open(abs_file_path, "r") as f:
    input = []
    rSum = 0
    for l in f.read().splitlines():
        rSum += (int(calcPoints(gettingResultSet(l))))
    print(rSum)