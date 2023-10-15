
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
x = complex(7+1j)
print(x)
x = range(6)
print(x)

print("*******Number types")
x = 1
y = -35.59
z = -3255522
w = 3+6j

a = float(x)
b = int(y)
c = int(w.real)
d = str(y)

print(type(x))
print(type(y))
print(type(z))
print(a,type(a),b,type(b))
print(c,type(c))
print(d,type(d))
print(w.real,type(w.real))
print(w.imag,type(w.imag))

print("*******Generate random number")
import random
for x in range(6):
  print(random.randrange(1, 10))


print("*******Multi-line string")
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)