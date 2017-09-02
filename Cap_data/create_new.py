import csv
import numpy as np, scipy.io

user_ids=[]
movie_ids=[]
rating=[]
curr_id=1
count=-1
mapping_movies={} # mapping[their_id]=our_posn
mapping_users={}  # mapping[their_id]=our_posn

final_user=[]

f = open("data/movies.csv","r")

# alltext = f.read()

spamreader = csv.reader(f)

spamreader.next()

all = dict()


features={}
features['Action']=0
features['Adventure']=1
features['Comedy']=2
features['Children']=3
features['Animation']=4
features['Horror']=5
features['Drama']=6
features['Romance']=7
features['Thriller']=8
features['Crime']=9
features['Fantasy']=10
features['Sci-Fi']=11
features['Mystery']=12
features['IMAX']=13
features['War']=14
features['Documentary']=15
features['Musical']=16
features['Film-Noir']=17
features['Western']=18


for spam in spamreader:

    try:

        all[spam[0]]=spam[2].split('|')

        # feat.extend(spam[2].split('|'))

        # print spam[2]

    except:

        pass

with open('data/sample_solution.csv') as r:
    reader = csv.reader(r, delimiter=",")
    reader.next()
    print("count = ",count)
    for row in reader:
    	count+=1
    	if(count%5 ==0):
    		print("count = ",count)
    		final_user.append(int(row[0]))
    		mapping_users[(row[0])]=count/5

print("final user = ",len(final_user))
Y=np.zeros((int(len(final_user)), 19))

print("Going to read training data")
with open('data/training.csv') as r:
    reader = csv.reader(r, delimiter=",")
    reader.next()
    print("count = ",count)
    for row in reader:
    	if(int(row[3]) in final_user):
    		movie_id=int(row[0])
    		feat=all[str(movie_id)]
    		for f in feat:
    			try: 
    				our_id=int(mapping_users[(row[3])])
    				# print("our id = ",our_id)
    				# print("features(f) = ", int(features[f]))
    				Y[int(mapping_users[(row[3])])][int(features[f])]+=1;
    				# print("Y[",our_id,"][",int(features[f]),"] now has value",Y[int(mapping_users[(row[3])])][int(features[f])] )
    			except Exception as e:
    				print("in except",e)
    				pass	


scipy.io.savemat('final_user', mdict={'Y':Y})    				
np.savetxt('f_user.txt',Y, delimiter=',')
