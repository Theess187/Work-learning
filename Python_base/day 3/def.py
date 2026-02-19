logs = ["ERROR", "INFO", "ERROR", "WARNING", "ERROR"]

def count_errors(logs):
    count = 0
    for log in logs:
        if log == "ERROR":
            count += 1
    return count

print("Total ERRORs:", count_errors(logs))