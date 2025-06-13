import re

text = "hello_world test_case snake_case"
matches = re.findall(r"[a-z]+_[a-z]+", text)

print(matches)