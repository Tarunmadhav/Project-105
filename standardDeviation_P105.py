import math
import csv
with open("data_sd.csv") as d2:
    reader=csv.reader(d2)
    filedata=list(reader)
data=filedata[0]
def mean(data):
    l=len(data)
    total=0
    for i in data:
        total+=int(i)
    mean=total/l
    return mean
squaredlist=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squaredlist.append(a)
sum=0
for i in squaredlist:
    sum=sum+i
result=sum/(len(data)-1)
standardDeviation=math.sqrt(result)
print(standardDeviation)