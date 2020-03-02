# Dictionaries
product = {
    'id': 1,
    'name': 'Mac book',
    'price': 3000
}

print(product['name'])
print(product.get('name', 'mac book'))
print(product.keys())
print(product.values())
print(product.items())

# a = [11, 22123, 1233]
# for i in range(len(a)):
#     print(a[i])

# a = [11, 22123, 1233]
# for el in a:
#     print(el)

name = product.get('name')
new_name = ''
for i in name:
    if i == 'o':
        # print('*')
        new_name += '*'
        continue
    # print(i)
    new_name += i


print(new_name)


