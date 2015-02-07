# Python uses white space. Everything you define or use has
# to have the correct indentation.

def adder(a, b):
    return a + b

print adder(1, 2) # runs adder(1,2) and prints it (should print 3)

def subtracter(a, b):
    return a - b

print subtracter(3, 2) # runs the subtracter and prints (should print 1)

# lets talk about the difference between print and return
def adder2(a, b):
    print a + b

adder2(1, 2) # prints 3.
# Notice how we dont need to print this we only need to call it.
# The downside is that we cannot save a variable like a = adder2(4, 5).
# This is because the function only prints, it does not save anything.
# Looking at the first adder function however:

a = adder(4, 5)
print a
# prints 9
