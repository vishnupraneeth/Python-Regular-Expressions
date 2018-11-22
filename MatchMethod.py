import re
st="vishnu is there"
result=re.match(r"vishnu",st)
print(result.group(0))
# r1=re.findall(r"^\w+",st)
# print(r1)

# m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
# print(m.group(0))