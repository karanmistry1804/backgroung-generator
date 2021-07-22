# Python has two primitive loop commands:
#   1.while loops
#   2.for loops

b=[1,2,3]
b.insert(1,3)
print(b)

i=1
j=[]
while i in range(5):
    j.insert(0,2)
    i=i+1
print(j)

#Break Keyword
i=0
while i<5:
    if i==3:
        break
    else:
        i+=1
print(i)

for i in range(2):
    while i<6:
        print(i)
        if i==3:
            print(i)
            break
        i+=1

#continue Keyword
i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)

#else satatement

i=1
while i<6:

    if i==3:
        pass
    else:
        print(i)
    i=i+1
    

#for loop

# A for loop is used for iterating over a sequence data types
# (that is either a list, a tuple, a dictionary, a set, or a string).

# syntax
# for x in iterable:
#     code

# range(10)  start=0, stop=10,step=1
#range(7,10)  start=0, stop=10, step=1
#range(0,10,2) start=0, stop=10, step=2
# The range() function defaults to 0 as a starting value,
# however it is possible to specify the starting value by adding a parameter: range(2, 6),
# which means values from 2 to 6 (but not including 6):

for i in range(3):
    print(i)

for i in range(4,17,2):
    print(i)

#Numbers in reverse order
for i in range(10,-1,-1):
    print(i)

# With the for loop we can execute a set of statements, 
# once for each item in a list, tuple, set etc

marvel_heros=["ironman","Captan America","Black Widow","Hawkye","Thor"]
for x in marvel_heros:
    print(x)

#Looping of tuple
marvel_heros=("ironnman","Captan America","Black Widow")
for x in marvel_heros:
       print(x)

#Looping through string
for x in "ironman":
    print(x)

#Break the Statment
marvel_heros=["ironman","Captan America","Black Widow","Hawkye","Thor"]
for x in marvel_heros:
    print(x)
    if x=="Black Widow":
        break

for x in marvel_heros:
    if x=="Black Widow":
        break
    print(x)

#Continue statement
for x in marvel_heros:
    if x=="Black Widow":
        continue
    print(x)

#Else in for loop
for x in marvel_heros:
    if x=="Hawkye":
        break
    print(x)
else:
    print("Finally Finished")

# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be fully executed for each iteration of the "outer loop":
marvel_movies=["Avengers","Avengers:Civil War","Avengers:Age of Altron","Avengers:infinity War"]
marvel_heros=["Ironman","Captan America","Thor","hulk"]

for x in marvel_movies:
    for y in marvel_heros:
        print(x,y)

Marvel_capital=[]
for capital in marvel_heros:
    Marvel_capital.append(capital.capitalize())
print(Marvel_capital)
print(marvel_heros)

for i in range(len(marvel_heros)):
    marvel_heros[i]=marvel_heros[i].capitalize()
print(marvel_heros)

# The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
for i in range(len(marvel_movies)):
    marvel_movies[i]=marvel_movies[i].replace(':','_').title().split('_')
print(marvel_movies)

#Tag counter
lst=["<Mark 42>","Shield","<Arrows>","Vibranium Suit"]
count=0
for i in lst:
    if i[0]=="<" and i[-1]==">":
        count+=1

print(count)

n="Karan"
for i in n:
    print(i,end=" ")
print("\n")
#pattern
a=[1,2,3,4]
b=[0,1,2,3]
for i in a:
    for j in b:
        print(j+1,end=" ")
    print()


#Program to display student's marks record

marks={"Barney":94,"Ted":87,"Marshall":88,"Robin":70,"Lily":80}
std_name=input("Enter student name :")
for student in marks:
    if (student==std_name):
        print(marks[student])
        break
else:
    print("Student details not found!!")

# Building Dictionaries

#Method 1
word_lst=["Legendary","Awesome","Right","Suit Up","Legendary"]
word_counter={}
for word in word_lst:
    if word not in word_counter:
        word_counter[word]=1
    else:
        word_counter[word]+=1

print(word_counter)

#Method 2
word_lst=["Legendary","Awesome","Right","Suit Up","Legendary"]
word_counter={}

for word in word_lst:
    word_counter[word]=word_counter.get(word,0)+1
print(word_counter)

print(word_counter.items())
for key,values in word_counter.items():
    print(key,end=" ")
    print(values)


random_num = [2,3.11,7,5,1,4]
hand=[]
while sum(hand)<=20:
    print(random_num)
    print(hand)
    print("Sum_hand:",sum(hand))
    hand.append(random_num.pop())
else:
    print("Can't exceed more than 17")

#factorial using while loop
num=int(input("Enter a number:"))
fact=1
current=1
while current<=num:
    fact=fact*current
    current+=1
print("The factorial of ",num," is ",fact)

#factorial using for loop
fact=1
for x in range(1,num+1):
    fact=fact*x
print("Factorial of ",num," using for loop is ",fact)

#Nearest Perfect square
num=int(input("Enter a number:"))
number=1
nearest_square=0
while number**2<=num:
    nearest_square=number**2
    number+=1

print(nearest_square)

# Counting odd numbers ,sum of odd numbers and displaying odd numbers
num_lst=[3,2,5,6,7,8,22,11,13,100,24]
odd_lst=[]
lst_sum=0
count_odd=0
i=0
while i<len(num_lst):
    if num_lst[i]%2 != 0:
        odd_lst.append(num_lst[i])
        lst_sum+=num_lst[i]
        count_odd+=1
    i+=1
print("List of Odd numbers:",odd_lst)
print("Number of odd numbers:",count_odd)
print("Sum of list:",lst_sum)

