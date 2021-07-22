# syntax
# function_name = lambda parameters: operation

#Normally
def add(x,y):
    z=x+y
    return z

print(add(2,1.3))

sub = lambda x,y : x-y
print(sub(3,10))

##
cities = ["New York" , "LA" , "Chicago" , "Ahmedabad" , " Surat"]
def short(name):
    return len(name) <= 7

print(short("Surat"))

short_cities = list(filter(short,cities))
print(short_cities)

short = list(filter(lambda x:len(x)<=6,cities)) # Using lambda
print(short)

##
number = [[1,2,3,2],[2,4,6,1,2],[3,6,5,7],[1,2,1,2]]

def mean(num_lst):
    return sum(num_lst)/len(num_lst)

print(mean(number[3]))

average = (map(mean,number))
for i in average:
    print(i)
print(average)

average = (mean,number)    ## Using lambda
average = list(map(lambda x:sum(x)/len(x),number))
print(average)