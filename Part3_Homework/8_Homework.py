# 1.(Mandatory) Write a function called calculate_grade(score)
#    that RETURNS the correct letter grade:
#       90+ -> A
#       80-89 -> B
#       70-79 -> C
#       60-69 -> D
#       below 60 -> F
#
# 2. Write another function called display_report(score, grade)
#    that PRINTS something like:
#       Score: 85
#       Grade: B
#
# 3. In the main part of the program:
#       - ask the user for the score
#       - call calculate_grade(score)
#       - call display_report(score, grade)
#
# Keep input() outside the functions.

# Write your code here:
def calculate_grade(score):
	# assume score is an integer 0-100
	if score >= 90:
		return 'A'
	if score >= 80:
		return 'B'
	if score >= 70:
		return 'C'
	if score >= 60:
		return 'D'
	return 'F'


def display_report(score, grade):
	print('Score:', score)
	print('Grade:', grade)


if __name__ == '__main__':
	s = input('Enter the score: ')
	try:
		score = int(s)
	except ValueError:
		print('Please enter a whole number score (e.g. 85).')
	else:
		grade = calculate_grade(score)
		display_report(score, grade)

