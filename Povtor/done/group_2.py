import re
with open("logs.txt") as f:
    data = f.readlines()
    # print(data)
    msg = {}
    for line in data:
        # print("Дата: " + line.split()[0] + ", Уровень: " + line.split()[1])
        # print(re.search(r"(ERROR|INFO|WARNING)\s+(.*)", line).group(2))
        if re.search(r"(ERROR|INFO|WARNING)\s+(.*)", line).group(2) not in msg:
            msg[re.search(r"(ERROR|INFO|WARNING)\s+(.*)", line).group(2)] = 1
        else:
            msg[re.search(r"(ERROR|INFO|WARNING)\s+(.*)", line).group(2)] += 1
    for key, value in msg.items():
        print(f"{key}: {value}")
   