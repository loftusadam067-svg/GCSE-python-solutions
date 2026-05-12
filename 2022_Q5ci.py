# Year:        2022
# Question:    Q5(c)(i)
# Marks:       4
# Description: Defines the newPrice() function. Takes the number of nights and
#              room type, and returns the total price. No validation needed.


def newPrice(nights, room):
    # Work out the nightly rate based on the room type
    if room == "basic":
        rate = 60   # basic room costs £60 per night
    else:
        rate = 80   # premium room costs £80 per night

    # Multiply rate by number of nights to get the total cost
    total = nights * rate
    return total
