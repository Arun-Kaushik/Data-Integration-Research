import numpy
from numpy import array
from matplotlib.pylab import plot
import matplotlib.pyplot as plt
from matplotlib import colors
import networkx as nx

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

G = nx.Graph()
"""
# row-wise first
for m in range(0,256):
	plt.subplot(16,16,m)
	A = Matrix[m];
	for i in range(0,rows):
		G.clear()
		if numpy.array_equal(A[i], array([0,0,0])):
			nx.draw_random(G)
		
		elif numpy.array_equal(A[i], array([0,0,1])):
			G.add_node('c')
			nx.draw_random(G)
		
		elif numpy.array_equal(A[i], array([0,1,0])):
			G.add_node('b')
			nx.draw_random(G)
		
		elif numpy.array_equal(A[i], array([0,1,1])):
			G.add_edge('b','c')
			nx.draw_random(G)
		
		elif numpy.array_equal(A[i], array([1,0,0])):
			G.add_node('a')
			nx.draw_random(G)
		
		elif numpy.array_equal(A[i], array([1,0,1])):
			G.add_edge('a','c')
			nx.draw_random(G)
			
		elif numpy.array_equal(A[i], array([1,1,0])):
			G.add_edge('a','b')
			nx.draw_random(G)
			
		else: # numpy.array_equal(A[i], array([1,1,1]))
			G.add_edges_from([('a','b'),('a','c'),('b','c')])
			nx.draw_random(G)
plt.show()	
"""
# column-wise
for p in range(410,414):
	plt.subplot(2,2,p-410)
	B = numpy.transpose(Matrix[p]);
	for i in range(0,cols):
		G.clear()
		if numpy.array_equal(B[i], array([0,0,0])):
			nx.draw_random(G, node_size=250, node_color='b')
		
		elif numpy.array_equal(B[i], array([0,0,1])):
			G.add_node(3)
			nx.draw_random(G,node_size=250, node_color='b')
		
		elif numpy.array_equal(B[i], array([0,1,0])):
			G.add_node(2)
			nx.draw_random(G,node_size=250, node_color='b')
		
		elif numpy.array_equal(B[i], array([0,1,1])):
			G.add_edge(2,3)
			nx.draw_random(G,node_size=250, node_color='b')
		
		elif numpy.array_equal(B[i], array([1,0,0])):
			G.add_node(1)
			nx.draw_random(G,node_size=250, node_color='b')
		
		elif numpy.array_equal(B[i], array([1,0,1])):
			G.add_edge(1,3)
			nx.draw_random(G,node_size=250, node_color='b')
			
		elif numpy.array_equal(B[i], array([1,1,0])):
			G.add_edge(1,2)
			nx.draw_random(G,node_size=250, node_color='b')
			
		else: # numpy.array_equal(B[i], array([1,1,1]))
			G.add_edges_from([(1,2),(1,3),(2,3)])
			nx.draw_random(G,node_size=250, node_color='b')
plt.show()
