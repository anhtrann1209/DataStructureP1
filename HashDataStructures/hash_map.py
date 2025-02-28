from LINKLIST.doublell import DoublyLinkedList, DLLIterator 
from random import randint, random, choice
import numpy as np

class Item:
    def __init__(self, k, v):
        self.key = k
        self.value = v

    
    def __str__(self):
        return f"{self.key}: {self.value}"
    
    def __repr__(self):
        return str(self)
    
    def set_value(self, new_value):
        old_value = self.value
        self.value = new_value
        return old_value

class HashMap:
    PRIMES = (25165843, 50331653, 100663319, 201326611, 402653189, 805306457, 1610612741)

    def __init__(self):
        self._init_table(16)

    def _init_table(self, new_capacity):
        self.the_table = np.empty(new_capacity, dtype=DoublyLinkedList)
        self.prime = choice(HashMap.PRIMES)
        self.a = randint(1, self.prime-1)
        self.b = randint(0, self.prime-1)
        self.size = 0

        #create all the buckets
        for i in range(len(self.the_table)):
            self.the_table[i] = DoublyLinkedList()

    def _expand_table(self):
        #store the items in the table
        #store all items in a list to make copy to new list
        item_list = self.items()
        #Initialize a table with twice the number of buckets
        self._init_table(len(self.the_table)*2)

        #Store the items in the new table
        for element in item_list:
            self.put(element.key, element.value)
                
    def _hash_and_compress(self, k):
        return ((hash(k) * self.a + self.b) % self.prime) % len(self.the_table)
    
    def get(self, k):
        #get the index of the bucket where key could exist
        index = self._hash_and_compress(k)
        #get the bucket (DLL)
        bucket = self.the_table[index]
        #iterate over the keys and return value if key is found
        for item in bucket:
            if item.key == k:
                #the whole value lists
                return item.value
        return None

    def put(self, k, v):
        index = self._hash_and_compress(k)
        bucket = self.the_table[index]
        #itearte over the keys
        for item in bucket:
            #if we find the key
            if item.key == k:
               #replace the old value with the new and return the old value
               return item.set_value(v) 
            
        if (self.size / len(self.the_table)) > 0.75:
            self._expand_table()

        new_item = Item(k, v)
        bucket.add_first(new_item)
        self.size += 1
        
        #Check if we need to expand the table here
        
        return None

    def remove(self, k):
        index = self._hash_and_compress(k)
        bucket = self.the_table[index]

        for item in bucket:
            if item.key == k:
                return bucket.remove_value(item)
        return None

        
    #iterable methods
    def keys(self):
        #create an iterable
        the_keys = []

        #iterate over the buckets
        for bucket in self.the_table:
            #iterate over the items
            for item in bucket:
                #append the key to iterable
                the_keys.append(item.key)
        return the_keys

    def values(self):
        return [item.value for bucket in self.the_table for item in bucket]

    def items(self):
        return [item for bucket in self.the_table for item in bucket]

    #size methods
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    #Make my HashMap Iterable
    def __iter__(self):
        return iter(self.keys())
    
    #print methods
    def __str__(self):
        return str(self.items())

    def output_table_info(self):
        max_bucket_size = 0
        for i in range(len(self.the_table)):
            print(f"{i}: {self.the_table[i]}")
            if self.the_table[i].size > max_bucket_size:
                max_bucket_size = self.the_table[i].size

        print("Size of largest bucket: ", max_bucket_size)
        print("Table size: ", self.size)
        print("Load factor: ", self.size / len(self.the_table))



def main():
    # map = HashMap()
    map = HashMap()
    with open("baby_names2016.txt", "r") as a_file:
        for line in a_file:
            data = line.strip().split(" ")
            if map.get(data[0]) is None:
                map.put(data[0], data[1])
            else:
                map.put(data[0], data[1] + map.get(data[0]))
    map.output_table_info()
    # print(map.remove("Jericho"))
    print("TO GET JERICHO ")
    print(map.get("Jericho"))
    print("Remove JERICHO")
    print(map.remove("Jericho"))
    print("GET JERICHO AGAIN")
    print(map.get("Jericho"))

if __name__=="__main__":
    main()






































