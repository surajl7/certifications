def even_odd(x):
    for i in x:
        if i % 2 == 0:
            yield "Even"
        yield "Odd"

num = [0, 1, 2, 3, 4, 5]
for i in even_odd(num):
    print(i, end = ' ')