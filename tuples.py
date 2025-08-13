#Tuples -- is a immutable
#variable_name=(value1,value2,value3)


letters=('a','b','c')
numbers=(1,2,3)

print(letters)
print(numbers)

#Access Tuple value
print(letters[-1])
print(numbers[1])

print(letters[:-1])
print(numbers[::-1])

print( 'a' in letters)

upper_case=('A','B')
print(letters+upper_case)

weights=(2,3,4)
x,y,z=weights
print(x,y,z)

#sort

num=(1,9,0,8,7,3)
print(tuple(sorted(num)))


#delete
numbers=(1,3,4,5,6,7,9)

del numbers

print(numbers)