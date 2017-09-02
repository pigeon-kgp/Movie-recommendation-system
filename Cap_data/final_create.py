import pandas as pd
import numpy as np
import scipy.io
import operator
file = pd.read_csv('data/movies.csv')
movie_ids = file['movieId']
features = file['genres']
features_mapping={}
Matrix = np.zeros((len(movie_ids), 19))

features_mapping['Action']=0
features_mapping['Adventure']=1
features_mapping['Comedy']=2
features_mapping['Children']=3
features_mapping['Animation']=4
features_mapping['Horror']=5
features_mapping['Drama']=6
features_mapping['Romance']=7
features_mapping['Thriller']=8
features_mapping['Crime']=9
features_mapping['Fantasy']=10
features_mapping['Sci-Fi']=11
features_mapping['Mystery']=12
features_mapping['IMAX']=13
features_mapping['War']=14
features_mapping['Documentary']=15
features_mapping['Musical']=16
features_mapping['Film-Noir']=17
features_mapping['Western']=18

Matrix={}
count=0
for id in movie_ids:
	
	Matrix[str(id)] = np.zeros(19)
	for feature in features[count].split('|'):
		try:
			Matrix[str(id)][features_mapping[feature]]=1
		except Exception as e:
			print(e)	
	count+=1		

# scipy.io.savemat('Movie_param', Matrix)

# file.close()
file = pd.read_csv('data/sample_solution.csv')
final_users = set(file['userId'])
final_movie_id = np.zeros(len(final_users))
final_rating = np.zeros(len(final_movie_id))
User_param={}
for user in final_users:
	User_param[str(user)]=np.zeros(19)

scipy.io.savemat('User_param', User_param)
file = pd.read_csv('data/training.csv')
total_users = file['userId']
rating = file['rating']
movieId = file['movieId']
for i in xrange(len(total_users)):
	# count=0
	user_id = total_users[i]
	if user_id in final_users:
		movie_id = movieId[i]
		rating_ = rating[i]-3
		# print(User_param[str(user_id)], " rating ",rating_, " was rating ")
		# print(rating_*Matrix[movie_id_mapping[movie_id]])
		# print("done")
		User_param[str(user_id)] += (rating_*Matrix[str(movie_id)])
	if(i%1000==0):
		print(i*100.0/len(total_users))

scipy.io.savemat('User_param', User_param)
scipy.io.savemat('Movie_param', Matrix)
# print(User_param)
print("no of movies = ",len(Matrix))

print(User_param)
print("Data saved")
# print(Matrix)


