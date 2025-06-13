import re

pattern = r"a.*b"
test_strings = ["ab", "acb", "axyzb", "a123b", "aXb", "abbb"]

for s in test_strings:
    print(f"{s}: {bool(re.fullmatch(pattern, s))}")


