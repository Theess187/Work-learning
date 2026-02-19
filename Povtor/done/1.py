import re
with open ("logs.txt") as f:
    data = f.readlines()
    # print(data)
    # print(f"Number of lines: {len(data)}")
    # print(f"Number of ERRORs: {len(re.findall('ERROR', str(data)))}")
    # print(f"Number of INFOs: {len(re.findall('INFO', str(data)))}")
    info = 0
    err = 0
    count = 0
    stats = {
    "2025-04-10": 0,
    "2025-04-11": 0
    }
    date1 = "2025-04-10"
    date2 = "2025-04-11"
    for line in data:
        if line.startswith("2025-04-10"):
            stats["2025-04-10"] += 1
        elif line.startswith("2025-04-11"):
            stats["2025-04-11"] += 1
    # print(f"Number of lines starting with {date1}: {stats[date1]}")
    # print(f"Number of lines starting with {date2}: {stats[date2]}")
    print(stats)
    # for n in data:
    #     if "ERROR" in n:
    #         err += 1
    # print(f"Number of ERRORs: {err}")

    # for i in data:
    #     if "INFO" in i:
    #         info += 1
    # print(f"Number of INFOs: {info}")

    # for line in data:
    #     if line.startswith(date):
    #         # print(line.strip())
    #         count += 1
    # print(f"Number of lines starting with {date}: {count}")

