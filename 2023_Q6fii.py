# Year:        2023
# Question:    Q6(f)(ii)
# Marks:       6
# Description: Asks the user for a date, then totals the number of seconds
#              sensors were activated on that date and outputs the result.

# arrayEvents is a 2D array (list of lists) — all values are stored as strings.
# Column index structure:
#   Index 0 = Date        e.g. "05/02/2023"
#   Index 1 = SensorID    e.g. "WS2"         -- arrayEvents[1][1] contains "MS1"
#   Index 2 = SensorType  e.g. "Window"
#   Index 3 = Length      e.g. "38"          -- seconds; must be cast to int to add up
arrayEvents = [
    ["05/02/2023", "WS2", "Window", "38"],
    ["05/02/2023", "MS1", "Motion", "2"],
    ["06/02/2023", "DS3", "Door",   "1"],
    ["06/02/2023", "MS2", "Motion", "3"],
    ["06/02/2023", "MS1", "Motion", "2"],
    ["07/02/2023", "WS1", "Window", "24"],
    ["07/02/2023", "DS1", "Door",   "1"],
]

# --- Input ---
dateInput = input("Enter a date (DD/MM/YYYY): ")

# --- Calculation ---
totalSeconds = 0

# Go through every row and add up the length for rows that match the date
for i in range(len(arrayEvents)):
    if arrayEvents[i][0] == dateInput:
        # Length is stored as a string so it must be converted to int before adding
        totalSeconds = totalSeconds + int(arrayEvents[i][3])

# --- Output ---
print("Sensors were activated for " + str(totalSeconds) + " seconds on " + dateInput)
