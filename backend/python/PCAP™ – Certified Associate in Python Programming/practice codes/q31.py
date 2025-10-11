import functools

lis = [5, 7, 3, 1]

def Add(a,b):
    print('a: ', a)
    print('b: ', b)
    print()
    return a + b

print("Reduce 1: ", functools.reduce(lambda x,y : Add(x,y),lis))
lis = [5]
print("Reduce 2: ", functools.reduce(lambda x,y : Add(x,y), lis))