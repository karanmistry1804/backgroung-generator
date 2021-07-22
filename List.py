#List 
mylist=["I","Me","Myself"]
print(mylist)

#length of list
print(len(mylist))

#list can be of any data type
mylist=['112','karan',True]
print(mylist)

# Type 
print(type(mylist))

# list constructor
new_list=list(('Apple','Banana','Orange'))
print(new_list)


#ACCESSING LIST ITEMS
# #Access one item by index
marvel=["Ironman","Captan America","Black Widow","Thor","Hulk","Hawkye"]
print(marvel[4])

# Negative indexing .It starts from last item onthe list
print(marvel[-1])

#Range of indexes
print(marvel[2:5]) 
print(marvel[:4])
print(marvel[3:])

# Range of Negative indexes
print(marvel[-5:-1])

#Check if item exists in the list
if "Thor" in marvel:
    print('God of Thunder')

#CHANGE LIST ITEMS

#Change item value in the list
marvel[3]="Spiderman"
print(marvel)

# Change a Range of items
marvel[2:4]=["Antman","Falkon","Vison"]
print(marvel)

#Change the second and third value by replacing it with one value:
marvel[2:4]=["Winter soilder"]
print(marvel)

#ADD LIST ITEMS

#Insert items :The insert() method inserts an item at the specified index:
marvel.insert(4,"Spiderman")
print(marvel)

#Append items: To add an item to the end of the list, use the append() method:
marvel.append("Black Widow")
print(marvel)

# Extend List: To append elements from another list to the current list, use the extend() method.
dc=["Batman","Superman","Wonderwoman","Flash","Adam","Green Lentern"]
marvel.extend(dc)
print(marvel)

#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)
marvel=["Ironman","Captan America","Black Widow","Thor","Hulk","Hawkye"]
dc=("Batman","Superman","Wonderwoman","Flash","Adam","Green Lentern")
marvel.extend(dc)
print(marvel)

#REMOVE LIST ITEMS

# Remove specified item : The remove() method removes the specified item.
marvel.remove("Superman")
print(marvel)

#Remove Specified index: The pop() method removes the specified index.
marvel.pop(10)
print(marvel)

#If you do not specify the index, the pop() method removes the last item.
marvel.pop()
print(marvel)

#The del keyword also removes the specified index:
del marvel[0]
print(marvel)

#The del keyword can also delete the list completely.
del marvel

#Clear the list : The clear() method empties the list.
dc=["Batman","Superman","Wonderwoman","Flash","Adam","Green Lentern"]
dc.clear()
print(dc)

#LOOPING OF LIST

#Loop Through a list
marvel=["Ironman","Captan America","Black Widow","Thor","Hulk","Hawkye"]
for x in marvel:
    print(x)

#Loop Through the Index Numbers\
for x in range(len(marvel)):
    print(marvel[x])

#Using a while loop
i=0
while i<len(marvel):
    print(marvel[i])
    i+=1

#LIST COMPREHENSION 
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#THE SYNTAX: newlist = [expression for item in iterable if condition == True]

# Looping Using list Comprehension
[print(x) for x in marvel]

#Condition
newlist=[x for x in marvel if "man" in x]
print(newlist)

newlist=[x for x in marvel if "man" not in x]
print(newlist)

#Iterable 
newlist=[marvel[x] for x in range(len(marvel))]
print(newlist)

#Expression
newlist=[x.upper() for x in marvel]
print(newlist)

newlist=[x if x !="Captan America" else "Winter Soilder" for x in marvel]
print(newlist)


#SORTING OF LIST
#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

marvel.sort()
print(marvel)

#Sort Decending
marvel.sort(reverse=True)
print(marvel)

#Reverse Order
#What if you want to reverse the order of a list, regardless of the alphabet?
#The reverse() method reverses the current sorting order of the elements.

marvel.reverse()
print(marvel)

#Copy a List
marvel_update=marvel.copy()
print(marvel_update)

marvel_update=list(marvel)
print(marvel_update)

#JOINING OF LIST 
marvel=["Ironman","Captan America","Black Widow","Thor","Hulk","Hawkye"]
latest_marvel=marvel + marvel_update
print(latest_marvel)

marvel_update.extend(dc)
print(marvel)

