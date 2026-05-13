# Topic:       String processing (character iteration, ord() and chr())
# Marks:       8
# Description: A simple encryption program uses a Caesar cipher to encode
#              messages. Each letter is shifted forward by a given number of
#              positions in the alphabet. Non-letter characters (spaces,
#              punctuation) are left unchanged.
#              The cipher wraps around: shifting 'z' by 1 gives 'a'.
#              The original case of each letter must be preserved.
#
#              Write a function called caesarEncrypt that:
#                - takes two parameters: message (a string) and shift (an int)
#                - returns the encoded message as a string
#
# Note: you may use ord() and chr() in this question.
#
# Example calls:
#   caesarEncrypt("hello", 3)   →  "khoor"
#   caesarEncrypt("xyz", 2)     →  "zab"
#   caesarEncrypt("Hello!", 1)  →  "Ifmmp!"

# Write your solution below:
