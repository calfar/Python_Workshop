# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 09:05:59 2021

@author: Calum
"""

### Day Two ###
## Lists ##
# square brakets denote lists
# lists can have int, float and str data
#arrays require just one type typically
pressure = [0.27, 0.456, 0.033333, 0.7, 1.4]
pressure_second = [0.43, 2, 7, 0.655]
print('pressure:', pressure)

print(len(pressure))

#subsetting a list
pressure[0 : 3] #this prints each value in the list between two points
pressure[0]
pressure[3]

pressure.append(0.54333333) #.append() places an additional value onto the end of a list
print(pressure)
#append is useful for loops
#can also combine two lists
pressure.append(pressure_second) #can refer to another list of values via a variable
print(pressure)
pressure.append([0.6, 0.8, 1.4]) #can be done as a list of values
#prints as a list within a list, not ideal

#to produce a single list
pressure1 = [0.27, 0.456, 0.033333, 0.7, 1.4]
pressure1.extend(pressure_second) #.extend adds to the list, not adding a list within a list
pressure1.extend([0.6, 0.8, 1.4])

#you can also delete from a list, uses statements
del pressure1[0] #this removes the first value from the list
del pressure1[0 : 3] #this removes the values between two points
#useful for a loop if you want to iteratively remove things

empty = [1, "rrrrrr", 1.2345]

pressure1.sort() #.sort() will just order values in ascending order

words = ['alphabet', 'zoo', 'wallaby', 'camera', 'memory']
words.sort() #using .sort() on string will order alphabetically

## For Loops ##

"I like cats"
"I like dogs"
"I like gold fish"
"I like sushi"
#What changes each time? The subjects in this case e.g. cats, dogs, etc
subjects = ['cats', 'dogs', 'gold fish', 'sushi']
#i is just a place holder, don't place #comments within loop, they will print
for i in subjects: 
    print("I really like", i)
#wide space is necessary after first line
for likables in subjects:
    print("I like", likables)
#it will print string before each object in the list
#lists can be places directly after 'in', does not need to be a variable
for number in [2, 3, 4]:
    print("the value is", number)
# you can modify the values in this process
for number in [2, 3, 4]:
    print("the value of the number times 2 is", number*2)
          
    print("something")
#indents after will also be included

primes = [2,3,5]

for p in primes:
    squared = p ** 2
    cubed = p ** 3
    print("original:", p, "squared:", squared, "cubed", cubed)
# this produces new values and prints them alongside a discription of the new values
# new values are assignedt to variables also

print(cubed) #only prints last value from list

sqr = []
for pr in primes:
    squared = pr ** 2
    sqr.append(squared)
    print(sqr)
#above prints each value in the list, if you keep running it though it'll just keep making the list longer
#range() 
for i in range(0, len(primes), 1):
    print("the value of i in this loop is:", primes[i])
#above function prints the value of each value in the primes list
#i referring to the point the loop is at in the list

#in example below, this will print the list textx twice in same list
#changing range() values from (0,1) -> (0,3) makes it print 1 line or three lines respectively
testx = [7,8,9,10]

for x in range(0,3):
    print(testx*2)
    
## if statements ##
# for if you need a function that needs to meet intial conditions before running

mass = 7.02

if mass > 3.0 and mass <= 10.0:
    print(mass, "is large")
elif mass >= 3.0 and mass > 10.0:
    print(mass, "is rediculously large")
else:
    print(mass, "is not large")

# < or > next to = means less than or equal to and greater than or equal to respectively
# and statements set two or more conditions on the following functions
#else is, if the if statement is false, do this
#does not need to be indented below if statement
#elif statement for additional conditions after initial if, that way it's not trying to pass both if statements if it pases the first

#if statements using lists
masses = [2.4, 7.4, 1.1, 52.3]

for i in masses:
    if i > 3.0 and i <= 10.0:
        print(i, "is large")
    elif i >= 3.0 and i > 10.0:
        print(i, "is rediculously large")
    else:
        print(i, "is not large")

#replace the variable with i or whatever is declared as the variable in
# the for '' in masses statement

## or statements
#while 'and' requires both statements are true
# 'or' will proceed if one is false

for i in masses:
    if i > 3.0 or i <=10:
        print(i, "is large")
    elif i > 10.0:
        print(i, 'is rediculously large')
    else:
        print(i, 'is not large')

# the result of this is it prints 'is large' for all values, because one statement is always true

velocity = [53.6, 100.44, 7.2, 10000.5]
# == means this value equals exactly this value, rather than declaring a variable
# or assigning a new value to a value in the list
if masses[1] > 3.0 and masses[2] <=10 or velocity[0] == 54:
    print('all good')

#e.g. velocity[0] = 54 #this would reassign the value of value 0 to 54 in the velocity list

## processing small files
import glob
import pandas as pd
for filename in glob.glob('/Users/Calum/Desktop/python-novice-gapminder-data/data/*.csv'):
    cont = pd.read_csv(filename)
    if len(cont) <50:
        print(filename, len(cont))
# the * in 'data/*.csv) is a wildcard, it will read any csv file
# the if len(cont) <50 means that the only files displayed are the ones with less than 50 rows?

### Creating Functions ###
#def for defining a function
def print_gretting():
    print("Hello World")
print_gretting()    

#Example of setting parameters on printing the date
#doesn't like leading zeroes e.g. 08
def print_date(year, month, day):
    joined = str(year) + '-' + str(month) + '-' + str(day)
    if month == [4, 6, 9, 11] and day > 31:
        print("wrong date input")
    elif month == 2 and day > 28:
        print("wrong date input")
    elif year > 2200 or month > 12 or day > 31:
        print("wrong date input")
    else:
        print(joined)

print_date(2021, 2, 29) 

# averages #
# return is what the function will actually return back to you if conditions are met

def average(values):
    if len(values) == 0:
        print("You must provide some values")
        return None
    return sum(values) / len(values) #this is for the mean

def report(pressure):
    print('pressure is', pressure)
    return(pressure)

print('calling' , report(22.5))

r = report(22.5) #will always auto print from report function
r # running the variable by itself does not run the function, just the value
# function must be defined prior to using it in a script











