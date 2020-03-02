# a = [1, 2, 3, 4, 5, 5, 6, 6, 7, 7]
a = 'hello kbtu'
# print(a[2])
# print(len(a))
# print(a[len(a) - 1])
# print(a[-2])
# print(a[:])
print(a[2:])  # == print(a[2:len(a)])
print(a[:3])  # == print(a[0:3])
print(a[1:9])
# [start_index:end_index:step]
print(a[1:9:2])

b = "Lena's book"
print(b)

c = """
Line 1
line 2
line 3
"""
d = 'foo'
print(d[0])
print(d[:1])

e = 'hello {name} {age}'.format(name='Student 1', age=18)
print(e)

f = [1, 2, 3, 4]
f.append(5)
f.pop()
print(f)
