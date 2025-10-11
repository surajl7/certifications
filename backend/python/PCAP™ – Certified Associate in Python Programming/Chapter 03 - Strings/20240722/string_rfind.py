# The rfind() method
# The one-, two-, and three-parameter methods named rfind() do nearly the same things as their counterparts (the ones devoid of the r prefix), but start their searches from the end of the string, not the beginning (hence the prefix r, for right).

# Take a look at the example code in the editor and try to predict its output. Run the code to check if you were right.

# NOTE: We count the index from 0

# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta"))            #OUTPUT: 8
# This line of code searches for the substring "ta" in the string "tau tau tau" from right to left.
# Output: The method returns 8, which is the index of the last occurrence of "ta" in the string "tau tau tau".

print("="*100)

print("tau tau tau".rfind("ta", 9))         #OUTPUT: -1
# Here, rfind("ta", 9) specifies that the search starts from index 9 (inclusive) towards the beginning of the string.
# Output: Since the substring "ta" does not appear after index 9 in the string "tau tau tau", the method returns -1. This indicates that the substring was not found starting from index 9 or later.

print("="*100)

print("tau tau tau".rfind("ta", 3, 9))      #OUTPUT: 4
# In this case, rfind("ta", 3, 9) specifies a range where the search starts at index 3 (inclusive) and ends at index 9 (exclusive).
# Output: The method returns 4, which is the index of the last occurrence of "ta" within the substring " tau tau" (from index 3 to 8).

print("="*100)

string = "tau tau tau"
length = len(string)

# Iterate over the string
for i, char in enumerate(string):
    # Calculate the descending index
    desc_index = length - i - 1
    print(f"{char} = {desc_index}")