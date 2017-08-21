f = open("data/movies.csv","r")
fout = open("data/my_movie_list","w")
import csv
lines = csv.reader(f, delimiter=',')
for line in lines:
	print line[1]
	fout.write(line[1]+"\n")