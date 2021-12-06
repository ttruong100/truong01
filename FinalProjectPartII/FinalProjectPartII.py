#Thuyen Truong
#1780701

import csv #enable to read and use csv files
from datetime import datetime
from os import error, remove, terminal_size


first_input = input("Enter Manufacturer List:\n")   #manulist input
second_input = input("Enter Price List:\n")  #pricelist input
third_input = input("Enter Service Dates List:\n") #servicedateslistinput

def manufacturerlist(open_file):
    
    open_file = open(first_input,'r') #open the file in read mode
    my_file = csv.reader(open_file, delimiter=",")  #read the csv file

    my_list = [] #empty list to append later on
    for row in my_file:     #loop to go through each row
        row = [row.strip() for row in row]     #remove trailing if element have trailing
        my_list.append(row)     #append each row into a list making a nested list of all items
        my_sorted_list = (sorted(my_list, key=lambda x:[x[1]] ))  #sorted by inner element [1] - which is the item type by alphabetical order
                                                              #citation https://www.kite.com/python/answers/how-to-sort-a-list-of-lists-by-an-index-of-each-inner-list-in-python
                                                              #use to acces inner element of a list of list 
    return(my_sorted_list)


manulist = manufacturerlist(first_input)  #get the full manufacturerlist


inventory_item_id = {}   #dictionary with item id: if damaged
for i in manulist:
    inventory_item_id[i[0]] = i[3]

item_id = []            #create an item id list to append later 
for i in manulist:
    item_id.append(i[0])

item_name = []        #crrate an item name list
for i in manulist:
    item_name.append(i[1])          

item_name_dict = dict(zip(item_id, item_name))  #create itemid:itemname dictionary



item_type_list = []                  #create type list
for i in manulist:
    item_type_list.append(i[2])

item_type_dict = dict(zip(item_id, item_type_list))   #create itemid:itemtype dictionary




def pricelist(second_input):
    open_file = open(second_input,'r') #open the file in read mode
    my_file = csv.reader(open_file, delimiter=",")  #read the csv file
    price_list = []
    for row in my_file:            
        price_list.append(row)
    return(price_list)

price_list = pricelist(second_input)            #create  price list from data from the pricelist input

item_id = []                                      #create item id list
for i in price_list:
    item_id.append(i[0])                    
item_price = []                                     #create item price list
for i in price_list:    
    item_price.append(i[1])
    

price_dict = {}
price_dict = dict(zip(item_id,item_price))          #create a itemid:itemprice dictionary



def servicedatelist(third_input):
    open_file = open(third_input,'r') #open the file in read mode
    my_file = csv.reader(open_file, delimiter=",")  #read the csv file

    service_date =[]                #create a service date list using data from service date list input

    for row in my_file:
        service_date.append(row)                
    
    
    
    return(service_date)
    

service_dates_with_id = (servicedatelist(third_input))
my_dates = []                                         #create a list with dates from the date
for i in service_dates_with_id: 
    my_dates.append(i[1])
    

my_id = []                                            #create a list of id from the date
for i in service_dates_with_id:
    my_id.append(i[0])

service_dates_dict = dict(zip(my_id, my_dates))     #create a itemid:servicedates dictionary



bigdict= {}                             #create a big dictionary for item id: itemname, type, price, dates, and if damaged
for key in inventory_item_id:           
    if key in item_name_dict:
        if key in item_type_dict:
            if key in price_dict:
                if key in service_dates_dict:
                    bigdict[key] = inventory_item_id[key] , item_name_dict[key] , item_type_dict[key] , price_dict[key] , service_dates_dict[key]

#if common key in all the dictionaries then combine all the dictionaries with the common key #in this case the item id is the common key for all dics

mainlist = list(bigdict.items()) #turn the big dictionary into a list for index access



#fullinventory
fullinventory = []                  #list of full inventory 
for i in mainlist:
    a =  (i[0],i[1][1],i[1][2],i[1][3], i[1][4],i[1][0]) #getting the items using index position
    fullinventory.append(a)

        
