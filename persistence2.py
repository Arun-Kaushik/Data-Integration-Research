"""
This function loads randomly-selected data from the Netflix sample dataset
and generates a user-complex and a movie-complex. It then performs poor
man's persistence on each and reports the results.
"""

# Importation statements.
from os.path import join
from sys import exit
from numpy import loadtxt, zeros, sum, max, savetxt
from scipy.io import mmread
from numpy.linalg import eigvalsh
from pydec import abstract_simplicial_complex

# Define a function for extracting the simplicial complex from rows and 
# columns of a 0/1 matrix.
def get_complexes(M):
    """ Extracts the row- or column-complexes of the 0/1 matrix M. That is,
    e.g. each row in M becomes a simplex in the abstract simplicial row-
    complex, with the simplex degree set by the number of nonzeros in that
    row; the simplex has vertices corresponding to the nonzero entries. """

    # Initialize the return tuples of lists of lists that define complex.
    row = []
    col = []
    for i in range(M.shape[1]):
        row += [[i]]
    for i in range(M.shape[0]):
        col += [[i]]
    row_complex = tuple([row])
    col_complex = tuple([col])

    # Determine number of each type of non-vertex simplex in each complex.
    row_sum = sum(M,axis=1)
    col_sum = sum(M,axis=0)
    row_simplices = list(set(list(row_sum[row_sum > 1])))
    col_simplices = list(set(list(col_sum[col_sum > 1])))

    # Now for each type of simplex in each complex, concatenate simplex 
    # into list of other similar simplices, then add to complex tuple.
    for i in row_simplices:
        row_list = []
        for j in range(M.shape[0]):
            if row_sum[j] == i:
                row_list += [list(M[j,:].nonzero()[0])]
        row_complex += tuple([row_list])
    for i in col_simplices:
        col_list = []
        for j in range(M.shape[1]):
            if col_sum[j] == i:
                col_list += [list(M[:,j].nonzero()[0])]
        col_complex += tuple([col_list])

    return row_complex, col_complex

# Define a function to find the dimension of the kernel of a dense matrix.
def get_dim_ker(A, tol=1e-7):
    """ Finds the dimension of kernel of dense Laplacian matrix A using
    eigenvalue method. tol specifies cutoff level below which an eigenvalue
    is assumed to be zero for purposes of deciding if it is in kernel. """
    q = eigvalsh(A)
    return len((q < tol).nonzero()[0])


### Top of program. #######################################################

# Specify path to data, path for output, and problem sizes.
datapath = "."
outpath = "."
n_movies = 5
n_users = 10 # number of users to sample per movie
tot_movies = 10 # 17700
movie_user_file = './M1.mtx'

## # Create a random number generator with controlled seed.
## seed = 123459876
## rng = RandomState(seed)



# Initialize storage for Betti numbers. Size is [top_dim+1 x # filters].
user_results = zeros((max(sum(1*(M>0),axis=1)) + 1, 5),dtype=int)
movie_results = zeros((max(sum(1*(M>0),axis=0)) + 1, 5),dtype=int)

# Define the tolerance for determining when an eigenvale is "zero enough."
tol = 1e-7

# Now that we have the master data matrix assembled, we filter it, and at 
# each level construct the user- and movie-complex, upon which we compute
# dim(ker(Laplacian_k)) for k ranging from 0 through top dimension.
print "Filtering data and computing Betti numbers..."
M_0 = 1*(M > 0) # used to filter out the non-rated films
for stars in [1,2,3,4,5]:
    print stars

    # Filter M and create filtered complexes.
    M_filt = 1*(M <= stars) * M_0
    user_tuple, movie_tuple = get_complexes(M_filt)
    user_complex = abstract_simplicial_complex(user_tuple)
    movie_complex = abstract_simplicial_complex(movie_tuple)

    # Perform calculations on user complex Lalacians.
    for k in range(user_complex.complex_dimension()):
        b_low = user_complex.chain_complex()[k]
        b_high = user_complex.chain_complex()[k+1]
        Laplacian_k = (b_low.T * b_low + b_high * b_high.T).todense()
        betti_k = get_dim_ker(Laplacian_k, tol)
        user_results[k, stars-1] = betti_k
    k = user_complex.complex_dimension()
    b_low = user_complex.chain_complex()[k]
    Laplacian_k = (b_low.T * b_low).todense()
    betti_k = get_dim_ker(Laplacian_k, tol)
    user_results[k, stars-1] = betti_k

    # Perform calculations on movie complex Lalacians.
    for k in range(movie_complex.complex_dimension()):
        b_low = movie_complex.chain_complex()[k]
        b_high = movie_complex.chain_complex()[k+1]
        Laplacian_k = (b_low.T * b_low + b_high * b_high.T).todense()
        betti_k = get_dim_ker(Laplacian_k, tol)
        movie_results[k, stars-1] = betti_k
    k = movie_complex.complex_dimension()
    b_low = movie_complex.chain_complex()[k]
    Laplacian_k = (b_low.T * b_low).todense()
    betti_k = get_dim_ker(Laplacian_k, tol)
    movie_results[k, stars-1] = betti_k

# Save results to directory.
savetxt(join(outpath,'user_betti_numbers.txt'), user_results, fmt='%7i')
savetxt(join(outpath,'movie_betti_numbers.txt'), movie_results, fmt='%7i')
print "Done."
