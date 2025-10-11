# Comparing strings
# Python's strings can be compared using the same set of operators which are in use in relation to numbers.

# Take a look at these operators - they can all compare strings, too:

# ==
# !=
# >
# >=
# <
# <=
# There is one "but" - the results of such comparisons may sometimes be a bit surprising. Don't forget that Python is not aware (it cannot be in any way) of subtle linguistic issues - it just compares code point values, character by character.

# The results you get from such an operation are sometimes astonishing. Let's start with the simplest cases.


# Two strings are equal when they consist of the same characters in the same order. By the same fashion, two strings are not equal when they don't consist of the same characters in the same order.

# Both comparisons give True as a result:

print('alpha' == 'alpha')
print('alpha' != 'Alpha')

print("="*100)

# The final relation between strings is determined by comparing the first different character in both strings (keep ASCII/UNICODE code points in mind at all times.)

# When you compare two strings of different lengths and the shorter one is identical to the longer one's beginning, the longer string is considered greater.

# Just like here:

print('alpha' < 'alphabet')

print("="*100)

# The relation is True.

# String comparison is always case-sensitive (upper-case letters are taken as lesser than lower-case).

# The expression is True:

print('beta' > 'Beta')

print("="*100)

# Comparing strings: continued
# Even if a string contains digits only, it's still not a number. It's interpreted as-is, like any other regular string, and its (potential) numerical aspect is not taken into consideration in any way.

# Look at the examples:

print('10' == '010')  # False
print('10' > '010')   # True
print('10' > '8')     # False
print('20' < '8')     # True
print('20' < '80')    # True

print("="*100)

print('10' == 10)     # False
print('10' != 10)     # True
print('10' == 1)      # False
print('10' != 1)      # True
print('10' > 10)      # TypeError exception

print("="*100)
