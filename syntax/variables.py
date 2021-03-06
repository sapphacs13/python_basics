# Reminder:
# In python, you DO NOT need to tell the computer that you want to define
# an int or a string. You just write your definition.

a = 5
b = 7
print a # this will print 5
print b # this will print 7
print a + 10 # this will print 15
print a + b # this will print 12
b = "Hello World"
print b
# this will print 'Hello World'

# Remember that since a and b are not the same type, we cannot add them together
# to add a number and a string together, there are two easy options: (I am adding s + n + s2)

s = "I want to eat"
s2 = "cookies"
n = 5
s3 = s + str(5) + s2
print s3
# this will print 'I want to eat5cookies" because we did not put spaces in :) oops





#ignore the rest because it's not working
# another way (I am now adding s + s_num + s2 and they will all be strings):
#s_num = "" + n # this means s_num is now '5'
#s3 = s + s_num + s2
#print s3
# this will still print 'I want to eat5cookies'
