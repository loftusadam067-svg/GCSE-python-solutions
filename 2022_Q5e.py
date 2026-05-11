# Year:        2022
# Question:    Q5(e)
# Marks:       6
# Description: Calculates and outputs car park charges for each visit.
#              Standard rate is £4/hour; electric vehicles pay £2/hour.
#              The program repeats until the user enters 0 hours to exit.

# --- Main Loop ---
# A while True loop is used because the number of visits is unknown in advance;
# the sentinel value 0 provides the only exit condition, matching the question spec
while True:

    # --- Input ---
    hours_input = input("Enter number of hours parked (0 to exit): ")

    # Convert to float so the program handles fractional hours (e.g. 1.5 hours)
    hours = float(hours_input)

    # 0 is the sentinel value that signals the user has finished entering visits
    if hours == 0:
        break

    electric_input = input("Is the car electric? (yes/no): ")

    # --- Calculation ---
    # Electric vehicles receive a 50% discount to encourage sustainable transport;
    # any answer other than "yes" is treated as a non-electric vehicle
    if electric_input.lower() == "yes":
        rate = 2    # halved rate for electric cars
    else:
        rate = 4    # standard hourly charge

    total_price = hours * rate

    # --- Output ---
    print("Total price to pay: £" + str(total_price))
