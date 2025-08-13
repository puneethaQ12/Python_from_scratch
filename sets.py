'''
sets are collection of values.used to store multiple values
sets are Unordered
'''

#Define set
letters={'a','n','s','s'}
print(letters)

numbers=set([1,2,3])
print(numbers)

#Access items
letters={'a','n','s','s'}

#print(letters[0]) # in this case we use the in opeartor
print('s' in letters)

#Add to set
numbers={1,2,3,4}
decimals={1.2,2.9,9.8}

decimals.add(6)
numbers.add(5)
print(numbers)
print(decimals)

#remove from set
letters={'a','b','c','d'}

letters.remove('a')
letters.discard('c')
letters.pop()
letters.clear()  #remove the all the items in the set

print(letters)

#Join Sets
odd={1,3,5}
even={2,4,6}

combined=odd.union(even)
odd.update(even)
print(odd)
print(even)
print(combined)

#keep Duplicates Only
num1={1,2,3,4,5,6,8}
num2={2,4,5,6,7}

inter=num1.intersection(num2)
print(inter)

#distinct values only
#numbers=num1.symmetric_difference(num2)
#print(numbers)

numbers=num1.symmetric_difference_update(num2)
print(numbers)
