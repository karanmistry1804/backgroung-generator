# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

day=int(input('Enter date:'))
month=int(input('Enter month:'))
year=int(input('Enter year:'))

print('class date {0}/{1}/{2}'.format(day,month,year))