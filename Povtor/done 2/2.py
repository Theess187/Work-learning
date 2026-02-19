# stats = {}
# with open ("logs.txt") as f:
#     for line in f:
#         data = line.split()
#         if len(data) >= 2:
#             stats[data[1]] = stats.get(data[1], 0) + 1
#     print(stats)
#     print("------------------")
errors = {}
with open("logs.txt") as f:
    lines = f.readlines()
    for line in lines:
        parts = line.strip().split()

        if len(parts) >= 3 :
            error_text = " ".join(parts[2:])
            errors[error_text] = errors.get(error_text, 0) + 1

    for x, y in errors.items():
        print(f"{x}: {y}")