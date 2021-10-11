from types import CodeType


# HASHING FUCNTION WILL GIVE A PARTICULAR INDEX FOR THE STRING AND WILL RETURN VALUE SMALLER THAN 100
# HERE WE WANT TO CREATE THE HASH TABLE WHOSE SIZE IS 100
# ord() FUCNTION WILL GET ASCII CODE FOR EVERY CHARACTER IN THE KEY AND ADD ALL THE CODE 
# LAST LINE MOD THE SUMM BY 100 TO MAKE NUMBER SMALLER THAN 100


def hashing(key):
    hash = 0
    for char in key:
        hash += ord(char)
    return hash % 100

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------


# CLASS HASH TABLE WILL CREATE HASHTABLE IN THE FORM OF ARRAY IN WHICH EACH INDEX OF ARRAY RESSEMBLES ON HASH NUMBER
class HashTable:  
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]


# GET HASH WILL GET HASH VALUE FOR THE KEY         
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    

# __getitem__ IS THE OVERWRITTEN OPERATOR OF PYTHON, IT RETURNS THE KEY AT PARTICULAR HASH INDEX     
    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]


# __setitem__ IS THE OVERWRITTEN OPERATOR OF PYTHON, IT ADD THE KEY AT PARTICULAR HASH INDEX
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    


# __delitem__ IS THE OVERWRITTEN OPERATOR OF PYTHON, IT DELETES THE KEY AT PARTICULAR HASH INDEX
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None



tab = HashTable()
tab["march 6"] = 310     #USES __getitem__() function
tab["march 7"] = 420     #USES __getitem__() function 
print(tab["march 6"])    #USES __setitem__() function

print(tab.arr)

