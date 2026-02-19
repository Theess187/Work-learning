logs = ["ERROR", "INFO", "ERROR", "WARNING", "ERROR"]
def count_errors(logs):
    return logs.count("ERROR")

print(count_errors(logs))