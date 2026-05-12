# Year:        2024
# Question:    Q9(f)
# Marks:       6
# Description: Repeatedly takes team names and scores until the user enters
#              'stop', then outputs the name and score of the winning team.

# --- Initialisation ---
winningTeam = ""
winningScore = 0
firstTeam = True  # used to make sure the first team always becomes the initial winner

# --- Input Loop ---
# Keep asking for teams until the user types stop
teamName = input("Enter team name (or 'stop' to finish): ")

while teamName != "stop":
    score = int(input("Enter score for " + teamName + ": "))

    # --- Comparison ---
    # The first team entered always becomes the winner to start with;
    # after that, only replace the winner if the new score is higher
    if firstTeam == True or score > winningScore:
        winningTeam = teamName
        winningScore = score
        firstTeam = False

    teamName = input("Enter team name (or 'stop' to finish): ")

# --- Output ---
print("The winning team is " + winningTeam + " with a score of " + str(winningScore))
