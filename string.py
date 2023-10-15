print("********* String is an array")
a = "Hello, World!"
print("First character",a[0])
print("Length of the string",len(a))

print("********* Looping characters in string")
for x in "banana":
  print(x)

print("********* Checking for sub-strings in a string")
txt = "The best things in life are fre!"
print("free" in txt)
print("free" not in txt)