from ArraySet import ArraySet

#size of the set is unknow
#dynamic array grow

test_s = ArraySet()
#constructure we just write

test_s.add("COMP 1353")
test_s.add("GEOG 2020")
test_s.add("WRIT 1133")
test_s.add("ARTS 1250")
test_s.add("SPAN 2003")
test_s.discard("ARTS 1250")
#won't be added twice
test_s.add("COMP 1353")
print(test_s)

#true or false an element exist in the list
test_s.contains("COMP 1353")
print(test_s.contains("ARTS 1250")) #return false since it remove
#how to use union create new set
test_t = ArraySet()
test_t.add("BUS 1440")
test_t.add("ACT 2200")
test_t.add("COMP 1353")

test_3 = test_s.union(test_t)
#element double dip count once
test4 = test_s.intersection(test_t)
print(test_3)
print(test4)

#remove overlap
test_5 = test_s.difference(test_t)
print(test_5)