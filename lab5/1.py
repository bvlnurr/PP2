import re

pattern = r"ab*"
test_strings = ["a", "ab", "abbb", "ac", "b"]

for s in test_strings:
    print(f"{s}: {bool(re.fullmatch(pattern, s))}")