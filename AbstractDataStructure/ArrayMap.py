
class Item:

    def __init__(self, k, v):
        self.key = k
        self.value = v
    
    #print individual object
    def __str__(self):
        return f"{self.key}: {self.value}"
    
    #this method only needed if your object is in a list
    def __repr__(self):
        #you can use str(self)
        return f"{self.key}: {self.value}"
    
    #this method add to simplify the implementation of put
    def set_value(self, new_value):
        old_value = self.value
        self.value = new_value
        return old_value
    
class Map:

    def __init__(self):
        self.the_map = []
    
    "get the items from section inside the list and return value"
    def get(self, k):
        #O(n)
        for element in self.the_map:
            if element.key == k:
                return element.value
        return None
    
    #O(n) bad
    def remove(self, k):
        for i, element in enumerate(self.the_map):
            if element.key == k:
                #a list of element, pop (key, value)
                return self.the_map.pop(i) #remove() python
        #when the key is not in the map
        return None
    
    def put(self, k, v):
        #for lap
        for element in self.the_map:
            #when key exist
            if element.key == k:
                return element.set_value(v)
        self.the_map.append(Item(k,v))

    def __str__(self):
        list_str = "["

        for element in self.the_map:
            list_str += str(element) + ", "
        return list_str.rstrip(", ") + "]"

def main():
    #must implement str, and put
    m = Map()
    m.put(1, "Fluffy")
    m.put(2, "Snowball")
    m.put(3, "Spooky")
    m.put(4, "Killer")
    print(m)
    print(m.put(3, "Killer Jr"))
    print(m)

    m.remove(1)
    print(m)

if __name__ == "__main__":
    main()

