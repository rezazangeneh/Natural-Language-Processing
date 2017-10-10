import random
fid = open("finalData.csv", "r")
header = fid.readline()
li = fid.readlines()[1:]
fid.close()

for i in range(5):
	random.shuffle(li)
print "Done"

fid = open("finalData.csv", "w")
fid.writelines(header)

fid.writelines(li)
fid.close()