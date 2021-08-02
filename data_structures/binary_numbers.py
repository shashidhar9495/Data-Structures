from collections import deque

de=deque()
for i in range(0,6):
    if i==0:
        de.append(str(i+1))
    else:
        de.append(de[i-1]+str(0))
        de.append(de[i-1]+str(1))
        
print(de)       
        
    

