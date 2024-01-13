a = list(range(1, 11))
print(a)

b = [i ** 2 for i in a]
print(b)

c = [i ** 2 for i in a if i % 2 == 0]
print(c)

d = [i ** 2 if i % 2 == 0 else i ** 3 for i in a]
print(d)

e = [i ** 2 if i % 2 == 0 else i ** 3 for i in a if i % 3 == 0]
print(e)

f = {i: i ** 2 for i in a}
print(f)

g = {i: i ** 2 for i in a if i % 2 == 0}
print(g)

h = {i: i ** 2 if i % 2 == 0 else i ** 3 for i in a}
print(h)

i = {i: i ** 2 if i % 2 == 0 else i ** 3 for i in a if i % 3 == 0}
print(i)

j = (a[i - 1] if i % 2 == 0 else b[i - 1] for i in a)
print(*j)
