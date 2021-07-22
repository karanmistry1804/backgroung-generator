  
# Dictionary
# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.

dct={
     'bio':'hard worker',
     'name':'Karan Mistry',
     'age':19
     }
print(dct['name'])
print(dct)
print(type(dct))

#Accessing items
x=dct['bio']
print(x)

#Change values of existing items
dct['bio']='The learner'
print(dct)
dct['age']=21
print(dct)

#Print only dictionaries keys
print(dct.keys())

#Print only dictionaries values
print(dct.values())

#check whether the key is present in the dictionary or not
print('name' in dct)
print('address' in dct)

#To check values
print('bio' in  dct.values())

#To check lengh
print(len(dct))

#Add new items
dct['address']='Shree narnarayan Saw mill'
print(dct)

#Remove Items
dct.pop('address')
print(dct)

#Popitem to remove element from dictionary
dct.popitem()
print(dct)
dct.popitem()
print(dct)

# Remove using del
del dct['name']
print(dct)

del dct
print(dct)

#Empty type creation
dct.clear()
print(dct)

#copy a dictionary
new_dct=dct
print(id(new_dct))
print(id(dct))
new_dct=dct.copy()
print(new_dct)

#Nested Dictionary

avangers={
    "ironman":{
        "movies":{ 1:"Ironman",2:"Ironman 2",3:"Ironman 3"},
        "name":"Robert Downey Jr."
    },
    "Captan_America":{
        "movies":{1:"Captan America",2:"Captan Americam & Winter Soilder"},
        "name":"Chris Evans",
        "age":30
    },
    "Black_Widow":{
        "movies":{1:"Avangers",2:"Civil War",3:"Avangers:Age of Altron",4:"Avangers:Infinity War"},
        "name":"Scarllet Johnson"
    }
}

print(avangers)
print(avangers["ironman"])
print(avangers["Captan_America"]["name"])
print(avangers["Black_Widow"]["movies"][3])
print(avangers.get("ironman").get("movies").get(2))

#items 
print(avangers.items())

#keys
print(avangers.keys())
print(avangers.get("ironman").keys(),avangers.get("Captan_America").keys())

#Update Method
avangers["ironman"]["age"]=35
print(avangers["ironman"])

avangers.update({"Thor":{"movies":{1:"Thor",2:"Thor:Dark World",3:"Thor Ragnarok"},"name":"Chris Hemsworth"}})
print(avangers)