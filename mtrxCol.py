import numpy as np 
from numpy import array
from matplotlib.pylab import plot
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.patches as patches

# 'a'- 01 is red, 'b'- 12 is green, 'c'- 02 is blue
# '0'- ab is yellow, '1'- bc is cyan, '2'- ac is magenta

print("Which matrix(0-511) do u want?\n")
num = raw_input('> ')
def mcol(num):
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

	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.set_xlim(0,1)
	ax.set_ylim(0,1)
	
	num = int(num)
	B = np.transpose(Matrix[num])
	for i in range(0,cols):
		if np.array_equal(B[i], array([0,0,0])): # no points
			continue
		
		elif np.array_equal(B[i], array([0,0,1])): # '2' point only
		
			p2=[[0.8,0.2]]
			plt.plot(*zip(*p2),marker='o',color='m',label='2')
			#plt.legend()
			plt.show()
		
		elif np.array_equal(B[i], array([0,1,0])): # '1' point only
		
			p1=[[0.2,0.2]]
			plt.plot(*zip(*p1),marker='o',color='c',label='1')
			#plt.legend()
			plt.show()
			
		
		elif np.array_equal(B[i], array([0,1,1])): # '1-2' line 
		
			verts = [0.2,0.2], [0.8,0.2]
			poly = patches.Polygon(verts)
			poly.set_edgecolor('g') # b green
			ax.add_patch(poly)
		
			lbl=np.array(('1','2'))
			x=np.array([0.2,0.8])
			y=np.array([0.2,0.2])
			for t,color in zip(('1','2'),('co','mo')):
    				plt.plot(x[lbl==t],y[lbl==t],color, label=t)
			#plt.legend()
			plt.show()
			
		
		elif np.array_equal(B[i], array([1,0,0])): # '0' point only
		
			pa=[[0.2,0.8]]
			plt.plot(*zip(*pa),marker='o',color='y',label='0')
			#plt.legend()
			plt.show()
			
		
		elif np.array_equal(B[i], array([1,0,1])): # '0-2' line 

			verts = [0.2,0.8], [0.8,0.2]
			poly = patches.Polygon(verts)
			poly.set_edgecolor('b') # c blue
			ax.add_patch(poly)
		
			lbl=np.array(('0','2'))
			x=np.array([0.2,0.8])
			y=np.array([0.8,0.2])
			for t,color in zip(('0','2'),('yo','mo')):
    				plt.plot(x[lbl==t],y[lbl==t],color, label=t)
			#plt.legend()
			plt.show()
			
			
		elif np.array_equal(B[i], array([1,1,0])): # '0-1' line

			verts = [0.2,0.8], [0.2,0.2]
			poly = patches.Polygon(verts)
			poly.set_edgecolor('r') # a red
			ax.add_patch(poly)
		
			lbl=np.array(('0','1'))
			x=np.array([0.2,0.2])
			y=np.array([0.8,0.2])
			for t,color in zip(('0','1'),('yo','co')):
    				plt.plot(x[lbl==t],y[lbl==t],color, label=t)
			#plt.legend()
			plt.show()
			
		
		elif np.array_equal(B[i], array([1,1,1])): # 'solid abc triangle'
		
			verts = [0.2,0.8], [0.2,0.2],[0.8,0.2]
			poly = patches.Polygon(verts)
			poly.set_facecolor('0.4')
			ax.add_patch(poly)

			lbl=np.array(('0','1','2'))
			x=np.array([0.2,0.2,0.8])
			y=np.array([0.8,0.2,0.2])
			for t,color in zip(('0','1','2'),('yo','co','mo')):
    				plt.plot(x[lbl==t],y[lbl==t],color, label=t)
			#plt.legend()
			plt.show()
	plt.box('off');
	plt.axis('off');
	plt.show()
	plt.draw()
	return;

mcol(num)
"""
http://stackoverflow.com/questions/3302586/matplotlib-legend-help

"""
		

