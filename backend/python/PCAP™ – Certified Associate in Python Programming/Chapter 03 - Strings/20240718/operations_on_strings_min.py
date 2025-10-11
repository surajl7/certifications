# Operations on strings: min()

# Demonstrating min() - Example 1:
print()
string = "aAbByYzZ"
print("String: " + string)
print()
print("min value in string is -- " + min(string))
print()
print("ASCII values of characters in the string:")
for char in string:
    ascii_value = ord(char)
    print(f"ASCII value of '{char}' is: {ascii_value}")

print()

# Demonstrating min() - Examples 2:
t = 'The Knights Who Say "Ni!"'
print("String: " + t)
print()
print("min value in string is -- "+'[' + min(t) + ']')
print()
for char in t:
    ascii_value = ord(char)
    print(f"ASCII value of '{char}' is: {ascii_value}")
print()

# Demonstrating min() - Examples 3:
t = [0, 1, 2]
print(f"String: {t}")
print()
print(f"min value in string is -- {min(t)}")
print()
for char in t:
    ascii_value = ord(chr(char))
    print(f"ASCII value of '{char}' is: {ascii_value}")
print()