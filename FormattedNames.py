# LEVEL 1
 
#
 
# The exercise here is to write a function that takes a single argument (a
 
# list of names) and returns a string representing the English-formatted
 
# conjunction of those names.
 
#
 
# For example, given these names: ['Alice', 'Bob', 'Carlos', 'Diana']
 
#
 
# The output would be: "Alice, Bob, Carlos and Diana"
 
#
 
# This type of function is useful when building user interfaces that show the
 
# list of people in a conversation, for example.
 
#
 
# Whether or not the output follows the Oxford comma rule is up to the author.

def level1(lst):
	if lst is None or len(lst) == 0:
		return None
	if len(lst) == 1:
		return lst[0]
	res = ""
	i = 0
	while i < len(lst) - 1:
		res += lst[i] + ", "
		i += 1
	res += "and " + lst[len(lst) - 1]
	return res
 
# LEVEL 2
 
#
 
# We iterate on the problem by adding a second argument to our function.
 
#
 
# Now lets add a new argument called `limit`. This controls the maximum number of 
 
# names that should be displayed.  Any remaining items are "summarized" using the
 
# string "and # more".
 
#
 
# For example, given these names: ['Alice', 'Bob', 'Carlos', 'Diana'] and limit: 2
 
#
 
# The output would be: "Alice, Bob and 2 more"

def level2(lst, limit):
	if lst is None or len(lst) == 0:
		return None
	if len(lst) <= limit:
		return level1(lst)
	res = ""
	i = 0
	while i < limit:
		res += lst[i] + ", "
		i += 1
	res += "and " + str(len(lst) - limit) + " more"
	return res
 
# LEVEL 3
 
#
 
# Finally, write a function which prints the maximum  
# possible number of names within the `max_chars` limit
 
# (versus the first N names that fit within the limit).

def level3_1(lst, max_chars):
	"""Counts the number of items that will fit in max_chars and calls level2 function on the new limit"""
	if lst is None or len(lst) == 0:
		return None
	i = 0
	k = 0
	while i < len(lst):
		if max_chars - len(lst[i]) >= 0:
			k += 1
			max_chars -= len(lst[i])
		else:
			break
		i += 1
	return level2(lst, k)

def level3_2(lst, max_chars):
	"""Same function but doesn't call level2 function"""
	if lst is None or len(lst) == 0:
		return None
	i = 0
	k = 0
	res = ""
	while i < len(lst):
		if max_chars - len(lst[i]) >= 0:
			if i == len(lst) - 1:
				return level1(lst)
			else: 
				res += lst[i] + ", "
				max_chars -= len(lst[i])
				k += 1
				i += 1
		else:
			break
	return res + "and " + str(len(lst) - k) + " more"


# --- TESTS --- #

lst1 = None
lst2 = ['Alice', 'Bob', 'Carlos', 'Diana']
lst3 = ['Taffy']
lst4 = ['Tinkerbell', 'Tracie', 'Tina', 'Tori', 'Taffy']

# LEVEL 1 TESTS
print("Expected: None")
print(level1(lst1))
print("Expected: 'Alice, Bob, Carlos, and Diana'")
print(level1(lst2))
print("Expected: 'Taffy'")
print(level1(lst3))
print("Expected: 'Tinkerbell, Tracie, Tina, Tori, and Taffy'")
print(level1(lst4))
print()

# LEVEL 2 TESTS
print("Expected: None")
print(level2(lst1, 0))
print("Expected: 'Alice, Bob, Carlos, and 1 more'")
print(level2(lst2, 3))
print("Expected: 'Taffy'")
print(level2(lst3, 5))
print("Expected: 'Tinkerbell, Tracie, and 3 more'")
print(level2(lst4, 2))
print()

# LEVEL 3_1 TESTS
print("Expected: None")
print(level3_1(lst1, 10))
print("Expected: 'Alice, Bob, Carlos, and 1 more'")
print(level3_1(lst2, 14))
print("Expected: 'Taffy'")
print(level3_1(lst3, 5))
print("Expected: 'Tinkerbell, Tracie, and 3 more'")
print(level3_1(lst4, 16))
print()

# LEVEL 3_2 TESTS
print("Expected: None")
print(level3_2(lst1, 10))
print("Expected: 'Alice, Bob, Carlos, and 1 more'")
print(level3_2(lst2, 14))
print("Expected: 'Taffy'")
print(level3_2(lst3, 5))
print("Expected: 'Tinkerbell, Tracie, and 3 more'")
print(level3_2(lst4, 16))
print()

