# https://www.w3schools.com/python/python_arguments.asp
# https://www.w3schools.com/python/python_user_input.asp
# https://www.w3schools.com/python/python_casting.asp
# Write a function square(n) that returns the square of the number n (n multiplyed with n).
# Ask the user for a number, call the function, and print the result.
    
# Sample output:

# Input: 5
# Output: 25

# Write your code here:
def square(n):
	"""Return the square of n (n multiplied by n)."""
	return n * n


if __name__ == '__main__':
	# Ask the user for a number, convert to float so it works with integers and decimals
	user = input('Input: ')
	try:
		# convert to float so we can handle decimal input too
		num = float(user)
	except ValueError:
		print('Please enter a valid number.')
	else:
		result = square(num)
		# If result is a whole number, print without .0 like the sample output
		if result.is_integer():
			result = int(result)
		print('Output:', result)
