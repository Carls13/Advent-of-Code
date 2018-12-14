#Part 1

myGridSerial = 8561
fuelCells = []

# Calculate each cell's power level
for y in range(300):
    yCoord = y+1
    actualYCells = []
    for x in range(300):
        xCoord = x + 1
        xyPoint ='('+ str(xCoord) + ','+str(yCoord)+')'
        rackId = xCoord + 10
        powerLevel = rackId * yCoord
        powerLevel += myGridSerial
        powerLevel = powerLevel * rackId
        powerLevel = (powerLevel%1000)//100
        powerLevel -= 5
        actualYCells.append([xyPoint, powerLevel])
    fuelCells.append(actualYCells)
    
# mainCellPower = []

# # For each 3x3 area we will define it like: 
# # abc
# # def
# # ghi
# for y in range(298):
#     for x in range(298):
#         areaPower = 0
#         # Gets top left cell 
#         topLeft = fuelCells[y][x][0]
#         # Gets each cell's power level
#         a = fuelCells[y][x][1]
#         b = fuelCells[y+1][x][1]
#         c = fuelCells[y+2][x][1]
#         d = fuelCells[y][x+1][1]
#         e = fuelCells[y+1][x+1][1]
#         f = fuelCells[y+2][x+1][1]
#         g = fuelCells[y][x+2][1]
#         h = fuelCells[y+1][x+2][1]
#         i = fuelCells[y+2][x+2][1]
#         # Sums all of them
#         areaPower = a + b + c + d + e + f + g + h + i
#         mainCellPower.append([topLeft, areaPower])

# # Compares greatest
# greatestPower = -1000
# greatestCoord = ''

# for area in mainCellPower:
#     if area[1] > greatestPower:
#         greatestPower = area[1]
#         greatestCoord = area[0]

# print(greatestCoord)

# Part 2
# Using previous data
size = 1
while size < 31:
    for y in range(300 - (size - 1) ):
        for x in range(300 - (size - 1) ):
            areaPower = 0
            yi = y
            xi = x
            while yi <(yi + size - 1):
                while xi < (xi + size - 1):
                    areaPower += fuelCells[yi][xi]