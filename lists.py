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
