x = 0
y = 0
sums = 0
maxnum = 0
n = 0

out = open('result.txt', 'w')
inp = open('test.txt', 'r')

line = inp.readline().split()
x = int(line[0])
y = int(line[1])
out.write("row values\n")
for i in range(0, x): #get values of all rows
	vals = inp.readline().split()
	sums = 0
	n = 0
	maxnum = 0
	for x in vals:
		x = int(x)
		sums = sums + x
		n = n + 1
		if x > maxnum:
			maxnum = x
	if n != 1:
		sums = sums + n - 1
	else:
		sums = sums
	minplaceable = int(y - sums)
	if sums == y:
		for k in range(0,len(vals)-1):
			out.write("b" + vals[k])
			out.write(",w1,")
		out.write("b" + vals[-1] + "\n")
	elif minplaceable < maxnum: # we could place some not all
		curwhite = 0
		for x in vals:
			x = int(x)
			if x > minplaceable:
				curwhite = curwhite + minplaceable
				out.write("w" + str(curwhite) + ",")
				res = x - minplaceable
				out.write("b" + str(res) + ",")
				curwhite = minplaceable
				#trying to be clever with the math that goes here to calculate 
			else:
				curwhite = curwhite + x + 1
		out.write("w" + str(curwhite) + "\n")		
	else:
		out.write("w" + str(y) +"\n")


out.write("column values")
for j in range(0, y): #get values of all columns
	print("hello")