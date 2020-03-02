# Strings


# a = 'hello\'\' python'
#
# print(a)
#
b = """
Line 1
Line 2
Line 3
"""

a = 'hello python'
print(a[0]) # == a[0:1] == a[:1]
print(a[len(a) - 1]) # == a[-1]
print(a[:]) # == a == a[0:len(a)] == a[::1]
print(a[2:]) # == a[2:len(a)]
print(a[:7]) # == a[0:7]
print(a[1:9])
print(a[1:9:3]) # [start_index:end_index:step]
print(a[::-1])

c = ' c++'
# d = a + c
# d = 'hello python {} {}'.format(c, 'java')
# d = 'hello python {0} {1}'.format(c, 'java')
d = 'hello python {cpp} {java}'.format(cpp=c, java='java')


print(len(d))


e = [1, 2, 3, 4, 5]
e.append(10)
e.pop()
print(e)


