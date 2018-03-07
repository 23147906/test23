#Author:Win_Li   23147
#Date:2018-01-11 23:18



import re

ret = re.search(r'<(?P<name_1>\w*)><(?P<name_2>\w*)>.*</(?P=name_2)></(?P=name_1)>', "<html><h1>古墓派掌门</h1></html>")

print(ret.group('name_1'))

print(ret)
# print(ret.group())

ret = re.match(r'.*\Bmupai','gumupai')

print(ret.group())
