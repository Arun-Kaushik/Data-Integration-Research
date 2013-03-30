""" Read matrix of user-movie ratings and create a submatrix from
top users and popular movies.

"""

from scipy.io import mmread, mmwrite
from numpy import argsort, array, sum, int32, zeros_like

movie_user_file = './M1.mtx'
m_movies = 100; n_users = 100000
## m_movies = 100; n_users = 10000

# Read user-movie rating matrix
Mfull= mmread(movie_user_file)
print "Read in full matrix"
clmnindxptr = Mfull.tocsc().indptr
rwindxptr = Mfull.tocsr().indptr

# Determine largest m rows (top users) and n columns (popular movies) to
# find submatrix for additional experiments
nnz_cols = [clmnindxptr[i+1] - clmnindxptr[i]
            for i in range(clmnindxptr.shape[0] - 1)]
nnz_rows = [rwindxptr[i+1] - rwindxptr[i]
            for i in range(rwindxptr.shape[0] - 1)]
popular_movies = array(argsort(nnz_cols)[:m_movies], dtype=int32)
print "Found %d popular movies" %(m_movies)
popular_users = array(argsort(nnz_rows)[:n_users], dtype=int32)
print "Found top %d users" %(n_users)

users_mask = zeros_like(Mfull.row)
movies_mask = zeros_like(Mfull.row)

for user in popular_users:
    users_mask += array(Mfull.row == user, dtype=int32)
for movie in popular_movies:
    movies_mask += array(Mfull.col == movie, dtype=int32)

## users_mask = sum([Mfull.row == user for user in popular_users], axis=0)
## movies_mask = sum([Mfull.col == movie for movie in popular_movies], axis=0)
data_mask = array([users_mask[i] and movies_mask[i] for i in
                   range(len(users_mask))])
print "Determined masks"

## submatrixfile = 'm' + str(m_movies) + 'u' + str(n_users) + '.mtx'
## mmwrite(submatrixfile, M, field="integer")





