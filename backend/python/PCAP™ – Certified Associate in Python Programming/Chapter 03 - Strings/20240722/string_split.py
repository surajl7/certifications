# The split() method
# The split() method does what it says - it splits the string and builds a list of all detected substrings.

# The method assumes that the substrings are delimited by whitespaces - the spaces don't take part in the operation, and aren't copied into the resulting list.

# If the string is empty, the resulting list is empty too.

# Look at the code in the editor. The example produces the following output:

# Note: the reverse operation can be performed by the join() method.

# Demonstrating the split() method:

string  = "phi       chi\npsi"

str_split = string.split()

print(str_split)

print(' '.join(str_split))
