# Zip

#  zip returns iterator that combines multiple iterables into
# one sequence of tuples
# ('a',1),('b',2),('c',3)

marvel_heros=["Ironman","Captan America","Black Widow","Hulk"]
heros_name=["Robert Downey Jr.","Chris Evans","Scarllet Johnson","Mark Buffalo"]
hero_roles=zip(marvel_heros,heros_name)
print(hero_roles)

for marvel_heros,heros_name in hero_roles:
    print(marvel_heros,":",heros_name)

# Unzip
marvel_movies=[("Ironman","Robert Downey Jr."),("Captain America","Chris Evans"),("Black Widow","Scarllet Johnson"),("Hulk","Mark Buffalo")]
marvel_heros,heros_name=zip(*marvel_movies)
print(marvel_heros)
print(heros_name)

for i in marvel_heros:
    print(i)


# Enumerate Function
# Enumerator is a built in function that returns an generator
# of tuples containing indices and value of list

marvel_heros=["Ironman","Captan America","Black Widow","Hulk"]
print(enumerate(marvel_heros))
for x,y in enumerate(marvel_heros):
    print(x,y)



# use zip to write for loop that creates string specifying the label and
# co-ordinates of each point and appends it to the list points.
# each string should be formatted as 'label:x,y,z'
# a:23,56,12

x_coord=[22,12,1]
y_coord=[31,11,21]
z_coord=[11,21,33]
lables=["a","b","c"]
zip_coord = zip(lables, x_coord, y_coord, z_coord)

print(zip_coord)
points = []
for point in zip_coord:
    print(point)

for point in zip_coord:
    print("{}:{},{},{}".format(*point))

for point in zip(lables,x_coord,y_coord,z_coord):
    points.append('{}:{},{},{}'.format(*point))

print(points)
for i in points:
    print(i)


# Zip to craete dictionary

marvel_heros=["Ironman","Captan America","Black Widow","Hulk"]
heros_name=["Robert Downey Jr.","Chris Evans","Scarllet Johnson","Mark Buffalo"]
hero_roles=dict(zip(marvel_heros,heros_name))
print(hero_roles)
print(hero_roles.items())

# Zip to create List
hero_roles=list(zip(marvel_heros,heros_name))
print(hero_roles)

# Zip to create Tuple

hero_roles=tuple(zip(marvel_heros,heros_name))
print(hero_roles)
print(zip(marvel_heros,heros_name))
for i in hero_roles:
    print(i)

# Unzip  tuple
hero_roles=(("Ironman","Robert Downey Jr."),("Captan America","Chris Evans"))
role,name=zip(*hero_roles)
print(role,name)


names=["Barney","Robin","Ted"]
height=[73,80,75]

for i,name in enumerate(names):
    print(i,name)

for i,name in enumerate(names):
    names[i]=name+" "+str(height[i])

print(names)