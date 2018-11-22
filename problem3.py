#Return the domain name of given email id's vishnu@gmail.com python@yahoo.com java@google.in
import re
result=re.findall(r"@\w*.\w+","vishnu@gmail.com python@yahoo.com java@google.in")
print(result)

res=re.findall(r"@\w*.(\w*)"  ,"vishnu@gmail.com python@yahoo.com java@google.in")
print(res)