name = "mamadou"
inv = ''

for i in range(len(name), 0, -1):
    inv += name[i - 1]

print(inv)