import numpy
from numpy import array
from matplotlib.pylab import plot
import matplotlib.pyplot as plt
from matplotlib import colors


rows  = 3
cols = 3

n = 2**(rows*cols)
List = []
for i in range(0, n):
	List.append(bin(i))
	# remove all prefix '0b'
	List[i]= List[i].replace('0b','')
	# padding with front zeros
	List[i] = [int(j) for j in list(List[i].zfill(rows*cols))]
	# Another way: List[i] = List[i].rjust(rows*cols, '0')

Matrix = [array(i).reshape(3,3) for i in List]
#print Matrix

"""cmap = colors.ListedColormap(['white', 'black']) # 0 as white, 1 as black
   binary = LinearSegmentedColormap('binary', cmapdata)
"""

"""for i in range(0, n):
	plt.subplot(16, n/16, i)
	plt.spy(Matrix[i], precision = 0, marker= '.', markersize=15)
"""

#for printing
"""for i in range(0, 64):
	plt.subplot(8,8,i)
	# spy(Z) plots the aparsity pattern of the 2-D array Z.
	plt.spy(Matrix[i], precision = 0, marker= '.', markersize=15)
	#plot(Matrix[i])
	#plt.imshow(Matrix[i], cmap = cmap)
	#ax=plt.subplots()
	#plt.matshow(Matrix[i], cmap=binary)
"""	
"""for i in range(64, 128):
	plt.subplot(8,8,i-64)
	plt.spy(Matrix[i], precision = 0, marker= '.', markersize=15)


for i in range(128, 192):
	plt.subplot(8,8, i-128)
	plt.spy(Matrix[i], precision = 0, marker= '.', markersize=15)

	
for i in range(192, 256):
	plt.subplot(8,8, i-192)
	plt.spy(Matrix[i], precision = 0, marker= '.', markersize=15)
	

for i in range(256, 320):
	plt.subplot(8,8, i-256)
	plt.spy(Matrix[i], precision = 0, marker= '.', markersize=15)

for i in range(320, 384):
	plt.subplot(8,8, i-320)
	plt.spy(Matrix[i], precision = 0, marker= '.', markersize=15)

for i in range(384, 448):
	plt.subplot(8,8, i-384)
	plt.spy(Matrix[i], precision = 0, marker= '.', markersize=15)

for i in range(448, 512):
	plt.subplot(8,8, i-448)
	plt.spy(Matrix[i], precision = 0, marker= '.', markersize=15)

"""	
#plt.show()	
