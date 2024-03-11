
def distinctSubstring(str):

	# Put all distinct substring in a HashSet
	result = set()

	# List All Substrings
	for i in range(len(str)):
		for j in range(i + 1, len(str) + 1):

			# Add each substring in Set
			result.add(str[i:j])

		# Return the HashSet
	return result



str = "asbsab"
subs = distinctSubstring(str)

print("Distinct Substrings are: ")
for s in subs:
    print(s)


