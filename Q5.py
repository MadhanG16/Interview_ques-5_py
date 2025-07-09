# Expand character+number pattern

import re

def expand_pattern(s):
    parts = re.findall(r'[a-zA-Z]\d+', s)
    result = ""
    for part in parts:
        char = part[0]
        count = int(part[1:])
        result += char * count
    return result

print(expand_pattern("a1b10"))
print(expand_pattern("b3c6d15"))     
