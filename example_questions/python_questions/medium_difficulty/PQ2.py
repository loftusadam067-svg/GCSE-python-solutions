# Topic:       Functions (two functions, one calls the other)
# Marks:       6
# Description: A delivery company calculates the final cost of a parcel.
#              The base cost depends on weight: £3.00 per kg.
#              A loyalty discount applies if the customer has made more than
#              10 previous orders: 10% off the base cost.
#
#              Write two functions:
#                calcBase(weight)          - returns the base cost (weight × 3.00)
#                calcFinal(weight, orders) - calls calcBase to get the base cost,
#                                           then returns the final cost:
#                                           if orders > 10, apply 10% discount
#                                           otherwise return the base cost unchanged
#
#              You do not need to call the functions or handle user input.
#
# Example calls:
#   calcFinal(5, 12)  →  13.5   (base = 15.00, 10% off = 13.50)
#   calcFinal(5, 8)   →  15.0   (base = 15.00, no discount)

# Write your solution below:
