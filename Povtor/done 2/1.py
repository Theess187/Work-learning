with open ("logs.txt") as f:
    for line in f:
        data = line.split()
        if len(data) >= 2 and data[1] == "ERROR" and data[0] == "2025-04-11":
            print(line)
    print("------------------")