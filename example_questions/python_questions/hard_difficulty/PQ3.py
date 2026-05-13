# Topic:       String processing (character iteration, classification)
# Marks:       8
# Description: A web application validates new passwords before they are
#              accepted. Write a function called checkPassword that:
#                - takes one parameter: password (a string)
#                - iterates through every character and counts:
#                    the number of uppercase letters
#                    the number of digits
#                  (count these yourself — do not use any built-in count method)
#                - outputs the counts in the format:
#                    "Uppercase: X   Digits: Y"
#                - returns True if ALL of the following are met:
#                    the password is at least 8 characters long
#                    it contains at least one uppercase letter
#                    it contains at least one digit
#                  returns False otherwise
#              You do not need to handle user input.
#
# Example calls:
#   checkPassword("Hello123")  → prints "Uppercase: 1   Digits: 3", returns True
#   checkPassword("hello123")  → prints "Uppercase: 0   Digits: 3", returns False
#   checkPassword("HELLO")     → prints "Uppercase: 5   Digits: 0", returns False

# Write your solution below:
