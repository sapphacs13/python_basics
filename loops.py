# for loops
def print_list_for(L):
    for i in L:
        print i
print "-------print 0-9 in a for loop--------"
print_list_for(range(10))
#while loops

def print_list_while(n):
    i = 0
    while (i < n):
        print i
        i = i + 1

print "-------print 0-9 in a while loop--------"
print_list_while(10)
