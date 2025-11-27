# Write a function text_length(s) that returns how many characters the text has.
# Ask the user for a word and print its length.

# Write your code here:
def text_length(s):
	"""Return number of characters in string s."""
	return len(s)


if __name__ == '__main__':
	word = input('Enter a word: ')
	print('Length:', text_length(word))
