
class HashTable:

    def __init__(self) :
        self.MAX = 10
        # Initializing an empty array of given Max size
        self.arr = [None for i in range(self.MAX)]

    # Creating hash Function to hash the keys 
    def hashFunction(self,key):
        
        summation=0
        for  i  in key:
            asciiValue = ord(i)
            summation+=asciiValue
        
        return summation%self.MAX


    # # Addition of Item in the hash table
    # def addItem(self,key,value):
        
    #     # get the key from the given item

    #     # call the hash function and pass the key to it
    #     index = self.hashFunction(key)
        
    #     # after receiving the value from the hash table , assign the given item to that particular index
    #     self.arr[index] = value 


    # # Get the item from the hash table

    # def getItem(self,key):
        
    #     # call the hash function and get the key
    #     index = self.hashFunction(key)

    #     # access the element from the hashtable using the index

    #     return self.arr[index] 


    def __setitem__(self,key,value):
               
        # call the hash function and pass the key to it
        index = self.hashFunction(key)
        
        # after receiving the value from the hash table , assign the given item to that particular index
        self.arr[index] = value

    def __getitem__(self,key):
        
        # call the hash function and get the key
        index = self.hashFunction(key)

        # access the element from the hashtable using the index

        return self.arr[index] 


# Driver Code
hashTable = HashTable()

hashKey = hashTable.hashFunction("March 2020")


# # Adding item to the hashTable
# hashTable.addItem("March 2020",300)
# hashTable.addItem("March 2021",560)
# hashTable.addItem("March 2022",780)
# hashTable.addItem("March 2023",850)

# # Getting Item from HashTable
# value1 = hashTable.getItem("March 2020")

# print(hashTable.arr)

# print(value1)

# Setting the item in the hashtable
hashTable["March 2020"] = 300

# getting the item from the hashTable
print(hashTable["March 2020"])






