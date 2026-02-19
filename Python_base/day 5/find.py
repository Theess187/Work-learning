import re

target_date = "2025-04-10"
pattern = rf"ERROR\s+({target_date})\s+\d{{2}}:\d{{2}}:\d{{2}}\s+(.*)"

with open("app.log", "r", encoding="utf-8") as log:
    for line in log:
        match = re.search(pattern, line)
        if match:
            message = match.group(2)
            print(message)