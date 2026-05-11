# Year:        2022
# Question:    Q5(c)(ii)
# Marks:       3
# Description: Uses the newPrice() function to calculate and output the total
#              cost of staying in a Premium room for 5 nights (£400).


def newPrice(nights, room):
    """
    Calculate the total price for a hotel stay.

    Parameters:
        nights (int): Number of nights the guest is staying.
        room (str):   Room type — either "basic" or "premium".

    Returns:
        int: Total price in pounds for the full stay.
    """
    # Rate depends on room type; premium costs more per night than basic
    if room == "basic":
        rate = 60
    else:
        rate = 80

    return nights * rate


# --- Output ---
# The question specifies exact values (Premium, 5 nights), so they are passed
# directly to newPrice() rather than prompting the user for input
price = newPrice(5, "premium")
print("The price of staying in a Premium room for 5 nights is £" + str(price))
