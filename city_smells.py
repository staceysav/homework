import string

f = open("city_smells.txt", 'r')
data = f.read()

data = data.lower() #lower case

data1 = data.translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~«»')) #переменная без пунктуации

# print(data)

data2 = data1.split()
# 1. определить среднюю длину слова в тексте
s = 0 #переменная для суммы
for i in data2:
    s = s + len(i)
print(s)
l = len(data2)
print(l)
result1 = s / l
print("средняя длина слова: ", result1)

#  5. количество уникальных слов и пророрция общему количеству слов в тексте
unique = set(data2)
print('количество уникальных слов:', len(unique))
print('пророрция общему количеству слов:', len(unique)/len(data2))
