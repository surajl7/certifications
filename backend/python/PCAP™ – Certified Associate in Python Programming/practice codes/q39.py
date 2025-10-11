# f = open("myfile.txt", "at")
# for i in range(1,11):
#     f.write('Line #' + str(i) + '\n')
# f.seek(0)
# print(f.readline(10))
# f.close()

f = open("myfile2.txt", "a+t")
for i in range(1,11):
    f.write('Line #' + str(i) + '\n')
f.seek(0)
print(f.readline(10))    # Line #1
f.close()     