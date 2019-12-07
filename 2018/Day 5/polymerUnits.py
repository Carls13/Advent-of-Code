# Part 1
file = open("day5Input.text", 'r')
inputString = file.read()

def hasRemainingRepeatingPairs(inputString):
	previous = ''
	for letter in inputString:
		if (previous.islower() and previous.upper() == letter) or ( previous.isupper() and previous.lower() == letter):
			return True
		previous = letter
	return False

def reactWord(inputString):
	while hasRemainingRepeatingPairs(inputString):
		previous = ''
		for letter in inputString:
			if (previous.islower() and previous.upper() == letter) or ( previous.isupper() and previous.lower() == letter):
				removingChar = previous + letter
				inputString = inputString.replace(removingChar, '')
			previous = letter
	return inputString

# finalString = reactWord(inputString)
# print(len(finalString))

# Part 2

file = open("day5Input.text", 'r')
inputString = file.read()

# Create alphabet list of lowercase letters
alphabet = []
for letter in range(97,123):
    alphabet.append(chr(letter))

deletedPairsInputs = []

# Creates array which contains words with each letter of alphabet deleted
for letter in alphabet:
	newInput = inputString.replace(letter, '')
	newInput = newInput.replace(letter.upper(), '')
	deletedPairsInputs.append(newInput)

# Creates arrays which contains every reacted word
reactedWords = []
for element in deletedPairsInputs:
	reacted = reactWord(element)
	reactedWords.append(reacted)

print(len(reactedWords))

# Finally, gets shortest reacted word
shortestWord = reactedWords[0]
shortestLength = len(shortestWord)
for word in reactedWords:
	if len(word) < shortestLength:
		shortestWord = word
		shortestLength = len(word)

print(shortestLength)


