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
		if x > maxnum
			maxnum = x
	sums = sums + n - 1
	minplaceable = y - sums
	if sums == y:
		for k in range(0,len(vals)-1):
			out.write("b" + vals[k])
			out.write(",w1,")
		out.write("b" + vals[-1] + "\n")
	elif y - sums <= maxnum: # we could place some not all
		
	else:
		out.write("bad\n")


out.write("column values")
for j in range(0, y): #get values of all columns
	print("hello")