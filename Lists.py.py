#Python Collection Data Types
#List : is mutable,
#Set
#Tuple
#Dictionary


letters=['a','b','c','d']
numbers=[1,3,5,7,9]
floats=[1.6,3.3]
zeroes=[0]*50



#access items in lists
print(letters[3])
print(letters[-4])
print(letters[0:2])

#in opeartor 
print('z' in zeroes)

#add to List
letters=['a','b','c','d']
letters.append('e')
letters.append('f')

print(letters)


#extend the list

uppercase_letters=['A','B']
letters.extend(uppercase_letters)
print(letters)
print(uppercase_letters)

#Remove from list
letters=['c','l','d']
letters.remove('l')

print(letters)

letters.pop()
print(letters)

del letters[0]

letters.clear() #deletes all the items in the list

#sort List
letters=['a','d','c','f','d']

letters.sort()
print(letters)

num=[1,5,0,3,9,7,6]

num.sort()
print(sum)

#copy List
letters=['p','q','r','s']
copy_letters=letters.copy()
copy_letters[-1]=['k']

print(letters)
print(copy_letters)

#Stack --LIFO
#Queue --FIFO

stack=[]

stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
stack.append('e')
print(stack)

print(stack.pop())
print(stack)

queue=[]
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)
queue.pop(1)
print(queue)