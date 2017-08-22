import csv
import numpy as np
no_users=0
curr_id=1
no_movies=0
movie_id={} #maps movie_id[their movie_id]=our_id
with open('ml-latest-small/ratings.csv') as r:
    reader = csv.reader(r, delimiter=",")
    reader.next()
    for row in reader:
    	if(int(row[0])>no_users):
        	no_users=int(row[0])


with open('ml-latest-small/movies.csv') as r:
    reader = csv.reader(r, delimiter=",")
    reader.next()
    for row in reader:
    	movie_id[row[0]]=curr_id
    	curr_id+=1

no_movies=len(movie_id)

Y=np.zeros((no_movies+1, no_users+1))
np.set_printoptions(threshold=np.nan)
with open('data/ratings.csv') as r:
    reader = csv.reader(r, delimiter=",")
    reader.next()
    for row in reader:
    	Y[int(movie_id[row[1]])][int(row[0])]=float(row[2])


np.savetxt('Y_matrix.txt',Y, delimiter=',')