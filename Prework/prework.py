# Question 1 Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
# def hello_name(user_name):

user_name = "hello_USERNAME!"
print (user_name)

USERNAME = "hello_Safiya!"
print (USERNAME)

USERNAME = "hello_Safiya!"
print (USERNAME.upper())

# Break
print("")

# Question 2 Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
# def first_odds():

first_odds = list(range(1,100,2))
print(first_odds)

# Break
print("")

# Question 3 Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
#def max_num_in_list(a_list):

a_list = [2,3,4,5,6,1]
print(max(a_list))  

# Break
print("")

# Question 4 Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

given_year = 2023
divisible_by_4 = given_year % 4
divisible_by_400 = given_year % 400
divisible_by_100 = given_year % 100

if (divisible_by_4 == 0) and (divisible_by_400 == 0) and (divisible_by_100 == 0):
#Is a leap year
    print(True) 
if (divisible_by_4 > 0) and (divisible_by_400 > 0) and (divisible_by_100 > 0):
#Not a leap year
    print(False) 

given_year2 = 2000
divisible_by_4 = given_year2 % 4
divisible_by_400 = given_year2 % 400
divisible_by_100 = given_year2 % 100

if (divisible_by_4 == 0) and (divisible_by_400 == 0) and (divisible_by_100 == 0):
#Is a leap year
    print(True) 
if (divisible_by_4 > 0) and (divisible_by_400 > 0) and (divisible_by_100 > 0):
#Not a leap year
    print(False)

# Break
print("")
#Question 5 Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

# def is_consecutive(the_list):

#Consecutive
the_list = [1,3,2,4,6,5,7,8]
sorted_list = sorted(the_list)
range_list = list(range(min(the_list), max(the_list)+1))
if sorted_list == range_list:
   print(True)
else:
   print(False) 

#Not consecutive
the_list = [1,2,4,5]
range_list=list(range(min(the_list), max(the_list)+1))
if the_list == range_list:
   print(True)
else:
   print(False)   