#Data Structures

#Strings
name="Pseudocode shrija Python Programming course"

#length of the string
print('Length of the string:',len(name))

#Access the character in the string
print(name[-8])

#String slicing
#start=0
#end=n+1
print(name[1:5])

#Reverse a string in place
print(name[::-1])

#concat the string
str1="hello"
str2="2025"
year=2023
print(str1+''+str2)
print(str1+str(year))

#string Methods

#1.lower(),upper()
name="Pseudocode shrija Python Programming course"
print(name.lower())
print(name.upper())

#2.strip(),lstrip(),rstrip()

name =' Animal '
print('['+ name.strip() +']')
print('['+ name.lstrip() +']')
print('['+ name.rstrip() +']')

#3.isalpha()
name='Parrot'
print(name.isalpha())

#4.isdigit()
numb='67789'
print(numb.isdigit())

#5.isspace()
name=' '
print(name.isspace())

#6.format
#hello 2026,bye 2025
oldyear=2025
newyear=2026

output='hello {0},bye {1}'
print(output.format(oldyear,newyear))

#7.find()

name='RAvina' 

print(name.find('R'))

#8.replace()
msg='the one is the one with two or one sentences'
print(msg.replace('one','ten',2))

#9.startwith()
name='start stop'
print(name.startswith('stop'))

#10.endswith()
name='start stop'
print(name.endswith('stop'))