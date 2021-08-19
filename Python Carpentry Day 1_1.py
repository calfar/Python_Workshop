# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
################# hashes for comments, python does not recognise anything after a hash
# f9 to run line
a = 2 + 2

b = 2 + 4 #this is a integer variable

c = 'this is a senctence' #this is a string

d = [2 + 50, 3 - 1, 4 - 0, 'ipsum'] #this is a list

name = 'Calum'

campus = "Gold Coast"

sentence = 'My name is ' + name + " and I'm at the " + campus + ' campus.'

multi = a * c

len(c) #this calculates the lenght of a string
length = len(c)

begin = c[0:-1] #this extracts part of a string relating to character lenght

x = 1 + 1 #this is a comment

minutes_here = 10
import math #import 'libraryname' imports a library
#print(math.pi) #'libraryname' '.' then 'variable

#help(math) #provides help from library

#int = whole number e.g. 2001
#float = decimal e.g. 2.2 or 2.0
#string (str) = characters
# identify the type by using #type(variable_name)
#int and float can be added, subtracted etc.
z = 2.1

first = 1
second = 5 * first
first = 2 #demonstrating the importance of declaring variables in order
#print("first is", first, "and second is", second)

#print("5 //3:", 5//3) = 1
#print("5 / 3:", 5 / 3) = 1.6666666666667
#print("5 % 3", 5 % 3) = 2

#print(int("3.4")) #does not work

#print(int(float(3.4))) #does work

#str -> float -> int
#print(int(float('3.4'))) = 3 # that's because float -> rounds to nearest whole

### Functions ###
# () round brackets is a function
# [] square brackets are ???

#result = print("Example")
#print("result of print is ", result)
# this results in None type

#print(max(1,2,3)) Max = maximum
#order is critical

#output = 'function name'(input)
# different fucntions expect different inputs
#print(round(3.712)) = 4 round can take two pieces of inpu
#print(round(3.712, 2)) = 3.71 two representing the number of decimal places

#help(function) provides info
#functions can be type specific e.g.
my_string = "Hello World!"
#print(len(my_string))
#print(my_string.swapcase())
#print(my_string.__len__()) #pushes the variable "my_string" into the function len()

### ERRORS ###
#syntax errors will point out where a mark is missing or there is a repeat or invalid use
## EOF = end of function
## EOL = end of line
## parsing = while reading line or function
#Indentation Error e.g. additional spaces at the start of a line
#Name Error = variable non-defined

#radiance = 1.0
#radiance = max(2.1, 2.0 + min(radiance, 1.1 * radiance - 0.5))
#radiance = 2.6

### Python Documentation ###
# contains all functions, types, etc.

### Libraries ###
#library installs
#import 'libraryname'
#import math
#provides no input/feedback
#call info from library
#print(math.pi) libraryname.reference
#print("cos(pi) is", math.cos(math.pi))
#call help(math)

#if not wanting to call math all the time
#import math as 'something' gives it a nickname
#e.g. 'import math as m'
#then can use m.pi or m.cos(m.pi)

#angle = math.degrees(math.pi/2)
#print(angle)

#when you don't want to import the entire library
#from math import pi, cos
#this brings those variables from the library into the script as a variable
#means you don't have to call the library
#from math import * means import everything, considered poor practice
#this is because the library may have functions that are the same as other libraries or variables you've already created.

### Data Frames and Reading Tabular Data ###
## Spatial or Visual data
#tables of colour values or height values, etc.
#can use a variety of types
# df[0,1] searches df (dataframe name) and location in the data frame [0,0,0]

#reading data in
#use csv. files over xl files
#import pandas as pd
data = pd.read_csv('C:/Users/Calum/Desktop/python-novice-gapminder-data/data/gapminder_gdp_oceania.csv')
#ensure to use foward slashes in this case, add file type (csv) to end of file name
print(data)

#to print specific things add "index_col='country') for country column, make sure to extend bracket to after both file location and index.
data = pd.read_csv('C:/Users/Calum/Desktop/python-novice-gapminder-data/data/gapminder_gdp_oceania.csv', index_col="country")
# now when using print(data) it removes the no. ID column or starts at country?
print(data)

data.info()
#below provides all the column names
print(data.columns)
#transposing data, switches rows and columns
print(data.T)
#summary statistics, provides some basic statistical information e.g. max min, percentages.
print(data.describe()) #only useful for numerical data

data_Americas = pd.read_csv('C:/Users/Calum/Desktop/python-novice-gapminder-data/data/gapminder_gdp_americas.csv')
data_Americas = pd.read_csv('C:/Users/Calum/Desktop/python-novice-gapminder-data/data/gapminder_gdp_americas.csv', index_col="country")

