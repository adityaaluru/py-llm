print("Hello world!")
if 5 > 2:
    print("Five is greater than 2")
x = 5
y = "John"
print(type(x))
print(type(y))
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

x = 5
y = "John"
#This throws an error indicating no auto-typecasting 
# print(x+y)
print(x,y)

x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

print("*******Global and local variables")
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

print("*******Accessing global variable inside a function")
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

print("*******Checking types")
x = 5
print(type(x))

print("*******Complex type")
x = complex(7+1j)s
print(x)
x = range(6)
print(x)
