"""
Algorithms Analysis
Implement three algorithms function: sequential, binary search, and pointers. 
Time the function and analyze.
File Name: tran_projec2.py
Author: Anh Tran
Date: 4/20/24
Course: COMP1353 - Data Structures and Algorithms I
Assignment: Project 2 - Algorithm Analysis
Collaborators: Lisette Real Rico, Pluto Hassan.
"""
import random
import time
#both table and graph to Canvas
#three different algorithms that solve same problems
#compare their running times empirically, analyze them
#list sorted list of positive and negative integers(no zeroes)
#f(x) determine if there exist some value x such that x and -x are in the list.

"""ALGORITHM 1"""
#sequential search, examine one by one.
#check for both x and -x in the list
def sequential(list_int: list)->bool:
    """
    Function: Comparing one value in the list to the rest of the value but not itself.
    This process help to see if there exist an x value that exist as -x in the list.
    Parameter: list
    Return: True if 
    """
    for i in range(len(list_int)):
        for j in range(len(list_int)):
            if i != j:
                if list_int[i]*-1 == list_int[j]:
                    return True
    return False

"""ALGORITHM 2"""
#algorithm 2: binary search 
#pseudo-code TODO: 
#1. check if list empty, compute middle index: mid = (start+end)//2
#2. after comparing middle target. Values equal:return True. 
#3.target < list[mid] must search lower half set end to middle -1.
#target > list[mid] must search upper half so set start to mid+1.

def binary_search(list_int, target:int, start:int, end:int) -> bool:
    """
    Function: Find value in the list, if value exist in the top half, remove the other half.
    Continue the process until target found at the new middle index.
    Parameter: list, target:int, start:int=0, end:int=len(list_int)-1.
    Return: True if exist another x value as negative, else "False".
    """
    #slicing technique where mid place in list_int[mid] to check for value.
    mid = (start+end)//2
    #when end is not less than start iteration point.
    if start > end:
        return False
        #if mid division directly is target return True.
    #target is the number that passed from binsearch2

    if list_int[mid] == target:
        return True
    #if target exist in the first half of the first, move end point to number behind mid
    #[mid-1, mid]
    elif target < list_int[mid]:
        #past new part only loop from start to mid-1.
        return binary_search(list_int, target, start, mid-1)
    #target exist in second half of the array, move start to mid+1
    elif target > list_int[mid]:
        #the looping iteration go through mid+1 to size.array-1 and new end continue with slicing mid.
        return binary_search(list_int, target, mid+1, end)


def binary_search_2(list_int) -> bool:
    """
    Function: takes in integers list, loop through every integer and pass to binary search function.
    Pass to binary search function as negative value to find the -x while the value is x.
    Parameter: list
    Return: True if same integer different sign exist in the list, else "False".
    """
    #a list passed in.
    #called binarysearch for opposite value by take num*-1 and function finish if True x and -x exist.
    for num in list_int:
        #for every number in list_int
        if binary_search(list_int, -num, 0, len(list_int)-1) == True:
            return True
    #the opposite number of list value did not exist
    return False


"""ALGORITHM 3"""
#maintain index i and j. Initialize first and last element
#if two indexed sum is 0, then x has been found, other wise sum less than 0.
#advance i: sum > 0, then retreat j. 
#Repeatedly test sum until either x is found or i and j meet.
def pointers(list_int) -> bool:
    """
    Function: takes in sorted integers list, finding x and -x by looping i from right side, and j from left side.
    When sum of two value at i and j index equals to 0, then they are opposite of each other.
    Parameter: list
    Return: True when there exist negative number of an integer, else "False".
    """
    i = 0
    j = len(list_int)-1
    #i is starting j is ending index of the list
    while j > i:
        #only loop while j approach greater or == 0.
        sum = list_int[i] + list_int[j]
        #if found opposite value of an element which x and -x sum of it is 0. Return True
        if sum == 0:
            return True
        #if number are not alike, keep moving j down the array.
        elif sum > 0:
            j -= 1
        #if i= negative number larger than j positive number, return negative value -> loop i increase index.
        elif sum < 0:
            i += 1
    return False

def create_list(n:int) -> list:
    """
    Function: creates a random integer list with "n" element.
    Parameter: n: int
    Return: sorted random integers list.
    """
    randomint = []
    for _ in range(n):
        randomint.append(random.randint(100, 1000))
    randomint.sort()
    return randomint

def main():
    """
    Function: main function structure called outter function and measure time complexity.
    Parameter: None
    Return: (n, elapse time, run time)
    """

    print("SEQUENTIALS: ALGORITHM 1")

    print("n\t\tElapsed_Time\t\tRun_Time\t")
    trials = 2
    #vary input size in reasonable range
    #based on your application
    for n in (5000, 10000, 20000, 40000, 80000):
        #take a time snapshot at the start
        start = time.time()
        #repeat running the function num_trial times
        for i in range(trials):
            some_list = create_list(n)
            sequential(some_list)
        #take a snapshot time at the end 
        end = time.time()

        print(f"{n}\t\t{end-start}\t{(end-start)/trials}")
    
    print("BINARY SEARCH: ALGORITHM 2")

    print("n\t\tElapsed_Time\t\tRun_Time\t")
    trials = 200
    #vary input size in reasonable range
    #based on your application
    for n in (5000, 10000, 20000, 40000, 80000):
        #take a time snapshot at the start
        start = time.time()
        #repeat running the function num_trial times
        for i in range(trials):
            some_list = create_list(n)
            binary_search_2(some_list)

        #take a snapshot time at the end 
        end = time.time()

        print(f"{n}\t\t{end-start}\t{(end-start)/trials}")
    
    print("POINTERS: ALGORITHM 3")

    print("n\t\tElapsed_Time\t\tRun_Time\t")
    trials = 700
    #vary input size in reasonable range
    #based on your application
    for n in (5000, 10000, 20000, 40000, 80000):
        #take a time snapshot at the start
        start = time.time()
        #repeat running the function num_trial times
        for i in range(trials):
            some_list = create_list(n)
            pointers(some_list)

        #take a snapshot time at the end 
        end = time.time()

        print(f"{n}\t\t{end-start}\t{(end-start)/trials}")
if __name__ == '__main__':
    main()