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
#pos=nx.spectral_layout(G, dim=4)
#nx.draw_random_random(G)

A = Matrix[413];
for i in range(0,rows):
	G.clear()
	if numpy.array_equal(A[i], array([0,0,0])):
		nx.draw_random(G)
		
	if numpy.array_equal(A[i], array([0,0,1])):
		G.add_node('c')
		nx.draw_random(G)
		"""if (('c1' in G)==False)and(('c2' in G)==False):
			G.add_node('c1', pos=(1,1))
			#nx.draw_random(G)
		elif (('c2' in G)==False):
			G.add_node('c2', pos=(0,0))
			#nx.draw_random(G)
		else:
			G.add_node('c3', pos=(0.47,0.58))
		nx.draw_random(G)
	
		"""
		
	if numpy.array_equal(A[i], array([0,1,0])):
		G.add_node('b')
		nx.draw_random(G)
		
	if numpy.array_equal(A[i], array([0,1,1])):
		#if nx.path.bidirectional_dijkstra(G,'b','c')==False
		G.add_edge('b','c')
		nx.draw_random(G)
		
	if numpy.array_equal(A[i], array([1,0,0])):
		G.add_node('a')
		nx.draw_random(G)
		
	if numpy.array_equal(A[i], array([1,0,1])):
		G.add_edge('a','c')
		nx.draw_random(G)
			
	if numpy.array_equal(A[i], array([1,1,0])):
		G.add_edge('a','b')
		nx.draw_random(G)
			
	if numpy.array_equal(A[i], array([1,1,1])):
		G.add_edges_from([('a','b'),('a','c'),('b','c')])
		nx.draw_random(G)


plt.show()	

	

