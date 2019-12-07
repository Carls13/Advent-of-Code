def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

#Part 1
inputs = open("day2Input.text", 'r')
for value in inputs:
	array = value.split(',')

#Replacing values
array[1] = 12;
array[2] = 2;

newArray = chunks(array, 4);

result = 0
for element in newArray:
	operator = int(element[0]);
	firstIndex = int(element[1]);
	secondIndex = int(element[2]);
	indexToReplace = int(element[3]);
	if operator == 1:
		result = int(array[firstIndex]) + int(array[secondIndex]);
		array[indexToReplace] = result;
	elif operator == 2:
		result = int(array[firstIndex]) * int(array[secondIndex]);
		array[indexToReplace] = result;
	elif operator == 99:
		break;

print array[0];