import pandas
from pandas.io.parsers import read_csv

# This code checks the number of squirrels of different colors and returns the new csv of it.

# opens SquirrelData_2018.csv as data
data = pandas.read_csv("CSV/SquirrelData_2018.csv")

# empty list for types of colors
colors = []

# This adds up new color to above colors[] list
Primary_Fur_Color_List = data['Primary Fur Color'].to_list()

for color in Primary_Fur_Color_List:
    if colors.count(color) == 0:
        colors.append(color) 

# this dict is used to store data of squirrels
squirrel_info = {
    'Fur Color' : [],
    'count'     : []
}

# counts the number of squirrels having color from colors[] list
for color in colors:
    value = squirrel_info['Fur Color'].append(color)
    count = Primary_Fur_Color_List.count(color)
    squirrel_info['count'].append(count)

#saves the data of squirrels as CSV file    
new_data = pandas.DataFrame(squirrel_info)  
print (new_data)
new_data.to_csv('CSV/SqirrelColorData.csv')