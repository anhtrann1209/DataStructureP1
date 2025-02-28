
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

def main():
    sll = SinglyLinkedList()

    for i in range(10):
        sll.add_first(i+1)
    #use iterator with content based loop
    for item in sll:
        print(item)
    
    print("Using iterator object!")
    iterator = iter(sll)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break
    
    #Using the iterator as an iterable
    "Create new one since it cannot start over."
    print("Element iterator:")
    iterator = iter(sll) 
    "This loop can only be used if the Iterator have the _iter_ method."
    for value in iterator:
        print(value)
    

#The following is the main code block:
if __name__ == "__main__":
    main()