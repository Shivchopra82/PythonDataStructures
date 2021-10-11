# COLLISION IS A SITUATION WHEN HASHISH FUCNTIONS ASSIGN SAME INDEX FOR TWO KEYS 
# COLLISION CAN BE HANDLED BY CHANINING METHOD IN WHICH WE USE ARRAY OF ARRAY FOR STORING KEY VALUE 
# SUPPOSE A SITUATION IN WHICH TWO KEYS GET THE SAME INDEX 
# THEN BOTH THE KEY VALUE GET STORES IN THE SAME INDEX ARRAY IN THE FORM OF KEY VALUE TUPLE

class HashTable:  
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                return kv[1]


# __setitem__ FUNCTION FIRST CHECK IF THERE EXIST ANY KEY VALUE PAIR AT THAT INDEX 
# IF FOUND THEN IT WOULD APPEND ANOTHER TUPLE WITH THE KEY VALUE PAIR 
# IF IT FINDS THAT THE KEY GIVEN IN INPUT ALREADY EXIST IN THE ARRAY THEN IT WILL MODIFIES THE VALUE OF THAT PARTICULAR KEY     
      
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))
        

# __delitem__ THIS FUNCTION FIRST IDENTIFIES THE KEY VALUE TUPLE AND THEN PERFORM DELETION         
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, kv in enumerate(self.arr[h]):
            if kv[0] == key:
                print("del",index)
                del self.arr[h][index]



tab = HashTable()
tab["march 6"] = 310
tab["march 7"] = 420
tab["march 8"] = 67
tab["march 17"] = 63457

print(tab.arr)