'''
Dictionaries are collection of values.used to store key value pairs

'''
#Define
data={
'name':'Pseudocode',
'course':'Python'
}

data={}
data=dict()

data2=dict(name='PSeudocoder',course='python')
print(data2)

#Access items in a dict
data={
'name':'Pseudocode',
'course':'Python'
}

#print(data['course'])

data.get('name',0)
print(data)