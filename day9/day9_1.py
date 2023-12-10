import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def forecast(nums:list) -> int:
    # liste von listen erstellen
    tmpList = []
    resList = []
    tmpList.append(nums)
    resList.append(nums)
    while not sum([0 if e == 0 else 1 for e in tmpList]):
        resList.append(tmpList)
        tmpList = []
        # generate new tmpList with diffs 
    return 0

with open(abs_file_path, "r") as f:
    input = f.read().splitlines()
    res = []
    for l in input:
        nums = [int(s) for s in l.split(" ")]
        res.append(forecast(nums))
    print(sum(nums))

 