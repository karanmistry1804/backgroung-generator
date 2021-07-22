#SET
a = {1,2,3,'a'}
 #add item
a.add(5)
print(a)
 #add multiple items
a.update(['a',2,1,4,5])
print(a)
 #length of set
print(len(a))
 #Delete items
a.pop()
a.clear()
print(a)
 #Union Of Two Sets
set1 ={1,2,3}
set2 ={'a','b','c',3}
set3=set2.union(set1)
del set2
 #List to Set
lst=[1,2,3,3,3,3,3,3,5,5,2,2,2,2,6,6,7,4]
a= set(lst)
print(a)
 #type of set
a={1,2}
print(type(a))

#Dictionary

dct = {
    'bio' : 'abc',
    'name' : 'Karan',
    'age' : 18
 }
print(dct['name'])
print(dct)
dct['bio']='none'
print(dct)
print(dct.keys())
print(dct.values())
print('namne' in dct)
print('name' in dct.values())
print(len(dct))
dct.pop('name')
print(dct)
dct['name']='Karan'
print(dct)
dct.popitem()
print(dct)
del dct['age']

#clearing dectionory
print(dct)
dct.clear()
print(dct)

#clearing set
s={1,2,3,4}
s.clear()
print(s)

#print empty set
a=set()
print(a)
a.add(1)
print(type(a))

#empty dectionary
c=dict()   
print(c)
print(type(c))

#empty tuple
b=()
print(type(b))

#empty list
a=[]
print(type(a))

# nested dictionary
myfamily={

    "child1":{
        "name":{'name':'Karan','middlename':'Mistry'},
        "year":2002
    },
 "child2":{
        "name":{'name':'Karan','middlename':'Mistry'},
        "year":2002
    },
 "child3":{
        "name":{'name':'Karan','middlename':'Mistry'},
        "year":2002
    }
}

print(myfamily['child1']['year'])
print(myfamily.get('child1').get('name').get('middlename'))

child1={
        "name":{'name':'Karan','middlename':'Mistry'},
        "year":2002
    }
child2={
        "name":{'name':'Karan','middlename':'Mistry'},
        "year":2002
    }
child3={
        "name":{'name':'Karan','middlename':'Mistry'},
        "year":2002
    }
myfamily={
    "child1":child1,
      "child2":child2,
        "child3":child3,

}
print(myfamily.items())
car={
    'name':'lamborgani',
    'model':'Urus',
    'Price':'4.5crors'
}
print(car)
car.update({'name':'audi','model':'Etron','Price':'2crors','Manufacture':'Germany'})
print(car)