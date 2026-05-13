# Topic:       File I/O (append mode, loop)
# Marks:       6
# Description: A running club wants to log race results to a file.
#              Write a program that:
#                - repeatedly asks the user to enter a runner's name
#                - if the name is "stop", the loop ends
#                - otherwise asks for that runner's finishing time (in seconds)
#                - appends a line to a file called results.txt in the format:
#                    Name,Time
#                  e.g. Alice,312
#                - after the loop ends, outputs "Results saved."
#
#              Use append mode ("a") so that existing results are not overwritten.
#
# Example run:
#   Enter runner name (or 'stop'): Alice
#   Enter finishing time for Alice (seconds): 312
#   Enter runner name (or 'stop'): Bob
#   Enter finishing time for Bob (seconds): 298
#   Enter runner name (or 'stop'): stop
#   Results saved.
#
# Expected content written to results.txt:
#   Alice,312
#   Bob,298

# Write your solution below:
