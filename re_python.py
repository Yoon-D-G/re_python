import re

test_string = 'abc123o98er!!??>,'

pattern = re.compile(r"abc")
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
