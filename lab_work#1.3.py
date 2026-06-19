# write a python to demonstrate the use of type casting constructors (int(),
# flot(), str(),and bool())
# take input from  the user as a string
# convert the string into an integer, a float, and a boolean.
# print the converted vlues along with their types
a = input("enter:")
b = int(a)
print(b,type(b))
c = float(a)
print(c,type(c))
d = bool(a)
print(d,type(d))

# write a program where the user inputs a floating point number
# convert this number into an integer using int() and print both values with
# a message explaining the difference
a = float(input("enter:"))
z = int(a)
print(a,"It shows real numbers with decimal points","\n",z,"It shows a whole number without decimal") 

# create a program that: 
# takes a boolean value (true or false) as input
# converts the boolean to an integer and a string and prints all 3 values.
a = bool(input("enter true or false:"))
b = int(a)
c = str(a)
print(a)
print(b)
print(c)

# write a python program to:
# declare a variable of each datatype(int, float, string, boolean, list,tuple,dictionary)
# print the value, type(using type()), and memory address (using id()) of each variable
a = 10
print(a,type(a),id(a))
b = 3.25
print(b,type(b),id(b))
c = "hi"
print(c,type(c),id(c))
d = True
print(d,type(d),id(d))
e = [1,2,3,4,5]
print(e,type(e),id(e))
f = (1,2,3,4)
print(f,type(f),id(f))
g = {'a':1,"b":2}
print(g,type(g),id(g))  

# create a program that: 
# declares two variables with the same value
# print their memory addresses using id() and checks if they are the same
# modifies one of the variables and checks the memory addresses again

a = 10
b = 10
print(a,id(a))
print(b,id(b)) 

# modifying one of the variable:
a = 11
b = 10
print(a,id(a))
print(b,id(b))