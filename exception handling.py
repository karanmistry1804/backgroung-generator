# Try _ Except _ Else _ Finally

# try: It is only mandatory clause in exception handling.try runs first in
# 	try__except

# except: if python runs into an exception, then code present in except
# 		will run.

# else:  if try is successfully executed then after execution of try block else part
# 		will execute.

# finally:  this part always runs.

#Try_Except
x = int(input("Enter a number"))
print(x)
try:
    x = int(input("Enter a number:"))
    print(x)
except:
    print("Enter a valid number")



#Try_Except_else_finally
try:
    x = int(input("Enter a number:"))
    print(x)
except:
    print("Invalid number!!!!");
else:
    print("Entered number is valid")
finally:
    print("Task completed")


# except errors

try:
    x = int(input("Enter number a:"))
    y = int(input("Enter number b:"))
    z=x/y
    print(z)
except ValueError:
    print("Invalid Number!!!")
except KeyboardInterrupt:
    print("You pass the keyboard interrupt")
except ZeroDivisionError:
    print("Number can't be divided by zero")
finally:
    print("Task Completed")


try:
    x = int(input("Enter number a"))
    y = int(input("Enter number b"))
    z=x/y
    print(z)
except(ValueError,KeyboardInterrupt,ZeroDivisionError):
    print("Invalid input")