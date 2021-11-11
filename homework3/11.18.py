#Thuyen Truong
#1780701

myinput = input()    #take user input

myinput = myinput.split()  #split each element into individual str


myinput = [int(i) for i in myinput] #convert each string in the list into int

nonnegative = []         #empty list
for i in myinput:        #for item in list of string
    if i >= 0:            #for item >= 0
        nonnegative.append(i)  #append to the empty list



sortedlist = sorted(nonnegative)           #sort the list
print(*sortedlist, end=" ")     #print the sorted list, * to unpack each element 


