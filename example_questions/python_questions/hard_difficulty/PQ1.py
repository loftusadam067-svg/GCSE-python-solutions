# Topic:       Input Validation (re-prompt loop, multiple fields)
# Marks:       8
# Description: A hotel booking form collects two pieces of information.
#              Write a program that:
#                - asks the user to enter the number of nights
#                  (must be a whole number between 1 and 30 inclusive)
#                  and keeps asking until a valid value is entered
#                - asks the user to enter the room type
#                  (must be "single", "double", or "suite")
#                  and keeps asking until a valid value is entered
#                - once both are valid, outputs the booking summary:
#                    "Room: " and the room type
#                    "Nights: " and the number of nights
#
# Example run:
#   Enter number of nights: -1
#   Invalid. Please try again.
#   Enter number of nights: 3
#   Enter room type (single/double/suite): penthouse
#   Invalid. Please try again.
#   Enter room type (single/double/suite): double
#   Room: double
#   Nights: 3

# Write your solution below:
