#Write a program to display the current dat and time

import datetime
current_dt=datetime.datetime.now()
print('Current Date and Time : ',current_dt)

#Return the year ,date,month
print(current_dt.year)
print(current_dt.day)
print(current_dt.month)

# The strftme() method
# This method is for formatting data objects into readable strings

# Program to print day from the given date
print("day: ",current_dt.strftime("%a"))
print('Day:',current_dt.strftime("%A"))

#Program to print number of weekday 0-6,0 is Sunday
print('week_day_num :',current_dt.strftime("%w"))  

#Program to print day of month 0-31
print('month_day:',current_dt.strftime("%d"))

# Program to find day number of Year
print('No. of day in Year:',current_dt.strftime("%j")) 

#program to find number of week in a year
print('No. of week in year:',current_dt.strftime("%U"))  # sunday as first day of week
print('No. of week in year:',current_dt.strftime("%W"))  #Monday as first day of week


#Program to print month name for a given date
print('month:',current_dt.strftime("%b"))
print('Month:',current_dt.strftime("%B"))

#program to print number of month 0-12
print('month_number:',current_dt.strftime("%m"))


#Program to print year 
print('year:',current_dt.strftime("%y"))
print('Year:',current_dt.strftime("%Y"))

#Program to print hour for given time
print('24_hours:',current_dt.strftime("%H"),current_dt.strftime("%p"))
print('12-hours:',current_dt.strftime("%I"),current_dt.strftime("%p"))

#program to print am/pm 
print('time:',current_dt.strftime("%X"),current_dt.strftime("%p"))

#Program to print minute from a given time
print('Minute:',current_dt.strftime("%M"))

#Program to print seconds from a given time
print('Seconds:',current_dt.strftime("%S"))

# Program to print UTC offset and time zone
print('Utc_offset:',current_dt.strftime("%Z"))

# Program to print local version of date and time
print('Local version of D&T:',current_dt.strftime("%c"))  

# Program to print local version of date & local version of week
print('Local version of Date:',current_dt.strftime("%x")) 
print('Local version of Time:',current_dt.strftime("%X"))   


# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)

from datetime import date
f_date = date(2020,12,21)
t_date = date(2021,5,6)
number_days=t_date-f_date
print(number_days)

