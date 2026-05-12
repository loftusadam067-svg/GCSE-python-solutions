# Year:        2023
# Question:    Q6(e)
# Marks:       6
# Description: Defines the SaveLogs() procedure. Takes a string of data and a
#              filename, and stores the data in that text file.


def SaveLogs(data, filename):
    # Open the file in append mode so existing entries are not overwritten
    # "a" adds to the end of the file; "w" would delete everything already there
    myFile = open(filename, "a")
    myFile.write(data + "\n")  # add a new line after each entry
    myFile.close()
