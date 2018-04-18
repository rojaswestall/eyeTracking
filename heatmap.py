import numpy as np
import matplotlib.pyplot as plt
import re

file = open("./eyetrackingdata/eyedatahannah.txt", "r")

xarr = []
yarr = []

first = True
pagenum = 1

# Manually clean up beginning and end of file so that it starts at the right "User Clicked."
for line in file:
	# print(line)
	if re.search("User Clicked.", line) is not None and not first:
		# MAKE HEATMAP HERE

		plt.scatter(xarr, yarr)
		plt.show()

		print('Page ' + str(pagenum) + ': ' + str(len(xarr)))
		pagenum += 1

		xarr = []
		yarr = []

	else:
		#Adding to current map arrays
		first = False
		grps = re.match(r"\((.*), (.*)\)", line)

		if grps == None:
			#empty line, so skip it
			pass
		else:
			grps = grps.groups()
			x = float(grps[0])
			y = float(grps[1])

			if x == 0 or y == 0 or y < 0 or x < 0 or x > 1600:
				#didn't track eyes ignore 0's
				pass
			else:
				xarr.append(x)
				yarr.append(y)

file.close()

