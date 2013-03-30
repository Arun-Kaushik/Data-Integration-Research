from networkx import draw, Graph
G = Graph()
G.add_edges_from([('a','b'), ('b','c'), ('a','c')])
draw(G, {'a': (0,1), 'b': (0,0), 'c': (1,0)})
