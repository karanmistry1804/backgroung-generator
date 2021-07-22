#User input
# day1 = input("Enter date :")
# print(day)

day = input("Enter date:")
month = input("Enter month:")
year= input("Enter Year:")
print("class date {}/{}/{}".format(day,month,year))
print("class date {1}/{0}/{2}".format(day,month,year))


#if else statment

a=2
b=2

if a>b:
   print("A is less than B")
elif a==b:
    print("A and B are equal")
else:
   print("B is greater")

#Ternary OPeration
print('A') if a>b else print('B')
print('a') if a>b else print("a=b") if a==b else print('b')