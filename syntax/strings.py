#string syntax

str = "Hello World"

beginning = str[:5] #this returns "Hello" because it travels from the beginning of the string up to but not including the 5th index (the space)

ending = str[6:] #this returns "World" because it starts at the 6th index and travels to the end of str

skipping = str[::2] #this returns "HloWrd" because it travels from beginning to end tracking every other number

#first parameter: optional, defaults to 0
#second parameter: optional, defaults to end
#third parameter: optional, defaults to 1

print str
print beginning + ending #notice the lack of space
print skipping
