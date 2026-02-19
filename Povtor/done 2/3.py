def count_logs(filename, level):
    count = 0
    try:
        with open(filename) as f:
            for line in f:
                parts = line.strip().split()

                if len(parts) >= 2 and parts[1] == level:
                    count += 1

        return count
    except FileNotFoundError:
        print(f"File {filename} not found.")
        

print(count_logs("log.txt", "ERROR"))

# print("ERRORS:",count_logs("logs.txt", "ERROR"))