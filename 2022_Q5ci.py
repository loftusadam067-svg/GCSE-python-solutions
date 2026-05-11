# Year:        2022
# Question:    Q5(c)(i)
# Marks:       4
# Description: Defines the newPrice() function that calculates and returns the
#              total cost of a hotel stay given a number of nights and room type.
#              Basic rooms cost £60/night; Premium rooms cost £80/night.
#              Parameters are not validated, as stated in the question.


def newPrice(nights, room):
    """
    Calculate the total price for a hotel stay.

    Parameters:
        nights (int): Number of nights the guest is staying.
        room (str):   Room type — either "basic" or "premium".

    Returns:
        int: Total price in pounds for the full stay.
    """
    # Assign the correct nightly rate based on room type;
    # the else branch covers "premium" because the question guarantees only
    # two valid values and states validation is not required here
    if room == "basic":
        rate = 60   # basic nightly rate in pounds
    else:
        rate = 80   # premium nightly rate in pounds

    # Multiply the nightly rate by the number of nights to get the full cost
    return nights * rate
