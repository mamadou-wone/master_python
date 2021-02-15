def add(*args):
    sum = 0
    for n in args:
       sum += n
    return sum


# print(add(5, 4, 6, 8, 10))

def calculate(**kwargs):
    sum = 0
    for (key, value) in kwargs.items():
        sum += value
    print(sum)


calculate(add=3, multiply=5)