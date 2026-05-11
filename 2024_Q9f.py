# Year:        2024
# Question:    Q9(f)
# Marks:       6
# Description: Repeatedly collects team names and scores until the user enters
#              'stop', then identifies and outputs the team with the highest
#              score. Handles the edge case where no teams are entered.

# --- Initialisation ---
# Both winning values start as None so the first team entered automatically
# becomes the leader without needing a separate "first team" code path;
# None also lets us detect the case where the user stops before entering any teams
winning_team = None
winning_score = None

# --- Input Loop ---
# A while True loop is used because the number of teams is unknown in advance;
# 'stop' acts as the sentinel value that ends data entry, as specified
while True:
    team_name = input("Enter team name (or 'stop' to finish): ")

    # Check for the sentinel before asking for a score so the user is never
    # prompted for a score after typing 'stop'
    if team_name.lower() == "stop":
        break

    score_input = input("Enter score for " + team_name + ": ")

    # Scores are compared numerically, so the string input must be cast to int
    score = int(score_input)

    # --- Comparison ---
    # winning_score is None on the very first iteration, so any score qualifies;
    # after that, only a strictly greater score replaces the current winner —
    # ties leave the first team with that score as the winner
    if winning_score is None or score > winning_score:
        winning_team = team_name
        winning_score = score

# --- Output ---
# Guard against the case where the user entered 'stop' immediately
if winning_team is not None:
    print("The winning team is " + winning_team +
          " with a score of " + str(winning_score))
else:
    print("No teams were entered.")
