import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path, "r") as f:
    input = f.read().splitlines()
    _, inputNums = input[0].split(":")
    tmp = ""
    for n in [s for s in inputNums.split(" ") if s.isdigit()]:
        tmp += n
    time = int(tmp)

    _, inputNums = input[1].split(":")
    tmp = ""
    for n in [s for s in inputNums.split(" ") if s.isdigit()]:
        tmp += n
    record = int(tmp)
    
    # time 7
    # record dist 9
    # hold range(0,7 + 1) -> 0, 1, .., 7
    # speed = hold 
    # distance = speed * (time - hold)
    # if distance > record dist -> in array

    newRecords = []

    for h in range(0, time + 1):
        speed = h
        distance = speed * (time - h)
        if distance > record:
            newRecords.append(h)
    print(len(newRecords))

    










