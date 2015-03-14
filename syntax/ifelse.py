# Let's talk about if/else statements.
# While looking at this, it is important to remember your indents.
# While a tab is the same as 4 spaces, just use a tab.
# I've written some sample functions, feel free to test them out


def func(a):
    if (a < 0):
        return "a is less than 0"
    elif (a > 10):
        return "a is greater than 10"
    else:
        return "a is between 0 and 10 inclusive"

def func2(a, b):
    if (a < b):
        return "a is smaller than b. a equals: " + str(a)
    elif (b < a):
        return "b is smaller than a. b equals: " + str(b)
    else:
        return "a and b both equal: " + str(a)
print "Testing func() of -2, 5, and 15:"
print func(-2)
print func(5)
print func(15)
print "---------------"
print "Testing func2() of (0, 10), (10, 0), and (5, 5)"
print func2(0, 10)
print func2(10, 0)
print func2(5, 5)
