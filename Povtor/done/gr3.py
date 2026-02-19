with open ("logs.txt", "r") as f:
    stats = {
    "timeout": 0,
    "disk": 0,
    "other": 0
    }

    for line in f:
        if line.split()[1] == "ERROR":
            if "timeout" in line.lower():
                stats["timeout"] += 1
                # print(line.lower()+"timeout")
            elif "disk" in line.lower():
                stats["disk"] += 1
                # print(line.lower()+"disk")
            else:
                stats["other"] += 1
                # print(line.lower()+"other")
    for key, value in stats.items():
        print(f"{key}: {value}")    
