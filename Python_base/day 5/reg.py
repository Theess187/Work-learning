import re

log = "INFO 2025-04-10 11:16:15 Service started"

pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
pattern2 = r"(INFO|ERROR|WARNING)"
pattern3 = r"(INFO|ERROR|WARNING)\s+(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(.*)"
# match = re.search(pattern, log)
# if match:
#     # print(help(re.search))
#     # print(help(match.group))
#     print("Found timestamp:", match.group())

# match2 = re.search(pattern2, log)
# if match2:
#     print("Found log level:", match2.group())

match3 = re.search(pattern3, log)
if match3:
    print("Log Level:", match3.group(1))
    print("Timestamp:", match3.group(2))
    print("Message:", match3.group(3))