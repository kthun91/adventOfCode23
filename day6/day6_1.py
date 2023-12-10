import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path, "r") as f:
    input = f.read().splitlines()
    _, inputNums = input[0].split(":")
    time = [int(s) for s in inputNums.split(" ") if s.isdigit()]
    _, inputNums = input[1].split(":")
    record = [int(s) for s in inputNums.split(" ") if s.isdigit()]
    
    # time 7
    # record dist 9
    # hold range(0,7 + 1) -> 0, 1, .., 7
    # speed = hold 
    # distance = speed * (time - hold)
    # if distance > record dist -> in array

    newRecords = []
    waysToWin = []
    for i in range(0, len(time)):
        for h in range(0, time[i] + 1):
            speed = h
            distance = speed * (time[i] - h)
            if distance > record[i]:
                newRecords.append(h)
        waysToWin.append(len(newRecords))
        newRecords = []

    print(waysToWin)

    res = 1
    for r in waysToWin:
        res *= r
    print(res)
    










