
# The isalnum() method

# The parameterless method named isalnum() checks if the string contains only digits or alphabetical characters (letters), and returns True or False according to the result.

# Note: any string element that is not a digit or a letter causes the method to return False. An empty string does, too.

t = 'Six lambdas'
print(t.isalnum())  #False  -- Space in between

t = 'ΑβΓδ'
print(t.isalnum())  #True

t = '20E1'
print(t.isalnum())  #True

print("="*100)

# Demonstrating the isalnum() method:
print('lambda30'.isalnum())  #True
print('lambda'.isalnum())    #True
print('30'.isalnum())        #True
print('@'.isalnum())         #False -- Special character
print('lambda_30'.isalnum()) #False -- Underscrore
print(''.isalnum())          #False -- empty string
