"""
this program simulates a random walk.

A person starts on a number line at 0. They choose
to walk either -1 and +1 on the line. Once they reach
either -5 or 5, they stop walking. The program reports
regular updates on where the person is and how many
steps it took the person to get there
"""

from random import choice

def main():
	person = 0
	steps_taken = 0
	while abs(person) < 5:
		direction = choice([-1, 1])
		person = person + direction
		steps_taken = steps_taken + 1
		print("After", steps_taken, "steps, I'm at", person)
	print("It took me", steps_taken, "steps to move 5 places away from my starting location.")


main()