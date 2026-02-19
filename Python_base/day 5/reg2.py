import re

text = "ERROR 500 Database timeout"
match = re.search(r"\d{3}", text)

print(match.group())
