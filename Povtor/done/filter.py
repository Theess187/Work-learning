with open ("logs.txt") as f:
    data = f.readlines()
    for line in data:
        if line.strip().split()[1]=="ERROR":
            print(line.strip())
    print()