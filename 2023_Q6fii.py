# Year:        2023
# Question:    Q6(f)(ii)
# Marks:       6
# Description: Asks the user for a date, searches the arrayEvents 2D array for
#              all sensor activations on that date, sums their durations in
#              seconds, and outputs a message including the date and total.

# arrayEvents is a 2D list where every element is a list of strings.
# Column index structure (all values stored as strings):
#   Index 0 = Date       (e.g. "05/02/2023")
#   Index 1 = SensorID   (e.g. "WS2")    — arrayEvents[1][1] contains "MS1"
#   Index 2 = SensorType (e.g. "Window")
#   Index 3 = Length     (e.g. "38")     — seconds activated; cast to int before summing
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
date_input = input("Enter a date (DD/MM/YYYY): ")

# --- Calculation ---
total_seconds = 0

# Iterate through every row to collect all events that match the entered date;
# a single loop handles any number of rows without knowing the count in advance
for row in arrayEvents:
    # Index 0 holds the date for this sensor event
    if row[0] == date_input:
        # Length is stored as a string throughout the array, so it must be
        # converted to int before arithmetic — leaving it as a string would
        # cause string concatenation instead of numeric addition
        total_seconds += int(row[3])

# --- Output ---
# The message format mirrors the example given in the question
print("Sensors were activated for " + str(total_seconds) +
      " seconds on " + date_input)
