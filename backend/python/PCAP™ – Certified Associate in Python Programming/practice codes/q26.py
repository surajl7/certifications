False == True
i = 0
while True:
    print("Python")
    if i > 5:
        break
    i += 1

'''
Iteration | i Value | i > 5	| Printed	| Next i Value
--------------------------------------------------------
1	      | 0       | False	| Python	| 1
2	      | 1       | False	| Python	| 2
3	      | 2       | False	| Python	| 3
4	      | 3       | False	| Python	| 4
5	      | 4       | False	| Python	| 5
6	      | 5       | False	| Python	| 6
7	      | 6       | True	| Python	| Loop breaks
'''