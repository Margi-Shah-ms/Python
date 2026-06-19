# write a program to demonstrate different formatting 
# options in print()
print("Hello", "to", "the", "world",sep="-") 

print("Hello", end=" ")
print("python") 

# # create a program that asks the user for their name,age,and 
# favorite hobby using the input() function, then displays a formatted 
# message like:
name = input("Name: ")
age = input("Age: ")
hobby = input("Hobby: ")
print("Hello,",name,"!","At", age,"enjoying",hobby,"sounds fun!") 

# perform addition, subtraction, multiplication, floor division, 
# modulus, and exponentiation 
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))  
# add
c= a+b
print(c)
# subtract 
d = a-b
print(d)
# multiplication
e = a*b
print(e)
# division
f = a//b
print(f)
# modulus
g = a%b
print(g) 

# write a python program that declares variables of different datatypes
# prints their values and types using the type() function 
a = 20
print(a,type(a))
b = 3.56
print(b,type(b))
c = "Hello"
print(c,type(c))
d = True
print(d,type(d))
e = 3+2j
print(e,type(e)) 

# height & weight 
# store them in appropriately named variables and print a formatted message displaying their values.
height = int(input("Enter Height:"))
weight = int(input("Enter weight:"))
print("Height:",height,"cm","Weight:", weight,"kg")  

# implement a program to demonstrate logical operators(and,or,not) by asking the user
# for boolean input 
a = input("Enter first value:")
b = input("Enter second value:")
print("A AND B=", a and b)
print("A OR B=", a or b)
print("NOT A=", not a)
print("NOT B=", not b)
    
# write a program to demonstrate assignment operators(=,+=,-=,*=,/=)
c = int(input("enter value:"))
a = c
print(a)
c+=5
print(c)
c-=5
print(c)
c/=5
print(c)  
c*=5
print(c)