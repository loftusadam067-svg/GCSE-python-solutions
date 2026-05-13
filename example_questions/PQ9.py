# Topic:       Boolean logic and procedure call
# Marks:       4
# Description: A server room monitoring system uses three Boolean variables:
#                PowerOn         - True if the server is powered on
#                DoorOpen        - True if the server room door is open
#                TemperatureHigh - True if the temperature is above the safe threshold
#
#              The cooling system should activate (by calling CoolDown()) only if:
#                - the server is powered on
#                - AND at least one of the following is true:
#                    the door is open OR the temperature is high
#
#              The function CoolDown() is already written for you.
#              Write the conditional logic that calls CoolDown() when appropriate.
#              Use the variable values given below — do not change them.
#
# The expected behaviour with the values below:
#   PowerOn = True, DoorOpen = False, TemperatureHigh = True  →  CoolDown() is called


def CoolDown():
    # In a real system this would activate the cooling hardware
    print("Cooling system activated.")


# --- Variables ---
PowerOn = True
DoorOpen = False
TemperatureHigh = True

# Write your solution below:
