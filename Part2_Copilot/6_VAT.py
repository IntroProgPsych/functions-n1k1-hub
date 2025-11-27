# Write a function apply_vat(price) that returns the price including 19% VAT.
# Ask the user for a price and print the result.

# Write your code here:
def apply_vat(price):
	"""Return the price including 19% VAT.

	price can be an int or float. This function returns a float.
	"""
	return price * 1.19


if __name__ == '__main__':
	user = input('Enter price: ')
	try:
		p = float(user)
	except ValueError:
		print('Please enter a valid number for the price.')
	else:
		total = apply_vat(p)
		# Show result rounded to 2 decimal places (common for prices)
		print('Price with VAT:', f"{total:.2f}")

