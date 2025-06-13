import re

text = "Hello World ThisIsCorrect"
matches = re.findall(r"[A-Z][a-z]+", text)

print(matches)