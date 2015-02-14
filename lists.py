#lists are one of the ways that we can store a whole bunch of data

def first_element(list):
    return list[0]

#this returns the first element of list.

print "-------Testing List elements------------"
L1 = [1, 2, 3]
print first_element(L1) #should print 1
L2 = ['a', 'b', 'c']
print first_element(L2) #should print 'a'
print L1[2] #should print 3
#etc.

#Angela mentioned the range() function

print "-------Testing Range---------"
L3 = range(10)
print L3 #L3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] --> the integers between 0 and 9
L4 = range(4, 10)
print L4 #L4 = [4, 5, 6, 7, 8, 9] --> the integers between 4 and 9s