print(data_Americas.describe())
data_Americas.info()
data_Americas

#inspecting the data
data_Americas.tail(5) #shows last x amount of rows
data_Americas.head(5)

#Exporting the data putting in file location and new name at end + file type.
data_Americas.to_csv('C:/Users/Calum/Desktop/python-novice-gapminder-data/data/write.csv') #in brackets place a location directory

data_Europe = pd.read_csv('C:/Users/Calum/Desktop/python-novice-gapminder-data/data/gapminder_gdp_europe.csv', index_col="country")

#sub-setting dataframe and locating data
data_Europe.iloc[0,0] #pulls cell value
print(data_Europe)

data_Europe.loc['Austria', 'gdpPercap_1952'] #pulls column and row data using names as strings

print(data_Europe.loc['Austria',:]) #the colon after 'Austria', will produce all cells relating to Austria
austria_GDP = data_Europe.loc['Austria',:] #This sets this column/row as it's own variable/set
print(austria_GDP) #can now be manipulated independently

print(austria_GDP.loc["gdpPercap_1952" : "gdpPercap_1987"]) #this will print that range

print(data_Europe.loc["Austria" : "Hungary"].max()) #provides max value from each row, but doesn't tell you which one it comes from.

GDPmax = data_Europe.loc["Austria" : "Hungary"].max() #setting and printing this category as a variable
print(GDPmax)

#creating a mask
data_Europe > 10000 #produces a true or false table for greater than this value
#This is a masking layer
mask10000 = data_Europe > 10000
print(mask10000)
data_Europe [mask10000] #this shows the values which are greater than 10000, hiding others under NaN
GDP10000 = data_Europe[mask10000]
print(GDP10000) #this process maintains table integreting, just replaces values

print(data_Europe[mask10000].describe()) #describes only the values which meet the mask requirments

#The mask is just a way of filtering out certain values
print("this is the data summary for values greater than 10,000" + str(data_Europe[mask10000].describe())) #bad way of adding info

###Group By: split-apply-combine
# Pandas has methods for data analysis
mask_higher = data_Europe > data_Europe.mean() #this mask gives a ture or false for values around the European mean
print(mask_higher)
#Below, this gives a score to each country, each year gets a score of 1 or 0 depending on if it was above or below the average respectively.
#This is then divided by the number of columns "len*data_Europe.columns"
wealth_score = mask_higher.aggregate("sum", axis = 1) / len(data_Europe.columns)
print(wealth_score)
data_Europe.groupby(wealth_score).sum() #this sums the GDP of countries of each score of the period for each period, not particularly useful
#above is reliant of having the country name index and doing the index_col="country"

print(data_Europe.loc["Serbia", "gdpPercap_2007"])
#above is solution to problem "write expression to find the per capita gdp of Servia in 2007

print(data_Europe.idxmin()) #produces name of country which has the minimum value in each year
print(data_Europe.idxmax()) #produces name of country which has the maximum value in each year

#### Plotting ####
import matplotlib.pyplot as plt

#Test Plot
time = [0, 1, 2, 3, 4]
position = [0, 100, 200, 300, 400]
plt.plot(time, position) #plots two lists against eachother (x,y)
plt.xlabel("time (hr)") #captions the x-axis
plt.ylabel("position (km)") #captions the y-axis
#make sure to untick mute inline plotting so that it shows in console

plt.plot(data_Europe) #creates a very busy plot
years = data_Europe.columns.str.strip('gdpPercap_') #removes gdppercap from year title and makes them strings
print(years)
data_Europe.columns=years.astype(int) #replaces the column headings with the years and as integers
data_Europe.describe()
data_Europe.loc['Austria'].plot() #plots Austrian data over each yeardata_Europe.loc['Albania' : "Croatia"].plot()
#below is new plot, of all countries
plt.style.use("ggplot") #adds a style ggplot adds lines on background
data_Europe.T.plot(kind= 'bar') #kind= '' changes what kind of graph it is
plt.ylabel("GDP per Capita")
plt.xlabel("year")
#two countries test
plt.style.use("ggplot")
data_Europe.loc["Albania" : "Austria"].T.plot(kind= 'bar')
plt.ylabel("GDP per Capita")
plt.xlabel("year")
plt.legend(loc="upper left")

#another test
plt.style.use("ggplot")
data_Europe.loc["Albania", "Austria"].T.plot(kind= 'bar')
plt.ylabel("GDP per Capita")
plt.xlabel("year")

#g-- g = green -- is the line type
plt.plot(time, position, "g--")
#data-to-vis.com/graph for more styles and graphs
#legend location
plt.legend(loc="upper left")

#if you want to save a graph
plt.savefig("my_graph.png", dpi = 1000, ) #help(plt.savefig) for more information



