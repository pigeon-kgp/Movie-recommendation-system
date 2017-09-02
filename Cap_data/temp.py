import numpy as np 
import scipy.io as sio

user_id=[1234,1456,1387,1354]
user_param={}

for id in user_id:
	user_param[str(id)]=np.zeros(19)

sio.savemat('test', user_param)
b=sio.loadmat('test')
print(b)
print("b done!")
print(user_param)	
