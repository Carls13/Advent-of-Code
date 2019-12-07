#Part 1
# inputs = open("day1Input.text", 'r')
# total = 0
# for value in inputs:
# 	total = total + (int(value) // 3 - 2);
# print total;

#Part 2
inputs = open("day1Input.text", 'r')
total = 0
for value in inputs:
	actualFuel = (int(value) // 3 - 2);
	total += actualFuel;
	while actualFuel > 0:
		actualFuel = (int(actualFuel) // 3 - 2);
		if actualFuel > 0:
			total += actualFuel;
print total;