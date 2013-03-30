"""
This function extracts all of the user rating data for all of the movie files. 
It then stores this information in the sparse integer matrix M for later use, 
and which will hopefully be small enough for storage on the repository.
"""

# Importation statements.
from os.path import join
from sys import exit
from numpy import loadtxt, zeros, uint8, uint32
from scipy.sparse import coo_matrix
from scipy.io import mmwrite, mmread

# Define paths and problem sizes.
data_path = "/Users/Mina/download/training_set"
#output_path = "."
output_path="/Users/Mina/download/training_set"
n_movies = 1960

# Loop over all movies. For each, open & extract data. Store to a list of non-
# zero components for M. For now, assume that user number is also ordinal 
# number. Later we will go through and correct these to true user number. Note
# that we have 17700 movies and about 480,000 users numbered from 1 - 2649429
# with (significant) gaps. There are slightly less than 101e6 integer data to 
# store.
print "Harvesting and assembling data..."
users = set([])
ij = zeros((2,10000000),dtype=uint32) # need at least 32-bit ints to store
nz = zeros((10000000,),dtype=uint8)
nnz = 0
for movie in range(n_movies):
	if not movie % 200:
		print "  " + str(movie)
	filename = join(data_path,'mv_' + ('%07i')%(movie+1) + '.txt')
	data = loadtxt(filename, skiprows=1, delimiter=',', \
		comments='-', dtype=int)
	users = users.union(set(list(data[:,0])))
	for k in range(data.shape[0]):
		ij[0,nnz] = data[k,0] # user number
		ij[1,nnz] = movie
		nz[nnz] = data[k,1] # rating
		nnz += 1	
	del(data)
#out of bound movie  =1961	
# Now trim, and convert user numbers to ordinal numbers. Create M and save.
ij = ij[:,0:nnz]
nz = nz[0:nnz]
user2num = dict(zip(list(users), range(len(users))))
for k in range(nnz):
	ij[0,k] = user2num[ij[0,k]]
M = coo_matrix((nz, ij), shape=(len(users),n_movies))
#mmwrite(join(output_path, 'M.mtx'), M, field="integer")
mmwrite('M1.mtx', M, field="integer")
print M
	
# Code below runs but used all my available memory before reaching 6000 movies.
"""
# Loop over all movies. For each, open & extract data. users is a set containing
# each unique user number. data is a list of lists of lists, where data is 
# indexed by [movie_number], [user_number, rating], [entry number].
print "Harvesting data..."
users = set([])
data = []
for movie in range(n_movies):
	if not movie % 200:
		print
		"  " + str(movie)
	filename = join(data_path,'mv_' + ('%07i')%(movie+1) + '.txt')
	contents = loadtxt(filename, skiprows=1, delimiter=',', \
		comments='-', dtype=int)
	temp_data = [[list(contents[:,0]), list(contents[:,1])]]
	users = users.union(set(list(contents[:,0])))
	data += temp_data

# Now that we have all of the data read in, determine user numbering and create
# the sparse matrix M. We have about 480,000 users and 17700 movies, so we can't
# store indices and data for all nonzeros at once in memory (since e.g. int8 or
# int16 won't work to record user index number). So instead we hstack data one
# column (movie) at a time. Initialize M as a zero vector.
print "Assembling data..."
n_users = len(users)
user2num = dict(zip(list(users), range(n_users)))
M = csc_matrix((n_users, 1), dtype="uint8")
for movie in range(n_movies):
	if not movie % 200:
		print "  " + str(movie)
	temp_inds = zeros((2, len(data[movie][0])), dtype=int)
	temp_data = zeros((len(data[movie][0]),), dtype=uint8)
	for j in range(len(data[movie][0])):
		user = data[movie][0][j]
		rate = data[movie][1][j]
		temp_data[j] = rate
		temp_inds[0,j] = user2num[user]
	N = csc_matrix((temp_data, temp_inds), shape=(n_users,1),dtype="uint8")
	M = hstack([M,N],format="csc",dtype=uint8)	

# Clip the initial (zero) vector of M and save to disk.
M = M[:,1:]
mmwrite(join(output_path, 'M.mtx'), M, field="integer")
"""
