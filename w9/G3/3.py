# Dictionaries / Objects / Maps

obj = {
    'id': '18BD0000',
    'name': 'Student',
    # 'age': 20
}

print(obj['name'])
print(obj.get('age', 18))
print(obj.keys())
print(obj.values())
print(obj.items())

name = obj.get('name')
# for i in range(len(name)):
#     print(name[i])


for el in name:
    # if el == 'd':
    if el in ['d', 'u', 't']:
        continue
    print(el)
