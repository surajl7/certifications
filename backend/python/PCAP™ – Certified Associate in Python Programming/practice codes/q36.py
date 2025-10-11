my_l = [[i+j for i in range(1,5,1)] for j in range(-1,6,3)]
my_p =[]
 
for l in my_l:
    for k in l:
        if k not in my_p:
            my_p.append(k)
 
print(my_p)