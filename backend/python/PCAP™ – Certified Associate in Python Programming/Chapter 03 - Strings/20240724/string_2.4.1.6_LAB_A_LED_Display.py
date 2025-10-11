# Scenario
# You've surely seen a seven-segment display.

# It's a device (sometimes electronic, sometimes mechanical) designed to present one decimal digit using a subset of seven segments. If you still don't know what it is, refer to the following Wikipedia article.

# Your task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.

# Each digit is constructed from 13 LEDs (some lit, some dark, of course) - that's how we imagine it:

#   # ### ### # # ### ### ### ### ### ### 
#   #   #   # # # #   #     # # # # # # # 
#   # ### ### ### ### ###   # ### ### # # 
#   # #     #   #   # # #   # # #   # # # 
#   # ### ###   # ### ###   # ### ### ###

# Note: the number 8 shows all the LED lights on.

# Your code has to display any non-negative integer number entered by the user.

# Tip: using a list containing patterns of all ten digits may be very helpful.

def display_digit(digit):
    # patterns = {
    #     '0': ["###", "# #", "# #", "# #", "###"],
    #     '1': ["  #", "  #", "  #", "  #", "  #"],
    #     '2': ["###", "  #", "###", "#  ", "###"],
    #     '3': ["###", "  #", "###", "  #", "###"],
    #     '4': ["# #", "# #", "###", "  #", "  #"],
    #     '5': ["###", "#  ", "###", "  #", "###"],
    #     '6': ["###", "#  ", "###", "# #", "###"],
    #     '7': ["###", "  #", "  #", "  #", "  #"],
    #     '8': ["###", "# #", "###", "# #", "###"],
    #     '9': ["###", "# #", "###", "  #", "###"]
    # }

    patterns = {
        '0': ["###", 
              "# #", 
              "# #", 
              "# #", 
              "###"],

        '1': ["  #", 
              "  #", 
              "  #", 
              "  #", 
              "  #"],

        '2': ["###", 
              "  #", 
              "###", 
              "#  ", 
              "###"],

        '3': ["###", 
              "  #", 
              "###", 
              "  #", 
              "###"],

        '4': ["# #", 
              "# #", 
              "###", 
              "  #", 
              "  #"],

        '5': ["###", 
              "#  ", 
              "###", 
              "  #", 
              "###"],

        '6': ["###", 
              "#  ", 
              "###", 
              "# #", 
              "###"],

        '7': ["###", 
              "  #", 
              "  #", 
              "  #", 
              "  #"],

        '8': ["###", 
              "# #", 
              "###", 
              "# #", 
              "###"],

        '9': ["###", 
              "# #", 
              "###", 
              "  #", 
              "###"]
    }
    
    return patterns.get(digit, [])

def display_number(number):
    digits = [display_digit(digit) for digit in number]
    
    for i in range(5):  # 5 rows for each digit pattern
        print(" ".join([digits[j][i] for j in range(len(number))]))

# Input handling
if __name__ == "__main__":
    number = input("Enter a non-negative integer number: ").strip()
    display_number(number)