#pastservice
pastservicedate = []                      #list of pastservice dates with attributes
current_date = datetime.today()  #todays date
for i in mainlist:
        service_date = (i[1][4])           #access service dates using positions
        service_date = datetime.strptime(service_date,"%m/%d/%Y")     #turn service dates into datetime format to compare
        if service_date < current_date:  #compare if service date is less than todays date
            past_service = (i[0], i[1][1], i[1][2], i[1][3], i[1][4], i[1][0]) #if yes then print the required attribute with the past service date
            pastservicedate.append(past_service)

sortdate = sorted(pastservicedate,  key=lambda x:[x[4]] )  #sort the list so dates will display from oldest to most recent



#damagedinventory 
damagedinventory = []                #list of damaged inventory with attributes
for i in mainlist:
        if 'damaged' in i[1]:                #if the word damaged is found
            damaged_items = (i[0],i[1][1],i[1][2],i[1][3],i[1][4])    #create a list of damaged item with its attributes
            damagedinventory.append(damaged_items)           
sortedprice = sorted(damagedinventory,  key=lambda x:[x[3]] )        #sort the price from most expensive to least expension




##QUERY 

newlist = []            #create a new list thats not past service date and not damaged
for i in fullinventory:                          #go through all the items in the full list
    if i not in pastservicedate:                  #if not in past service date list
        if 'damaged' not in i[5]:                 #if not in damaged list
            filtereditems = i[0],i[1],i[2],i[3]
            newlist.append(filtereditems)           #append to the newlist



userinput = input("Enter the Manufactuer and Item Name:\n")  #get the user input                 

while userinput != "q":                 #looping until user enter q to quit the program

    splitinput = userinput.split()       #split the strings in the input into list of individual string

    combinestuff = item_type_list + item_name               #combine the list of manufacture name and itemtype   
    typeandname = [i.lower() for i in combinestuff]         #lowercase the items in the combined list
    reduce = [i for i in splitinput if i in typeandname]    #check if strings in the list, exclude strings not in the list 
    reduced = " ".join(reduce)                              #turn the reduce list into a string (only item name and type left)

    foundstuff = []                    #list for items that founded in the newlist(inventory)
    def founded():                    #define a function to check if the item is in the newlist
        for stuff in newlist:          #go through all the item in the newlist
            if reduced.lower() == (stuff[1]+" "+stuff[2]).lower():      #if userinput(item name and type) == to  inventory(item name and type)
                a = stuff                 #get the stuff id, manufacturer name, item type, and price
                foundstuff.append(a)                                      #add the founded stuff into the empty list
                return True                                               #return the function as true
    def notfounded():                             #function for stuff that's not founded in the inventory
        for stuff in newlist:
            if reduced.lower() != (stuff[1]+" "+stuff[2]).lower():       #if user input(item name and type) do not exist in the inventory
                return True                                              #return the function as true
                
    similarstuff = []                  #list for similar stuff for suggestion
    def similaritem():                 #create a function
        for stuff in newlist:          #go through the items in the inventory
            if foundstuff[0][2] == stuff[2]:          #if item type from founded stuff equals to item type in the inventory
                if foundstuff[0][0] != stuff[0]:      #if its not the same item from the founded stuff (comparing the item id)
                    similarstuff.append(stuff)               #add the item to the similar stuff
                    return True

    

    if founded():                       #if the item is found
        print("\nYour item is:", ' '.join([i for sub in foundstuff for i in sub]))   #print the item (list comprehension to turn display the items as a string)
        if similaritem():                                                          #if similar item exists
            print("You may also consider:", ' '.join([i for sub in similarstuff for i in sub]),"\n")   #print the simlar item as a single string

    elif notfounded():          #if item does not exist
        print("No such item in inventory")  #print no item exist

        

        
        

                
        
    userinput = input("Enter the Manufactuer and Item Name or q to quit:\n")         #ask the user for the input to go through the query again
if userinput == "q":                                                                #if user type q then quit the query
        quit()


#citation
# https://stackoverflow.com/questions/27722041/how-to-convert-a-list-of-tuples-into-a-single-string - use to convert list of tuples to string for display
