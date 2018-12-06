#Part 1
#inputs = open("Day1Inputs.txt", 'r')
# freq = 0
# for value in inputs:
# 	freq = freq + int(value)

#Part 2
inputs = open("Day1Inputs.text", 'r')
data = inputs.read()
lines = data.split("\n")
freq = 0
freqArray = set()
first = True
firstRepeated = 0
while first:
	for value in lines:
		freq = freq + int(value)
		if freq in freqArray and first:
			firstRepeated = freq
			first = False
			break
		else:
			freqArray.add(freq)
print(firstRepeated)