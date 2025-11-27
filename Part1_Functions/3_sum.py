# https://www.w3schools.com/python/python_casting.asp / https://www.w3schools.com/python/python_scope.asp
# Write a function add(a, b) that returns the sum of the two numbers.
# Ask the user for two numbers (as input), convert them to integers, call the function, and print the result.
    
# Write your code here:
def add(a, b):
	"""Return the sum of a and b."""
	return a + b


if __name__ == '__main__':
	# Ask the user for two numbers (as input), convert them to integers
	x = input('First number: ')
	y = input('Second number: ')

	try:
		a = int(x)
		b = int(y)
	except ValueError:
		print('Please enter valid integers.')
	else:
		result = add(a, b)
		print('Result:', result)
