def hasAFour(indices):
	rowPostion = 0
	for row in indices:
		for cell in row:
			if all(elem in row for elem in list(range(cell,cell+4))):
				return True

			elif rowPostion < 7:
				if cell in indices[rowPostion+1]:
					if cell in indices[rowPostion+2]:
						if cell in indices[rowPostion+3]:
							return True
		rowPostion += 1

def tooManySingles(indices):
	rowPostion = 0
	single_count = 0
	for row in indices:
		for cell in row:
			if row.index(cell)+1


def validate_battlefield(battleField):
	boardVision = [['w','b','w','b','w','b','w','b','w','b'],
			['b','w','b','w','b','w','b','w','b','w'],
			['w','b','w','b','w','b','w','b','w','b'],
			['b','w','b','w','b','w','b','w','b','w'],
			['w','b','w','b','w','b','w','b','w','b'],
			['b','w','b','w','b','w','b','w','b','w'],
			['w','b','w','b','w','b','w','b','w','b'],
			['b','w','b','w','b','w','b','w','b','w'],
			['w','b','w','b','w','b','w','b','w','b'],
			['b','w','b','w','b','w','b','w','b','w']]

	battleFieldIndex = []
	battleFieldVision = []
	rowCount = 0
	if sum([sum(row) for row in battleField]) !=20 :
		return False

	for row in battleField:
		indices = [i for i, x in enumerate(row) if x == 1]
		battleFieldIndex.append(indices)

	for row in battleFieldIndex:
		for i in row:
			battleFieldVision.append(boardVision[rowCount][i])
		rowCount += 1

	bCount = battleFieldVision.count('b') - 5
	wCount = battleFieldVision.count('w') - 5

	if wCount >= 8 or bCount >= 8:
		return False
	elif wCount <= 2 or bCount <= 2:
		return False

	if ((wCount - 2) + (bCount - 4)) % 4 != 0:
		return False
	elif ((wCount - 3)+ (bCount - 3)) % 4 != 0:
		return False
	elif ((wCount - 4)+ (bCount - 2)) % 4 != 0:
		return False

	if hasAFour(battleFieldIndex):
		return True
	else:

		return False


print(validate_battlefield(
		[[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
		 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
		 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
		 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
		 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
		 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))