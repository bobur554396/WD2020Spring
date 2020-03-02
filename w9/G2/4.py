a = 'hello'

# for el in a:
#     if el == 'l':
#         print('*')
#         continue
#     print(el)

for i in range(len(a)):
    # print(i)
    if a[i] == 'l':
        print('*')
        continue
    print(a[i])
