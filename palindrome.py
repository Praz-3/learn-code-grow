import numpy
num = input()
numlist = list(num)
numlistr = numpy.flipud(numlist)

if( all(numlist) == all(numlistr) ):
	print("YES")
else:
	print("NO")