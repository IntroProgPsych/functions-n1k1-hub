# Write a function describe_number(n) that:

# returns “positive” if n > 0

# returns “zero” if n == 0

# returns “negative” if n < 0

# Ask the user for a number, call the function, and print the message.*

# Write your code here:
def describe_number(n):
	"""Return 'positive' if n>0, 'zero' if n==0, 'negative' if n<0."""
	# convert to float so function works with integers and decimals
	try:
		value = float(n)
	except (TypeError, ValueError):
		raise ValueError('n must be a number')

	if value > 0:
		return 'positive'
	if value == 0:
		return 'zero'
	return 'negative'


if __name__ == '__main__':
	# Ask the user for a number, call describe_number, and print the message
	user = input('Enter a number: ')
	try:
		# keep the original numeric value to pass to the function
		# function itself converts to float so we don't need to convert here,
		# but we'll validate to give a friendly error message.
		_ = float(user)
	except ValueError:
		print('Please enter a valid number.')
	else:
		message = describe_number(user)
		print(message)
