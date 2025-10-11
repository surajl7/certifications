def func(x,y):
    return x/(y-4)
 
try:
    print(func(x=1,4))
except ArithmeticError:
    print("ArithmeticError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("Misc. Error")