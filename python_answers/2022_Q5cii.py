# Year:        2022
# Question:    Q5(c)(ii)
# Marks:       3
# Description: Uses newPrice() to output the cost of a Premium room for 5 nights.


def newPrice(nights, room):
    # Work out the nightly rate based on the room type
    if room == "basic":
        rate = 60
    else:
        rate = 80

    total = nights * rate
    return total


# --- Output ---
# Call newPrice() with the values given in the question and display the result
price = newPrice(5, "premium")
print("The price of staying in a Premium room for 5 nights is £" + str(price))
