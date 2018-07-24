import numpy as np
import matplotlib.pyplot as plt
import re
import pandas

files = [] 
# Need to add file names to loop through

# for f in files:
# 	# If a text file
# 	# file = open(f)

# 	# If a csv
# 	df = pandas.read_csv(f)
# 	# Make a dataframe and read the coordinates to make a xarr and yarr
# 	# Loop through each line, add to xarr and yarr



# 	# Maybe can find way in the settings of the ploto to change the dimensions of the plot. The dimensions need to fit the size of the page
# 	plt.scatter(df['X Gaze Data'], df['Y Gaze Data'])
# 	plt.show()

# 	# Then run the script, save the output as the name in f and append the word 'dots'


file = 'gazeDataOutput.csv'

df = pandas.read_csv(file)
# Make a dataframe and read the coordinates to make a xarr and yarr
# Loop through each line, add to xarr and yarr

xarr = df['X Gaze Data']
print xarr


# Maybe can find way in the settings of the ploto to change the dimensions of the plot. The dimensions need to fit the size of the page
# plt.scatter(df['X Gaze Data'], df['Y Gaze Data'])
# plt.show()


# file = open("./eyetrackingdata/eyedatahannah.txt", "r")

# xarr = []
# yarr = []

# first = True
# pagenum = 1



# # Manually clean up beginning and end of file so that it starts at the right "User Clicked."
# for line in file:
# 	# print(line)
# 	if re.search("User Clicked.", line) is not None and not first:
# 		# MAKE HEATMAP HERE

# 		plt.scatter(xarr, yarr)
# 		plt.show()

# 		print('Page ' + str(pagenum) + ': ' + str(len(xarr)))
# 		pagenum += 1

# 		xarr = []
# 		yarr = []

# 	else:
# 		#Adding to current map arrays
# 		first = False
# 		grps = re.match(r"\((.*), (.*)\)", line)

# 		if grps == None:
# 			#empty line, so skip it
# 			pass
# 		else:
# 			grps = grps.groups()
# 			x = float(grps[0])
# 			y = float(grps[1])

# 			if x == 0 or y == 0 or y < 0 or x < 0 or x > 1600:
# 				#didn't track eyes ignore 0's
# 				pass
# 			else:
# 				xarr.append(x)
# 				yarr.append(y)

# file.close()

