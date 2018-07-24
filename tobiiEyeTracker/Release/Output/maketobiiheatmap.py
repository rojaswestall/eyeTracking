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
yarr = df[' Y Gaze Data']

count = 0
total = len(xarr)

for i in range(len(xarr)):
	if xarr[i] < 1000 or xarr[i] > 2450 or yarr[i] > 1750:
		count += 1
		del xarr[i]
		del yarr[i]

percent = (count/float(total))
print 'Number removed: ' + str(count)
print 'Total points: ' + str(total)
print 'Percentage focused on reading: ' + str(1 - percent)

# Maybe can find way in the settings of the ploto to change the dimensions of the plot. The dimensions need to fit the size of the page
plt.scatter(xarr, yarr)
plt.gca().invert_yaxis()
plt.show()
