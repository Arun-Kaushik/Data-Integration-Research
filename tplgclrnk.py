""" Some exploratory experiments involving topological rank of matrices.

"""

from numpy import zeros, int8, remainder, array
from numpy.random import seed, random_integers
from numpy.linalg import eigvalsh
from scipy.sparse import csr_matrix, csc_matrix
from pydec import abstract_simplicial_complex
from itertools import product, chain, combinations

## from itertools import tee, imap
## from operator import sub
## def pairwisediff(iterable):
##     "s -> (s[1] - s[0]), (s[2] - s[1]),..., (s[n] - s[n-1])"
##     a, b = tee(iterable)
##     next(a, None)
##     return imap(sub, a, b)

matrix_size = 20
max_block_size = 5
max_topological_rank = 5

seed(0); seeds1 = random_integers(0, 10000, 5)
seed(2012); seeds2 = random_integers(0, 10000, 5)
M = zeros(2 * (matrix_size,), dtype=int8)
for i in range(max_topological_rank):
    seed(seeds1[i])
    block_location = random_integers(0, matrix_size - 1, 2)
    seed(seeds2[i])
    block_size = random_integers(1, max_block_size, 2)
    row_span = list(remainder(
        range(block_location[0], (block_location[0] + block_size[0])),
        matrix_size))
    col_span = list(remainder(
        range(block_location[1], (block_location[1] + block_size[1])),
        matrix_size))
    for r, c in product(row_span, col_span):
        M[r, c] = 1
Mcsr = csr_matrix(M); Mcsc = csc_matrix(M)

# The complex formation is ugly for readability but IMHO elegant for
# getting the job done !
row_complex = map(list, list(set(filter(None, [tuple(
    Mcsr.indices[Mcsr.indptr[i]:Mcsr.indptr[i + 1]]
    ) for i in range(len(Mcsr.indptr) - 1)]))))
## row_complex += [[vertex] for vertex in list(set(list(chain(*row_complex))))]
row_vertex_set = [vertex for vertex in list(set(list(chain(*row_complex))))]
row_complex += [[v] for v in row_vertex_set]
row_complex = abstract_simplicial_complex(row_complex)

col_complex = map(list, list(set(filter(None, [tuple(
    Mcsc.indices[Mcsc.indptr[i]:Mcsc.indptr[i + 1]]
    ) for i in range(len(Mcsc.indptr) - 1)]))))
## col_complex += [[vertex] for vertex in list(set(list(chain(*col_complex))))]
col_vertex_set = [vertex for vertex in list(set(list(chain(*col_complex))))]
col_complex += [[v] for v in col_vertex_set]
col_complex = abstract_simplicial_complex(col_complex)

evals_row_complex = []; evals_col_complex = []
for p in range(row_complex.complex_dimension()):
    B_p = row_complex.chain_complex()[p]
    B_pplus1 = row_complex.chain_complex()[p + 1]
    laplacian_p = (B_p.T * B_p + B_pplus1 * B_pplus1.T)
    evals_row_complex.append(eigvalsh(laplacian_p.todense()))

for p in range(col_complex.complex_dimension()):
    B_p = col_complex.chain_complex()[p]
    B_pplus1 = col_complex.chain_complex()[p + 1]
    laplacian_p = (B_p.T * B_p + B_pplus1 * B_pplus1.T)
    evals_col_complex.append(eigvalsh(laplacian_p.todense()))

# Join of row_complex and col_complex
join_complex = set([])
## rowdict = {k:'s' + str(v) for v, k in enumerate(row_vertex_set)}
## coldict = {k:'t' + str(v) for v, k in enumerate(col_vertex_set)}

rowdict = {k:v for v, k in enumerate(row_vertex_set)}
coldict = {k:(v + len(row_vertex_set)) for v, k in enumerate(col_vertex_set)}

## simplices = [(s, t) for s in map(list, *row_complex.complex()[-2:-3:-1])
##              for t in map(list, *col_complex.complex()[-2:-3:-1])]

unique_row_simplices = set([])
## for nsimplex in row_complex.complex()[-1]:
##     unique_row_simplices.update([subset for p in range(2, len(nsimplex) + 1)
##                                  for subset in combinations(nsimplex, p)])
## unique_row_simplices.symmetric_difference_update(set(
##     [tuple(face) for faces in row_complex.complex()[1:-1]
##      for face in faces]))

unique_col_simplices = set([])
## for simplices in col_complex.complex()[-1:0:-1]:
##     for simplex in simplices:
##         unique_col_simplices.update([subset for p in range(2, len(simplex) + 1)
##                                      for subset in combinations(simplex, p)])
##         unique_col_simplices.symmetric_difference_update(set(
##             [tuple(face) for faces in col_complex.complex()[1:-1]
##              for face in faces]))

## for p in range(1, col_complex.complex_dimension() + 1):
##     for p_simplex in col_complex.complex()[p]:
##         unique_col_simplices.update(
##             [simplex for simplex_dimension in range(1, p + 1)
##              for simplex in combinations(p_simplex, simplex_dimension)])
##         unique_col_simplices.symmetric_difference_update(set(
##             [tuple(face) for faces in col_complex.complex()[1:p]
##              for face in faces]))
        
## unique_col_simplices.update([tuple(nsimplex) for nsimplex in
##                              col_complex.complex()[-1]])

unique_row_simplices.update([tuple(simplex) for simplex in
                             row_complex.complex()[-1]])
for p in range(row_complex.complex_dimension(), 1, -1):
    unique_row_simplices.update([
        face for simplex in row_complex.complex()[p]
        for face in combinations(simplex, p)])
    unique_row_simplices.symmetric_difference_update(
        [tuple(simplex) for simplex in row_complex.complex()[p - 1]])

unique_col_simplices.update([tuple(simplex) for simplex in
                             col_complex.complex()[-1]])
for p in range(col_complex.complex_dimension(), 1, -1):
    ## unique_col_simplices.update([tuple(simplex) for simplex in
    ##                              col_complex.complex()[p]])
    unique_col_simplices.update([
        face for simplex in col_complex.complex()[p]
        for face in combinations(simplex, p)])
    unique_col_simplices.symmetric_difference_update(
        [tuple(simplex) for simplex in col_complex.complex()[p - 1]])

join_simplices = []
for s in unique_row_simplices:
    for t in unique_col_simplices:
        join_simplices += [[rowdict[row_vertex] for row_vertex in list(s)] + \
                           [coldict[col_vertex] for col_vertex in list(t)]]
join_complex = abstract_simplicial_complex(array(join_simplices))
evals_join_complex = []
for p in range(join_complex.complex_dimension()):
    B_p = join_complex.chain_complex()[p]
    B_pplus1 = join_complex.chain_complex()[p + 1]
    laplacian_p = (B_p.T * B_p + B_pplus1 * B_pplus1.T)
    evals_join_complex.append(eigvalsh(laplacian_p.todense()))






    
