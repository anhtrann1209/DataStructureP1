import numpy as np
import time
class ArrayList:
    def __init__(self):
        #16 here is just open space for vacancy
        self.the_array = np.empty(16, dtype=object)
        #initial size
        self.size = 0

    def __iter__(self):
        return ArrayIterator(self.the_array)
    
    def _expand_array(self):
        #step 1: create new array.
        new_array = np.empty(len(self.the_array) * 2, dtype = object)
        #step 2: this is copy value over only with self.array size value.
        for i in range(self.size):
            #for every i in new array copy value
            new_array[i] = self.the_array[i]
        #step 3: reassign the list to new
        self.the_array = new_array

    def append(self, v):
            if self.size == len(self.the_array):
                self._expand_array()
            #if the array is not fulled, then add new with insert made function.
            self.insert(self.size, v)

    def insert(self, index, v):
        #always check if the array if fulled or not.
        if self.size == len(self.the_array):
            self._expand_array()

        #index, where it want to insert
        #for element in reverse 654321
        for i in reversed(range(index, self.size)):
            self.the_array[i+1] = self.the_array[i]

        #loop through first element from the back.
        self.the_array[index] = v
        self.size += 1

    def __str__(self):
        r = "["
        for i in range(self.size-1):
            r += str(self.the_array[i]) + ","
        return r + str(self.the_array[self.size-1]) + "]"

#iterator you just make element to loop through
#parameter are things that needed for the loop.
class ArrayIterator:
    #iterator contain NEXT function where the loop happen.
    def __init__(self, array):
        self.array = array
        self.current_index = 0

    def __next__(self):
            if self.current_index < len(self.array):
                result = self.array[self.current_index]
                self.current_index += 1
                return result
            else:
                raise StopIteration
            
    def __iter__(self):
        return self


"Expanding the Array with just + 1000 element when list reaches it maximum" 
class ArrayListArithmetic(ArrayList):
    def __init__(self):
        ArrayList.__init__(self)
    
    def _expand_array(self):
        new_array = np.empty(len(self.the_array) + 1000, dtype = object)
        for i in range(self.size):
            new_array[i] = self.the_array[i]
        #step 3: reassign self.the_array
        self.the_array = new_array

    def append(self, v):
        self.insert(self.size, v)
        
    def insert(self, index, v):
        #check for capacity
        #note len(self.the_array) is the capacity
        if self.size == len(self.the_array):
            self._expand_array()
        
        for i in reversed(range(index, self.size)):
            self.the_array[i+1] = self.the_array[i]
        
        self.the_array[index] = v
        self.size += 1

"""trials = 400
    print(("Geometric Expansion"))

    print(f"n\t\telapsed_time\t\truntime")
    num_trial = 40
    for n in (100000, 200000, 400000, 800000):
        start = time.time()
        for j in range(num_trial):
        #create ArrayList
            geometric = ArrayList()
            for _ in range(n):
                geometric.append(n)
        #Append n elements
        stop = time.time()
        print(f"{n}\t\t{stop - start}\t\t{(stop - start)/num_trial}")

    print("Arithmetic Expansion")
    print(f"n\t\telapsed_time\t\truntime")
    trials = 5
    #it a tuple
    for n in (100000, 200000, 400000, 800000):
        start = time.time()
        for j in range(trials):
        #create ArrayList
            arithmetic = ArrayListArithmetic()
            for _ in range(n):
                arithmetic.append(n)
        #Append n elements
        stop = time.time()
        print(f"{n}\t\t{stop - start}\t\t{(stop - start)/trials}")
"""
        
def main():
    #number of trials ArrayList(100)
    l = ArrayList()
    for i in range(5):
        l.insert(0, i+1)
    
    for num in l:
        print(num)

if __name__ == "__main__":
    main()