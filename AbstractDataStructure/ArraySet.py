

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
    
class ArraySet:
    "YOU SHOULD NEVER USE ARRAY AS DATA STRUCTURE FOR ARRAY SET"
    def __init__(self):
        # store the contents of the set in a python list,
        # which is itself a (dynamic) array
        self.the_set = []

    def __iter__(self):
        # made so easy since the contents are stored in a python
        #iter() python function for iterate an array        
        return iter(self.the_set)
    
    def __str__(self):
        result = "{"
        #element iteration
        for x in self.the_set:
            #every x convert to str()
            result += str(x) + ", "
        return result.rstrip(", ") + "}"
        #what is rstrip(", ")? get rid of the last comma

    def get_size(self):
        return len(self.the_set)

    def add(self, v):
        #check for no duplicate
        # add element to the end of the list)
        if v not in self.the_set:
            self.the_set.append(v)

    def discard(self, v):
        #no duplicates
        # a remove method which removes the first found element
        try:
            temp = self.the_set.remove(v)
            self.the_set.remove(v)
        #incase two element is pass through
        except:
            return temp

    def contains(self, v)->bool:
        #check the element is in the set
        return v in self.the_set

    def union(self, other): #the other set
        #all element
        new_set = ArraySet()
        for element in self.the_set:
            new_set.add(element)
        
        for element2 in other.the_set:
            #checking for duplicate
            new_set.add(element2)

        return new_set
    
    def intersection(self, other):
        #only the element in both set
        intersect_set = ArraySet()
        for element in self.the_set:
            if element in other.the_set:
                intersect_set.add(element)
        return intersect_set

    def difference(self, other):
        different_set = ArraySet()

        for element in self.the_set:
            if element not in other.the_set:
                different_set.add(element)
        return different_set


def main():
    set1 = ArraySet()
    set1.add(3)
    set1.add(5)
    set1.add(8)

    set2 = ArraySet()
    set2.add(9)
    set2.add(11)
    set2.add(5)

    print(set1.intersection(set2))
    print(set1.difference(set2))
    print(set1.union(set2))
if __name__ == "__main__":
    main()