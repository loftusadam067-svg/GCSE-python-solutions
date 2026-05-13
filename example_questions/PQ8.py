# Topic:       2D array iteration with accumulation
# Marks:       6
# Description: A supermarket logs daily sales in a 2D array.
#              Each row contains: [ProductName, UnitsSold, PriceEach]
#              The 2D array arraySales is given below.
#
#              Write a program that:
#                - asks the user to enter a product name
#                - searches arraySales for all rows with that product name
#                - outputs the total units sold and the total revenue for that product
#                - if the product is not found, outputs "Product not found"
#
# Column index reference:
#   Index 0 = ProductName   e.g. "Bread"
#   Index 1 = UnitsSold     e.g. "30"   -- stored as a string, must be cast to int
#   Index 2 = PriceEach     e.g. "1.20" -- stored as a string, must be cast to float
#
# Example run:
#   Enter product name: Milk
#   Total units sold: 75
#   Total revenue: £52.5

arraySales = [
    ["Bread",  "30", "1.20"],
    ["Milk",   "50", "0.70"],
    ["Butter", "20", "1.50"],
    ["Milk",   "25", "0.70"],
    ["Bread",  "15", "1.20"],
    ["Eggs",   "40", "2.00"],
]

# Write your solution below:
