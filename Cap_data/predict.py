import numpy as np
import scipy.io
import csv
count=-1
f = open("final_rating.csv","w")

mat = scipy.io.loadmat('final_user.mat')
print(mat)
Y=mat['Y']
print("Y[0][0]",Y[0][0])
writer = csv.writer(f)
movie_params = np.array([[1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]])

mapping_users={}
with open('data/sample_solution.csv') as r:
    reader = csv.reader(r, delimiter=",")
    reader.next()
    print("count = ",count)
    for row in reader:
    	count+=1
    	if(count%5 ==0):
    		print("row[0] = ",row[0])
    		
    		mapping_users[(row[0])]=count/5
count=-1
imdb=[0,4,3.5,3,2.5,3]
with open('data/sample_solution.csv') as r:
    reader = csv.reader(r, delimiter=",")
    reader.next()
    print("count = ",count)
    for row in reader:
    	user_id=mapping_users[(row[0])]
    	count+=1
    	if(count%5==0):
	    	for movie_id in [1,2,3,4,5]:
	    		feat_param=Y[user_id]
	    		max_like=np.sum(feat_param)
	    		movie_param=movie_params[movie_id-1]
	    		score=np.matmul(feat_param,movie_param)
	    		print("score = ",score)
	    		if max_like==0:
	    			rating=imdb[movie_id]
	    		else:	
	    			rating = score*5.0/max_like
	    		if(rating<1):
	    			rating=1
	    		rating=(rating+imdb[movie_id])/2		
	    		rating*=2;
	    		rating=round(rating)
	    		rating/=2
	    		
	    		if(rating>5):
	    			rating=5
	    		rating=round(rating,1)	
	    		writer.writerow([user_id, movie_id, rating])



