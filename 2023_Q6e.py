# Year:        2022
# Question:    Q6(e)
# Marks:       6
# Description: Defines the SaveLogs() procedure that appends a string of
#              sensor event data to a named text file, preserving all existing
#              log entries so the historical record is never overwritten.


def SaveLogs(data, filename):
    """
    Append a string of log data to a text file.

    Each call adds one new line to the file, so multiple calls build up a
    growing log rather than replacing earlier entries.

    Parameters:
        data (str):     The string of data to store (e.g. one sensor event).
        filename (str): The name (or path) of the text file to write to.

    Returns:
        None
    """
    # 'a' (append) mode is used deliberately instead of 'w' (write) mode;
    # 'w' would erase every previous log entry on each call, destroying the
    # historical record — 'a' keeps all existing lines and adds to the end
    with open(filename, "a") as log_file:
        # A newline character is appended so that each log entry starts on
        # its own line when the file is read back later
        log_file.write(data + "\n")
