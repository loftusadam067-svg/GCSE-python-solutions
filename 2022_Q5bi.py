# Year:        2022
# Question:    Q5(b)(i)
# Marks:       5
# Description: Validates hotel booking inputs (first name, surname, room type,
#              and number of nights) and outputs ALLOWED or NOT ALLOWED.
#              All four criteria must pass for the booking to be accepted.

# --- Input ---
# Collect raw strings from the user exactly as the question provides them
firstName = input("Enter a first name: ")
surname = input("Enter a surname: ")
room = input("Enter basic or premium: ")
nights = input("Enter between 1 and 5 nights: ")

# stayComplete tracks whether every validation check has passed;
# it starts False and is only set True if all four checks succeed
stayComplete = False

# --- Validation ---

# Names must contain at least one character; an empty string means the user
# pressed Enter without typing, which is not a valid name
names_valid = len(firstName) > 0 and len(surname) > 0

# Room type must be one of exactly two accepted strings; any other value
# (including "Basic", "PREMIUM" etc.) is rejected to keep comparisons simple
# and consistent with the OCR mark scheme wording
room_valid = room == "basic" or room == "premium"

# nights arrives as a string, so isdigit() guards against a ValueError before
# casting; a non-numeric entry (e.g. "abc") must still produce NOT ALLOWED
if nights.isdigit():
    nights_int = int(nights)
    # The range is inclusive at both ends: 1 and 5 are both valid
    nights_valid = 1 <= nights_int <= 5
else:
    nights_valid = False

# Only mark the stay complete when every individual check passes;
# a single failure is enough to deny the booking
if names_valid and room_valid and nights_valid:
    stayComplete = True

# --- Output ---
if stayComplete:
    print("ALLOWED")
else:
    print("NOT ALLOWED")
