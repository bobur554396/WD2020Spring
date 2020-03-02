# String

b = """
Line 1
Line 2
Line 3
"""

a = "hello' kbtu"
# a = [1, 2, 3, 4, 5, 4, 5, 6, 6, 6]
print(a[0]) # == a[:1] == a[0:1]
print(a[len(a) - 1])
print(a[-1])
print(a[:])  # == a
print(a[1:])  # == a[1:len(a)]  => [ 1;len(a) )
print(a[:4])  # == a[0:4]
print(a[1:9])
print(a[1:9:2])  # [start_index:end_index:step]
print(a[1:-1]) # == a[1:len(a) - 1]
print(a[::-1])

name = 'Bobur'
age = 20
# a = 'Hello ' + name
# a = 'Hello {}, {}'.format(name, 4)
# a = 'Hello {0}, {1}'.format(name, 4)
a = 'Hello {name}, {age}'.format(name=n, age=20)
# a = f'Hello {name}, {age}'

print(a)
