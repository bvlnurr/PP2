import re

text = "Python is great. Really great"
result = re.sub(r"[ ,.]", ":", text)

print(result)