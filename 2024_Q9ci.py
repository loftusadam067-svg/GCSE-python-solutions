# Year:        2024
# Question:    Q9(c)(i)
# Marks:       4
# Description: Takes a jump height in centimetres as input and outputs VALID
#              or NOT VALID. The height must be between 40.0 and 180.0 cm inclusive.

# --- Input ---
height = float(input("Enter the height jumped (cm): "))

# --- Validation ---
# Check the height is within the allowed range (both boundary values count as valid)
if height >= 40.0 and height <= 180.0:
    print("VALID")
else:
    print("NOT VALID")
