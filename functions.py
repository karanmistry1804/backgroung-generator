# syntax
# function definition

# DRY = Do Not Repeat Yourself

# def function_name(parameters):
# 	...code...
# 	...code...
# 	...code...
#
# function call
# function_name(parameters)

# function name should not be pre defined keyword

def operation_print():
    print("Jarvis Launch the suit")

operation_print()

#Return method in function
def return_method():
    return "Jarvis let's party"

print(return_method())


# Python follows DRY Priniciple  (Don't Repeat Yourself)

# Parameterized Function
# def op_para(num):
#     num=num/2
#     return num

# user_input=int(input("Enter a number:"))
# print(op_para(user_input))

#Global And Local Scope of variable
z=13 #Global variable
i=20 #Global variable
def operation_minus(y):
    #y is local variable
    global z
    z=i+y-z
    print(z)
    return(z)

operation_minus(20)
print(z)


# def calculator(x,y,z):
#     ans=x+y+z
#     print("Addition of x,y,z:",ans)
#     ans=x-y-z
#     print("Substraction of x,y,z:",ans)
#     ans=x*y*z
#     print("Multiplication of x,y,z:",ans)
#     ans=x/y/z
#     print("Division of x,y,z:",ans)
#     ans=x%y
#     print("Modulas of x&y:",ans)
#     ans=x//y
#     print("step division",ans)
    
# inp_x=int(input("Enter value of x:"))
# inp_y=int(input("Enter value of y:"))
# inp_z=int(input("Enter value of z:"))
# calculator(inp_x,inp_y,inp_z)

# Default Argument
def multiply(x=23,y=12):
    z=x*y
    print(z)

multiply()

#Population Density
def population_density(population=1000203,area=120302):
    density=population/area
    print(density)

population_density()


# FIND NUMBER OF WEEK AND WEEK_DAY FROM NUMBER OF DAYS
day_number=int(input("Enter no. of days:"))

def week_day(days):
    week=days//7
    day=days%7
    print("No. of week is {} and days are {}".format(week,day))

week_day(day_number)


