#Part 1
# Opens and reads file
inputs = open("words.text", 'r')
data = inputs.read()
words = data.split("\n")

# Initializes global counters
# global2Counter = 0
# global3Counter = 0
# for word in words:
# 	# Initializes counters for each word
# 	actualWord2Counter = 0
# 	actualWord3Counter = 0
# 	# Loop for letters in actual word
# 	for i in word:
# 		if word.count(i) == 2 and actualWord2Counter == 0:
# 			actualWord2Counter = 1
# 			global2Counter += 1
# 		if word.count(i) == 3 and actualWord3Counter == 0:
# 			actualWord3Counter = 1
# 			global3Counter += 1
# 		if actualWord2Counter == 1 and actualWord3Counter == 1:
# 			break
# print(global3Counter * global2Counter)

# Part 2
# Splits each word into array of letters
splittedWords = []
for word in words:
	splittedWords.append(list(word))

i = 0
highestCounter = 0
highestWords = []
# Loop for words
for word in splittedWords:
	j = i + 1
	# Loop for each target word to compare 
	# (starting from current word + 1)
	while j < len(splittedWords):
		wordCounter = 0
		k = 0
		# Compares letter by letter
		for letter in word:
			if letter == splittedWords[j][k]:
				wordCounter += 1
			k+=1
		# Saves current words if matches counter is greater
		if wordCounter > highestCounter:
			highestCounter = wordCounter
			highestWords = [ word, splittedWords[j] ]
		j += 1
	i += 1
print(highestCounter)

word1 = ''
word2 = ''

# Rebuilds winner words
for letter in highestWords[0]:
	word1 += letter
for letter in highestWords[1]:
	word2 += letter
	
# Prints words
print(word1)
print(word2)
