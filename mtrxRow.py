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
def mrow(num):

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
	A = Matrix[num]
	for i in range(0,rows):
		if np.array_equal(A[i], array([0,0,0])): # no points
			continue
		
		elif np.array_equal(A[i], array([0,0,1])): # 'c' point only
		
			pc=[[0.8,0.2]]
			plt.plot(*zip(*pc),marker='o',color='b',label='c')
			#plt.legend()
			plt.show()
		
		elif np.array_equal(A[i], array([0,1,0])): # 'b'point only
		
			pb=[[0.2,0.2]]
			plt.plot(*zip(*pb),marker='o',color='g',label='b')
			#plt.legend()
			plt.show()
			
		
		elif np.array_equal(A[i], array([0,1,1])): # 'b-c' line 
		
			verts = [0.2,0.2], [0.8,0.2]
			poly = patches.Polygon(verts)
			poly.set_edgecolor('c') # 1 cyan
			ax.add_patch(poly)
		
			lbl=np.array(('b','c'))
			x=np.array([0.2,0.8])
			y=np.array([0.2,0.2])
			for t,color in zip(('b','c'),('go','bo')):
    				plt.plot(x[lbl==t],y[lbl==t],color, label=t)
			#plt.legend()
			plt.show()
			
		
		elif np.array_equal(A[i], array([1,0,0])): # 'a' point only
		
			pa=[[0.2,0.8]]
			plt.plot(*zip(*pa),marker='o',color='r',label='a')
			#plt.legend()
			plt.show()
			
		
		elif np.array_equal(A[i], array([1,0,1])): # 'a-c' line 

			verts = [0.2,0.8], [0.8,0.2]
			poly = patches.Polygon(verts)
			poly.set_edgecolor('m') # 2 magenta
			ax.add_patch(poly)
		
			lbl=np.array(('a','c'))
			x=np.array([0.2,0.8])
			y=np.array([0.8,0.2])
			for t,color in zip(('a','c'),('ro','bo')):
    				plt.plot(x[lbl==t],y[lbl==t],color, label=t)
			#plt.legend()
			plt.show()
			
			
		elif np.array_equal(A[i], array([1,1,0])): # 'a-b' line

			verts = [0.2,0.8], [0.2,0.2]
			poly = patches.Polygon(verts)
			poly.set_edgecolor('y')
			ax.add_patch(poly)
		
			lbl=np.array(('a','b'))
			x=np.array([0.2,0.2])
			y=np.array([0.8,0.2])
			for t,color in zip(('a','b'),('ro','go')):
    				plt.plot(x[lbl==t],y[lbl==t],color, label=t)
			#plt.legend()
			plt.show()
			
		
		elif np.array_equal(A[i], array([1,1,1])): # 'solid abc triangle'
		
			verts = [0.2,0.8], [0.2,0.2],[0.8,0.2]
			poly = patches.Polygon(verts)
			poly.set_facecolor('0.4')
			ax.add_patch(poly)

			lbl=np.array(('a','b','c'))
			x=np.array([0.2,0.2,0.8])
			y=np.array([0.8,0.2,0.2])
			for t,color in zip(('a','b','c'),('ro','go','bo')):
    				plt.plot(x[lbl==t],y[lbl==t],color, label=t)
			#plt.legend()
			plt.show()
	plt.box('off');
	plt.axis('off');
	plt.show()
	plt.draw()
	return;
	
mrow(num)
"""
http://stackoverflow.com/questions/3302586/matplotlib-legend-help

"""
		

