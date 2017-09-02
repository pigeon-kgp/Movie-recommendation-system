import scipy.io as sio
import numpy as np
import operator
User_param = sio.loadmat('User_param.mat')

Movie_param = sio.loadmat('Movie_param.mat')
# Movie_param = file['Movie_param']

score = {}
final_user={}
for i in User_param:
    final_user[str(i)] = np.zeros((5,2))

# print(User_param['2438123'])
# exit_;
del Movie_param['__globals__']
del Movie_param['__version__']
del Movie_param['__header__']

print("list of movies length = ",len(Movie_param))

# print(" at 12143164",User_param['12143164'][0])
print("no of movies = ",len(Movie_param))

c=0
for user in User_param:        
    try:    
        params=User_param[str(user)][0]
    except Exception as e:
        print(" user param ",e," str(user)=",str(user)) 
        continue
    # print(" here user = ", user)
    # print(params)
    # print("\n\n\n\nDone printing user param")
    # exit_;
    for movie in Movie_param:
        try:
            movie_params = Movie_param[str(movie)][0]
        except Exception as e:
            print(" new error: ",e,"str(movie)=",str(movie))
            pass    

        score[str(movie)]=0
        for i in range(19):
            # print(score[str(movie)], "i=",i)
            try:
                r1=params[i]
            
                r2=movie_params[i]
            
                score[str(movie)] += r1*r2
            except Exception as e:
                pass

    sorted_x = sorted(score.items(), key=operator.itemgetter(1))
    count=0
    for i in sorted_x[-5:]:
        final_user[user][count][0] = int((i[0]))                #movie_id
        final_user[user][count][1] = int(i[1])
        count+=1
    print(" sorted_x = ",sorted_x[-5:])
    print("c = ",c," out of ",len(User_param))
    c+=1
    # print(" yo final user rating = ", final_user[user])
    # print(final_user[user])   
sio.savemat('rc_user', final_user)
print("Data saved")
