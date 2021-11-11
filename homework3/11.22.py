#Thuyen Truong
#1780701

mylist = input()   #take input from user

mylist = mylist.split()    #split each element into individual string
for i in mylist:   #each item in the list
    count = mylist.count(i)  #count all the individual string
    print(i,count)         #print item, its frequency