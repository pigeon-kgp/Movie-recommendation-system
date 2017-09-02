load('final_user.mat')
s=0
for i=1:size(Y,1)
	s+=sum(Y(i,:))

fprintf("\nFinal s is given to %d",s)