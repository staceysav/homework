import re

my_file = open('addresses.txt', 'r')
data = my_file.read()

result = re.findall(r'([0-9]{3,4}\s.+\n.+\n.+)', data)
# print(result)
for i in result:
    print(i, '\n')