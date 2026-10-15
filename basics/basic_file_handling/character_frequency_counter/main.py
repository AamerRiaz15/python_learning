string1 = '325432p45234'
d = {}

for char in string1:
    d[char] = d.get(char, 0) + 1

print("---List 1---")
print(list(d.keys()))

min_value = min(d, key=d.get)
print("Least frequent character:", min_value)
