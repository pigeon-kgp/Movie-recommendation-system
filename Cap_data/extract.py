import scipy.io as sio
import numpy as np
import pandas as pd
User_param = sio.loadmat('rc_user.mat')

del User_param['__globals__']
del User_param['__header__']
del User_param['__version__']
user_id=[]
movie_id=[]
rating=[]
print(User_param)
# exit_;
for user in User_param:
	print("user = ",user)
	try:
		M=User_param[user]
		for j in range(5):
			user_id.append((user))
			movie_id.append((M[j][0]))
			if(M[0][1]!=0):
				r = (M[j][1]*4.0/M[0][1])
			else:
			    r=1	
			if(4<r<4.5):
			  r=4
			if(5>r>4.5):
			  r=4.5    
			if(r>5):
				r=5
			rating.append(r)
	except Exception as e:
		print("Error: ",e)		
df = pd.DataFrame([[0,0,0]], columns=['userId','movieId','rating'])

print(" len of user_id = ",len(user_id)/5.0)
for i in xrange(len(user_id)):
	try:
		temp = pd.DataFrame([[int(user_id[i]), int(movie_id[i]), round(rating[i], 1)]], columns=['userId','movieId','rating'])	
		df=df.append(temp)
	except Exception as e:
		print("Final: ",e)
		continue	
print(df)
df.to_csv('test_.csv')	