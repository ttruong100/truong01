#Thuyen Truong
#1780701


def selection_sort_descend_trace(mylist): #create a function to do selection sort
    for i in range(len(mylist) -1):    #for item in the range of mylist - 1
        largestnum = i                #define the name largestnum and set it equal to i tem
        for j in range(i+1, len(mylist)):  #nested loop for elements in range from i +1 to my range
            if mylist[j] > mylist[largestnum]:  #if element larger than the largest num
                largestnum = j  #set the element as the largest num

        mynum = mylist[i]          #define mynum for items in mylist
        mylist[i] = mylist[largestnum]     #swap items in mylist and largest num
        mylist[largestnum] = mynum
        print(' '.join([str(x) for x in mylist]), end=" ") 
        print() #print the number after the sorting

    return mylist

if __name__=='__main__':
    myinput = input()   #take input from user
    mylist = myinput.split() #split each string into individual element
    mylist = [int(value) for value in mylist] #turn string into integer
    sortedlist = selection_sort_descend_trace(mylist)  #call the selection function
   
#cite https://learn.zybooks.com/zybook/UHCIS2348Fall2021/chapter/14/section/6 for selection sort algorithm