class Binarytree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
    def add_child(self,data):
        if data==self.data:
            return
        if data<self.data:

            if self.left:
                self.left.add_child(data)
            else:
                self.left=Binarytree(data)
        else:

            if self.right:
                self.right.add_child(data)
            else:
                self.right=Binarytree(data)
            
    def get_elements(self):
       elements=[]
       if self.left:
           elements+=self.left.get_elements()
       elements.append(self.data)
        
       if self.right:           
           elements+=self.right.get_elements()
       return elements
     
    def get_max(self):
        if self.right is None:
            return self.data
        if self.right:
            return self.right.get_max()
    
    def get_min(self):
        if self.left:
            return self.left.get_min()
        if not self.left:
            return self.data
    
    def del_element(self,val):

        if val<self.data:
            if self.left:
                self.left= self.left.del_element(val)
        elif val>self.data:
            if self.right:
                self.right=self.right.del_element(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            max_val=self.left.get_max()
            self.data=max_val
            self.left=self.left.delete(max_val)

    def search_element(self,val):
        if val == self.data:
            return True
        elif val<self.data:
            if self.left:
                return self.left.search_element(val)
            else:
                return False
        elif val>self.data:
            if self.right:
                return self.right.search_element(val)
            else:
                return False
            



           
root=Binarytree(15)
req_list=[12,13,18,18,1,19]

def build_tree(elements):
    for i in elements:
        root.add_child(i)
    
    return root
    
tree= build_tree(req_list)  
sorted_array=tree.get_elements()
min_val=tree.get_min()
max_val=tree.get_max()
del_array=tree.del_element(18)



