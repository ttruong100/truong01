# Thuyen Truong
# 1780701

#import math to use the round up function later
import math

# ask for user to input wall height and width
wallheight = int(input("Enter wall height (feet):\n"))
wallwidth = int(input("Enter wall width (feet):\n"))

# calculate wall area
wallarea = wallheight * wallwidth

# display the output area
print("Wall area:", wallarea, "square feet", end='\n')

# calculate paint needed 1gallon/350squarefeet
paintneeded = wallarea / 350

# print paint need result
print("Paint needed:", '{:.2f}'.format(paintneeded), "gallons", end='\n')

# round up the number of gallons needed
print("Cans needed:", math.ceil(paintneeded), "can(s)\n")

#create a dictionary for color:price
dic1= {'red':35,'blue':25,'green':23}

#ask user for desire color
desirecolor = input("Choose a color to paint the wall:\n")

#cal
finalcost = dic1[desirecolor]* math.ceil(paintneeded)

print("Cost of purchasing",desirecolor,"paint:","${}".format(finalcost))

