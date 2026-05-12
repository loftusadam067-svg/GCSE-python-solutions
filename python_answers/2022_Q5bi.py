# Year:        2022
# Question:    Q5(b)(i)
# Marks:       5
# Description: Takes hotel booking inputs and checks if they are all valid.
#              Outputs ALLOWED if everything passes, or NOT ALLOWED if not.

# --- Input ---
firstName = input("Enter a first name: ")
surname = input("Enter a surname: ")
room = input("Enter basic or premium: ")
nights = input("Enter between 1 and 5 nights: ")

stayComplete = False

# --- Validation ---
# Nest the checks so that every condition must pass before setting stayComplete
if firstName != "" and surname != "":        # names must not be blank
    if room == "basic" or room == "premium": # room must be one of the two options
        if nights.isdigit():                 # must be a whole number before casting
            if int(nights) >= 1 and int(nights) <= 5:  # must be in the valid range
                stayComplete = True

# --- Output ---
if stayComplete == True:
    print("ALLOWED")
else:
    print("NOT ALLOWED")
