# Return first 2 characters of each word in the string

import re
s1="HI This is regular expressions topic"
res=re.findall(r"\b\w{2}",s1)
print(res)
