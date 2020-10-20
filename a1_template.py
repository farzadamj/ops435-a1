#!/usr/bin/env python3


#OPS435 Assignment 1 - Fall 2020
#Author: "farzad amjadi kolour"
#Author ID: famjadi-kolour



import os
import sys



def leap_year(obj):
	
	if (year % 4 == 0 and year % 100 != 0) or (year% 400 == 0):
        	return True
	else:
        	return False
#if the year is leap year, the output of this function would be True, and otherwise, the output would be False.








def sanitize(obj1,obj2):
	obj3=''
	for i in range(len(obj1)):
		if obj1[i] in obj2:
			obj3=obj3 + obj1[i]
	return obj3





def size_check(obj, intobj):
        if len(obj)== intobj:
                return True
        else:
                return False







def range_check(x, y):
	if y == (1900,9999):
		if x in range (1900, 9999):
			return True
		else:
			return False
       
	elif y == (1,12):
		if x in range (1, 13):
			return True
		else:
			return False
	elif month == 1 :
		if y == (1,31):

			if x in range (1, 32):
				return True
			else:
				return False
	elif month == 2:
		if leap_year(year):
			if x in range (1, 30):
				return True
			else:
				return False	
		else:
			if x in range (1, 29):
				return True
			else:
				return False
	elif month == 3:
		if y == (1,31):
			if x in range (1, 32):
				return True
			else:
				return False
	elif month == 4:
		if y == (1,30):
			if x in range (1, 31):
				return True
			else:
				return False
	elif month == 5:
		if y == (1,31):
			if x in range (1, 32):
				return True
			else:
				return False
	elif month == 6:
		if y == (1,30):
			if x in range (1, 31):
				return True
			else:
				return False
	elif month == 7:
		if y == (1,31):
			if x in range (1, 32):
				return True
			else:
				return False
	elif month == 8:
		if y == (1,31):
			if x in range (1, 32):
				return True
			else:
				return False
	elif month == 9:
		if y == (1,30):
			if x in range (1, 31):
				return True
			else:
				return False
	elif month == 10:
		if y == (1,31):
			if x in range (1, 32):
				return True
			else:
				return False
	elif month ==11:
		if y == (1,30):
			if x in range (1, 32):
				return True
			else:
				return False
	elif month == 12:
		if y == (1,31):
			if x in range (1, 32):
				return True
			else:
				return False


def usage(): 
	x= "Usage: a1_famjadi-kolour.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD"  
	return x





if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   
   # setp 4
   result = size_check(dob,8)
   if result == False:
       print('Error 09: wrong date entered')
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   print(new_dob)  

