from networkx import draw, Graph

G = Graph()
G.add_edges_from([('a','b'),('b','c'),('a','c')])
draw(G,{'b': (0,0), 'c': (1,0), 'a' : (0,1)})
