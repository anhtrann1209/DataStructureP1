import numpy as np
import random

class Node:
    def __init__(self, v, n):
        self.value = v
        self.next = n
    
    def __str__(self):
        return str(self.value)

class SinglyLinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __iter__(self):
        return SLLIterator(self.head)

    def is_empty(self)->bool:
        return self.head.next is None
    
    '''
    Method adds the value as the first node in the list
    returns nothing
    '''
    def add_first(self, v):
        #step 1: create a new node with value. Set its next
        #        to head reference
        new_node = Node(v, self.head)
        #Step 2: change the head to the new node
        self.head = new_node

        #step 3: increment the size
        self.size += 1
    def add_last(self, v):
        #add new node to as last element
        if self.head is None:
            self.add_first(v)
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(v, None)            
        self.size += 1

    def min(self):
        minimum_value = 0

        if self.head is None:
            raise ValueError("List is empty!")
        
        temp_node = self.head
        minimum_value = self.head.value

        while temp_node.next is not None:
            if temp_node.value < minimum_value:
                minimum_value = temp_node.value
            temp_node = temp_node.next
        return minimum_value


    '''
    Method removes the first node in the list and returns
    the value removed
    '''
    def remove_first(self):
        #case 1: list is empty
        if self.head is None:
            raise ValueError("List is empty!")
        
        #case 2: list has values
        value_to_return = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value_to_return
    
    def remove_last(self):
        if self.head is None:
            raise ValueError("List is empty!")
        
        temp = self.head

        if temp.next is None:
            removed_value = self.head.value
            self.head = None
            self.size -= 1
            return removed_value
        
        while temp.next is not None:
            temp = temp.next
        
        removed_value = temp.next.value
        temp.next = None
        self.size -= 1
        return removed_value
    
    def remove_at_index(self, index):
        #remove element giving the index
        if self.head is None:
            raise ValueError("List is empty!")
        
        if index == 0:
            return self.remove_first()        

        temp = self.head
        for i in range(index-1):
            if temp.next is None:
                raise IndexError("Index out of range")
            temp = temp.next

        if temp.next is None:
            raise IndexError("Index out of range")

        removed_value = temp.next.value
        temp.next = temp.next.next
        self.size -= 1
        return removed_value
    
    def get(self, index):
        #return value stored at given index
        if self.head is None:
            raise ValueError("List is empty!")
        if index < 0 or index >= self.size:
            raise IndexError("Index is out of range!")

        temp = self.head
        for _ in range(index):
            temp = temp.next

        index_value = temp.value
        return index_value

    def __str__(self):
        #if the list is empty return []
        if self.head is None:
            return "[]"
        
        #list is not empty
        s = "["
        #stop the loop when we reach the last node
        temp_node = self.head
        while temp_node.next is not None:
            s += str(temp_node) + ", "
            temp_node = temp_node.next
        
        return s + str(temp_node) + "]"
    def first_value(self):
        if self.head is None:
            return "No value"
        else:
            return self.head.next.value

class SLLIterator:
    #passing in the head
    def __init__(self, head):
        self.current = head
    
    def __next__(self):
        #advance pointer or next value
        if self.current is not None:
            value = self.current.value
            self.current = self.current.next
            return value
        #when value reach None
        raise StopIteration
    
    #why we need iterable method
    def __iter__(self):
        return self
    
class ArrayList:
    def __init__(self, N):
        #16 here is just open space for vacancy
        self.the_array = np.empty(N, dtype=object)
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

def hash_function(k, N):
    return k%N

def efficient_hash(k, N):
    return (((k*13)+5)%23)%N

sequence = [41, 28, 11, 82, 40, 75, 21, 0,  90, 52, 96, 70, 83, 98, 1, 43, 4, 85, 79, 87]
sequence_2 = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

efficient_function = [41, 28, 11, 82, 40, 75, 21, 0,  90, 52, 96, 70, 83, 98, 1, 43, 4, 85, 79, 87]
efficient_fucntion_2 = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
N = 20
array = ArrayList(N)

for i in range(N):
    array.append((SinglyLinkedList()))

for i, k in enumerate(efficient_fucntion_2):
    array.the_array[efficient_hash(k, N)].add_first(k)

print(array)
print(array.the_array[0])
print(array.the_array[10])


collision = 0
for element in array.the_array:
    if element.size >= 2:
        collision += element.size - 1
print(collision)

