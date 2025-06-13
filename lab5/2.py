import re

pattern = r"ab{2,3}"
test_strings = ["abb", "abbbb", "ab", "a"]

for s in test_strings:
    print(f"{s}: {bool(re.fullmatch(pattern, s))}")