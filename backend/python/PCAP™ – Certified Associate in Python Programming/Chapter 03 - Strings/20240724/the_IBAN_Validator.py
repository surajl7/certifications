# The fourth program implements (in a slightly simplified form) an algorithm used by European banks to specify account numbers. The standard named IBAN (International Bank Account Number) provides a simple and fairly reliable method for validating account numbers against simple typos that can occur during rewriting of the number, for example, from paper documents, like invoices or bills, into computers.

# You can find more details here: https://en.wikipedia.org/wiki/International_Bank_Account_Number.

# IBAN Validator.

# TEST EXAMPLES
# British: GB72 HBZU 7006 7212 1253 00
# French: FR76 30003 03620 00020216907 50
# German: DE02100100100152517108

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")
