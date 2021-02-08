import json
import numpy as np 
import sys

with open("output/busout"+sys.argv[1]+".json", "r") as read_file: 
    data = json.load(read_file)

l = []
for m in data:
    l.append([m['sample']['day'],np.exp(m['lweight'])])
l=np.array(l)

l[:,1] /= np.sum(l[:,1])
print(np.sum([w for (y, w) in l if y==1 ]))
    


