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









