# The islower() method
# The islower() method is a fussy variant of isalpha() – it accepts lower-case letters only.

# Example 1: Demonstrating the islower() method:
print("Moooo".islower())  #False -- contains uppercase
print('moooo'.islower())  #True

print("="*100)

# The isspace() method
# The isspace() method identifies whitespaces only – it disregards any other character (the result is False then).

# Example 2: Demonstrating the isspace() method:
print(' \n '.isspace())             #True -- newline charater can be neglected
print(" ".isspace())                #True
print("mooo mooo mooo".isspace())   #False -- contains charater string

print("="*100)

# The isupper() method
# The isupper() method is the upper-case version of islower() – it concentrates on upper-case letters only.

# Example 3: Demonstrating the isupper() method:
print("Moooo".isupper())    #False -- contains lowercase charaters
print('moooo'.isupper())    #False -- contains lowercase charaters
print('MOOOO'.isupper())    #True

print("="*100)
