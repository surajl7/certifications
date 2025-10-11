# Strings vs. numbers
# There are two additional issues that should be discussed here: how to convert a number (an integer or a float) into a string, and vice versa. It may be necessary to perform such a transformation. Moreover, it's a routine way to process input/output data.

# The number-string conversion is simple, as it is always possible. It's done by a function named str().


itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)


si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)
