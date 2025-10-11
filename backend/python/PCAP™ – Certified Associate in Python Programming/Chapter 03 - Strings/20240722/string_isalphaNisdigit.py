
# The isalpha() method
# The isalpha() method is more specialized - it's interested in letters only.

# Example 1: Demonstrating the isapha() method:
print("Moooo".isalpha())  #True
print('Mu40'.isalpha())   #False -- contains number

print("="*100)

# The isdigit() method
# In turn, the isdigit() method looks at digits only - anything else produces False as the result.

# Example 2: Demonstrating the isdigit() method:
print('2018'.isdigit())         #True
print("Year2019".isdigit())     #False -- contains charaters