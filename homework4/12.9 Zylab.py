#Thuyen Truong
#1780701




myinput = input()   #take the input from the user


while myinput != '-1':  #if the input is not -1
    try: 
        splitinput = myinput.split()  #get the name using index
        firstinput = splitinput[0]   #position of the name
        secondinput = splitinput[1]   #get the age using index
        print(firstinput, int(secondinput)+1)   #try to print name and age+1
    except:         #if error occurs
        if myinput != int:            #print the one word name, 0 for age
            print(firstinput, 0)      

    myinput = input()   #take next input
     
    
