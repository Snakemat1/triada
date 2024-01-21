import re
dict = {
    'hello':'hi',
    'goodbye':'bye'
}

str = '123123123'
print(re.findall(r'\d\d\d',str))