def Add(x):
    print("ADD: ", end = "")
    for i in x:
        print(i+50, end = " ")

def Minus(x):
    print("MINUS: ", end = "")
    for i in x:
        print(i-50, end = " ")

num = [10, 20, 30, 40, 50]
obj = reversed(num)
print(obj)
Add(obj)
print()
Minus(obj)