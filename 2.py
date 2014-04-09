termA = 0
termB = 1
termC = 0
evenSum = 0
while termC <= 4000000:
	termC = termA + termB
	termA = termB
	termB = termC
	if termC % 2 == 0:
		evenSum += termC
print evenSum
