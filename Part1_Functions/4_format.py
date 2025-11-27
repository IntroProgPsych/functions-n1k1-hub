# https://www.w3schools.com/python/python_strings_format.asp
# Write a function greet_person(name) that returns the message “Hello, NAME!”.
# Ask the user for their name and print the returned message.
    
# Write your code here:
def greet_person(name):
	"""Return a greeting for the given name."""
	return f"Hello, {name}!"


if __name__ == '__main__':
	# Ask the user for their name, then print the greeting returned by greet_person
	name = input('Enter your name: ')
	message = greet_person(name)
	print(message)
