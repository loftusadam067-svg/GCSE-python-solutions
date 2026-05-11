# Year:        2023
# Question:    Q6(b)
# Marks:       4
# Description: Checks three Boolean sensor variables and calls SoundAlarm()
#              when the system is armed AND at least one sensor is active.
#              The alarm requires both conditions to prevent false triggers.


def SoundAlarm():
    """
    Stub procedure that represents triggering the physical alarm hardware.

    In a real embedded system this would send a signal to the alarm sounder
    (e.g. via a GPIO pin or network message). Here it prints to the console
    so the logic can be tested without hardware.

    Parameters: None
    Returns:    None
    """
    # This print statement stands in for real hardware interaction
    print("Alarm sounding!")


# --- Variables ---
# These Boolean values would be read from physical sensors or a control panel
# in a real system; they are set here for demonstration purposes
SystemArmed = True
DoorSensorActive = False
WindowSensorActive = True

# --- Logic ---
# The alarm must only sound when:
#   1. The system has been armed (prevents alerts during setup/maintenance), AND
#   2. At least one sensor has been triggered (door OR window is enough)
# Using 'or' for the sensors means either sensor alone is sufficient to raise
# the alarm — both being active at once is also handled correctly
if SystemArmed and (DoorSensorActive or WindowSensorActive):
    SoundAlarm()
