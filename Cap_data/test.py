import csv
threat=0
us_id=[]
with open('test_.csv') as r:
    reader = csv.reader(r, delimiter=",")
    reader.next()
    flag=0
    count=0
    li=[-1]
    for row in reader:
        # print(row)
        if(count%5==0):
            flag=0
            print(li)
            li=[-1]
         
        if(int(row[1]) in li):
            threat+=1
            flag=1
            us_id.append(int(row[0]))
        else:
            print(int(row[1]))
            print("before appending li=",li)
            li.append(int(row[1]))
            print("after appending li=",li)    
        count+=1       
print(threat)     
print(us_id)          

        