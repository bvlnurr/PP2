import re

text = "InsertSpaceBetweenWords"
result = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

print(result)