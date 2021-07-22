#if_else statment
# Python supports the usual logical conditions from mathematics:
#
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# An "if statement" is written by using the if keyword.

# syntax
# if condition:
# 	o/p code

a=21
b=112
if a<b:
    print("a is less than b")

a=211
b=321
if b>a:
    print("b is greater than b")

#if else
a=11
b=22
if a>b:
    print('a is greater than b')
else:
    print('b is greater than a')

#elif
a=22
b=11

if a>b:
    print('a is greater')
elif b>a:
    print('b is greater')
else:
    print('a and b are equal')

#shortend or ternary operators
a=20
b=10
print('A') if a>b else print('B')

#Logical operations

#AND Operation
a=22
b=10
c=29
if (a>b and a>c):
    print('a is greater')
elif (b>a and b>c):
    print('b is greater')
else:
    print('c is greater')

#OR Operation
a=23
b=54
c=23
if (a>b or c<b):
    print('At least one condition is true')
else:
    print('None of the condition is true')

#NESTED IF
x=21
if x>10:
    print('Above 10')
    if x>20:
        print('Above 20')
    else:
        print('not above 20')
else:
    print('Not above ten')

#Pass statement is used when there is no need of output

a=23
b=200
if b>a:
    pass


# # Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# c=int(input("Enter c:"))

# if (a==b==c):
#     print(3*a)
# else:
#     print(a+b+c)

# # Write a Python program to test whether a passed letter is a vowel or not.
# char=input('Enter a character:')
# if char in ['a','e','i','o','u']:
#     print("Enetred character is a vowel")
# else:
#     print("Entered character is not a vowel")

# # Write a Python program to check whether a specified value is contained in a group of values.
# num_list=[22,122,33,21,11]
# num=int(input("Enter a number:"))
# if num in num_list:
#     print("Entered number is present in the list")
# else:
#     print("Entered number is not present in the list")

# Write a Python function to find the maximum and minimum numbers from a sequence of numbers
num_list=[2,3,54,22,-7,-1,32]
min=num_list[0]
max=num_list[0]
for num in num_list:
    if num <= min:
        min=num
    if num >= max:
        max=num
print(min,max)