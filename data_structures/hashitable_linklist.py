## Creatin hash table:

class Hash_table:
    def __init__(self):
        self.max_value=100
        self.array=[[] for i in range(self.max_value)]
    
    def gethash(self,key):
        val=0
        for char in key:
            val+=ord(char)
        return val%self.max_value
        
    def __setitem__(self,key,value):
        hash_value=self.gethash(key)
        if len(self.array[hash_value])!=0:
            present=False
            for idx, val in enumerate(self.array[hash_value]):
                if val[0]==key:
                    self.array[hash_value][idx]=(key,value)
                    present=True
            if not present:
                self.array[hash_value].append((key,value))
        else:
            self.array[hash_value].append((key,value))
            
    def __getitem__(self,key):
        hash_value=self.gethash(key)
        if len(self.array[hash_value])!=0:
            for idx,value in enumerate(self.array[hash_value]):
                if value[0]==key:
                    return self.array[hash_value][idx][1]
        else:
            return 'Value does not exist'        
    def __delitem__(self,key):
        hash_value=self.gethash(key)
        for idx,value in enumerate(self.array[hash_value]):
            if value[0]==key:
                del self.array[hash_value][idx]
        

ht=Hash_table()
ht['march 6']=15
ht['march 8']=12
ht['march 16']=1
ht['march 17']=18





         