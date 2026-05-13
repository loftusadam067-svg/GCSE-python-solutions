# Topic:       2D array lookup
# Marks:       5
# Description: A bus company stores route information in a 2D array.
#              Each row contains: [RouteNumber, Destination, Fare]
#              The 2D array arrayRoutes is given below.
#
#              Write a program that:
#                - asks the user to enter a route number
#                - searches arrayRoutes for that route number
#                - if found, outputs the destination and fare
#                - if not found, outputs "Route not found"
#
# Column index reference:
#   Index 0 = RouteNumber   e.g. "42"
#   Index 1 = Destination   e.g. "City Centre"
#   Index 2 = Fare          e.g. "2.50"
#
# Example run:
#   Enter route number: 7
#   Destination: Westfield    Fare: £1.80
#
#   Enter route number: 99
#   Route not found

arrayRoutes = [
    ["5",  "North Park",    "1.50"],
    ["7",  "Westfield",     "1.80"],
    ["12", "City Centre",   "2.50"],
    ["18", "East Harbour",  "2.20"],
    ["24", "South Gate",    "1.60"],
]

# Write your solution below:
