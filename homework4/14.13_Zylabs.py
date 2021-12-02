#Thuyen Truong
#1780701


num_calls = 0 #define a global variable

def partition(mynum, i,k):  
    midpoint = i + (k-i) //2        #find the midpoint
    pivot = mynum[midpoint]   #get the pivot from the midpoint
    index = i - 1             #get the left part of the midpoint
    l = i                     #low = i
    h = k                     #high = k
    
    for j in range(l,h):
        if mynum[j] <= pivot:
            index = index + 1
            mynum[index], mynum[j] = mynum[j], mynum[index]
    mynum[index+1], mynum[k] = mynum[k], mynum[index+1]
    return index + 1


def quicksort(mynum, i,k):
    if i < k:
        j = partition(mynum, i,k)

        quicksort(mynum, i,j-1)
        quicksort(mynum, j + 1 , k)
    


if __name__=="__main__":
    mynum = []
    myinput = input()
    while myinput !="-1":           #if the input is less than -1, then append the input into mynum list
        mynum.append(myinput)
        myinput = input()
    
    quicksort(mynum, 0, len(mynum)-1)               #call the quickshot function
    num_calls =  int(2* len(mynum) - 1)            #calculate the number of num calls
    print(num_calls)
    for myinput in mynum:
        print(myinput)



#citation https://learn.zybooks.com/zybook/UHCIS2348Fall2021/chapter/14/section/8
#I use some codes from this lesson for the quicksort algorithm
