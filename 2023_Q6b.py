# Year:        2023
# Question:    Q6(b)
# Marks:       4
# Description: Checks whether the alarm should sound based on three Boolean
#              variables, and calls SoundAlarm() when appropriate.


def SoundAlarm():
    # In a real system this would trigger the physical alarm hardware
    print("Alarm sounding!")


# --- Variables ---
# These would come from the actual sensors in a real system
SystemArmed = True
DoorSensorActive = False
WindowSensorActive = True

# --- Logic ---
# The alarm only sounds if the system is armed AND at least one sensor is active
# Either sensor being active is enough to trigger the alarm
if SystemArmed == True:
    if DoorSensorActive == True or WindowSensorActive == True:
        SoundAlarm()
