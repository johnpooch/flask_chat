# With ints assignment automatically copies the value
x = 0
y = x
y += 1
print(x)

# With reference types like lists, assignment creates an alias to the same data
#Two variables reference the same list
x = []
y = x
y.append(1)
print (x)

#Copying a list and getting an actual copy
x = []
y = x[:]
y.append(1)
print (x)

