# Sorting
# Comparing is closely related to sorting (or rather, sorting is in fact a very sophisticated case of comparing).

# This is a good opportunity to show you two possible ways to sort lists containing strings. Such an operation is very common in the real world - any time you see a list of names, goods, titles, or cities, you expect them to be sorted.

# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()

# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)