#------------test for subplots------------------

import numpy as np 
from numpy import array
from matplotlib.pylab import plot
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.patches as patches



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

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(0,1)
ax.set_ylim(0,1)
# row-wise first
for m in range(410,414):
	plt.subplot(2,2,m-410)
	ax.set_xlim(0,1)
	ax.set_ylim(0,1)
	
	A = Matrix[m];
	for i in range(0,rows):
		if np.array_equal(A[i], array([0,0,0])): # no points
			continue
		
		elif np.array_equal(A[i], array([0,0,1])): # 'c' point only
			#fig = plt.figure()
		
			pc=[[0.8,0.2]]
			plt.plot(*zip(*pc),marker='o',color='b',label='c')
			plt.legend()
			plt.show()
		
		elif np.array_equal(A[i], array([0,1,0])): # 'b'point only
			#fig = plt.figure()
		
			pb=[[0.2,0.2]]
			plt.plot(*zip(*pb),marker='o',color='g',label='b')
			plt.legend()
			plt.show()
			
		
		elif np.array_equal(A[i], array([0,1,1])): # 'b-c' line 
			#fig = plt.figure()
		
			verts = [0.2,0.2], [0.8,0.2]
			poly = patches.Polygon(verts)
			ax.add_patch(poly)
		
			lbl=np.array(('b','c'))
			x=np.array([0.2,0.8])
			y=np.array([0.2,0.2])
			for t,color in zip(('b','c'),('go','bo')):
    				plt.plot(x[lbl==t],y[lbl==t],color, label=t)
			plt.legend()
			plt.show()
			
		
		elif np.array_equal(A[i], array([1,0,0])): # 'a' point only
			#fig = plt.figure()
		
			pa=[[0.2,0.8]]
			plt.plot(*zip(*pa),marker='o',color='r',label='a')
			plt.legend()
			plt.show()
			
		
		elif np.array_equal(A[i], array([1,0,1])): # 'a-c' line 
			#fig = plt.figure()

			verts = [0.2,0.8], [0.8,0.2]
			poly = patches.Polygon(verts)
			ax.add_patch(poly)
		
			lbl=np.array(('a','c'))
			x=np.array([0.2,0.8])
			y=np.array([0.8,0.2])
			for t,color in zip(('a','c'),('ro','bo')):
    				plt.plot(x[lbl==t],y[lbl==t],color, label=t)
			plt.legend()
			plt.show()
			
			
		elif np.array_equal(A[i], array([1,1,0])): # 'a-b' line
			#fig = plt.figure()

			verts = [0.2,0.8], [0.2,0.2]
			poly = patches.Polygon(verts)
			ax.add_patch(poly)
		
			lbl=np.array(('a','b'))
			x=np.array([0.2,0.2])
			y=np.array([0.8,0.2])
			for t,color in zip(('a','b'),('ro','go')):
    				plt.plot(x[lbl==t],y[lbl==t],color, label=t)
			plt.legend()
			plt.show()
			
		
		elif np.array_equal(A[i], array([1,1,1])): # 'solid abc triangle'
			#fig = plt.figure()
			verts = [0.2,0.8], [0.2,0.2],[0.8,0.2]
			poly = patches.Polygon(verts)
			poly.set_facecolor('k')
			ax.add_patch(poly)

			lbl=np.array(('a','b','c'))
			x=np.array([0.2,0.2,0.8])
			y=np.array([0.8,0.2,0.2])
			for t,color in zip(('a','b','c'),('ro','go','bo')):
    				plt.plot(x[lbl==t],y[lbl==t],color, label=t)
			plt.legend()
plt.show()
		
		

