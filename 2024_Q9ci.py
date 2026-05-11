# Year:        2024
# Question:    Q9(c)(i)
# Marks:       4
# Description: Takes a jump height in centimetres as input and outputs VALID
#              or NOT VALID. The acceptable range is 40.0 cm to 180.0 cm
#              inclusive; values outside this range are rejected.

# --- Input ---
height_input = input("Enter the height jumped (cm): ")

# --- Validation ---
# Convert to float rather than int because heights may include decimal values
# (e.g. 95.5 cm); using int() would lose the fractional part and could
# incorrectly accept or reject borderline entries
height = float(height_input)

# Both boundary values (40.0 and 180.0) are valid, so <= is used at each end
# rather than < to implement the inclusive range stated in the rules
if 40.0 <= height <= 180.0:
    print("VALID")
else:
    print("NOT VALID")
