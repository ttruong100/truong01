#Thuyen Truong
#1780701


import csv  #to able to interpret csv file


my_file = input()  #input for user to input their desired file

with open(my_file, 'r') as f:       #open the file in read mode
    reader = csv.reader(f, delimiter=',') #read the csv file, seperate without the comma
    for rows in reader:             
        my_items = rows         #create list from the csv file
        
no_duplciates = []                  #remove duplicates items
for i in my_items:
    if i not in no_duplciates:
        no_duplciates.append(i)

[print(item, my_items.count(item)) for item in no_duplciates] #print the result
    #item is the item name, my.items() to count the item in the no_duplicates list

#Citation
#I've followed this method of list comprehension from this Youtube video while writing my code
#https://www.youtube.com/watch?v=yeRnHfFXYDg

