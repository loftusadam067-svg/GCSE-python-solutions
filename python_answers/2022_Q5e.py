# Year:        2022
# Question:    Q5(e)
# Marks:       6
# Description: Calculates the car park charge for each visit and outputs the
#              total price. Repeats until the user enters 0 hours to stop.
#              Standard rate is £4/hour; electric vehicles pay £2/hour.

# --- Main Loop ---
# Keep asking for visits until the user enters 0 to stop
hours = -1  # set to a non-zero value so the loop runs at least once
while hours != 0:

    # --- Input ---
    hours = float(input("Enter number of hours parked (0 to exit): "))

    # Only calculate and output a price if the user hasn't chosen to exit
    if hours != 0:
        electric = input("Is the car electric? (yes/no): ")

        # --- Calculation ---
        # Electric cars pay half the standard rate
        if electric == "yes":
            rate = 2   # discounted rate for electric vehicles
        else:
            rate = 4   # standard hourly rate

        totalPrice = hours * rate

        # --- Output ---
        print("Total price to pay: £" + str(totalPrice))
