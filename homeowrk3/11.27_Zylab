#Thuyen Truong
#1780701

jersey = []   #empty list to store user input for jersey number
rating = []   #empty to store user input for rating

for i in range(0,5): #0-5 because output number starts at i+1's , in range of 5 inputs pair
    jerseynum = int(input("Enter player " + str(i+1) + "'s jersey number:\n")) 
    jersey.append(jerseynum)   #append to empty list
    playerrating = int(input("Enter player " + str(i+1) + "'s rating:"))
    rating.append(playerrating) #append to empty list
    print("\n")
mydict = dict(zip(jersey, rating))          #create a dictonary by combining the two list as key:value pair

print("ROSTER")                             #print the roster
for key,value in sorted(mydict.items()):
    print("Jersey number:", str(key)+",","Rating:", value)      #print for every key:value pair in the dictionary with sorted keys
 
def usermenu():                                  #create a menu for user to choose
    print('\nMENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit') 
    
usermenu()                                              #call the menu
useroption = input('\nChoose an option:\n')             #choose option from the menu
while useroption != 0:
    if useroption == 'q':                     #if choose q, quit the program
        quit()
    elif useroption =='a':                  #if choose a, add new key:value pair
        
        addjersey = int(input('''Enter a new player's jersey number:\n'''))     
        addrating = int(input('''Enter a new player's rating:\n'''))
        mydict[addjersey] = addrating
    
    elif useroption =='d':                     #if choose d, delete a player
        deletejersey = int(input('''Enter a jersey number:\n''')) 
        del mydict[deletejersey]             #delete player using key

    elif useroption =='u':
        keytoupdate = int(input('''Enter a jersey number:\n'''))             #if choose u, update rating
        newrating = int(input('''Enter a new rating for player:\n'''))
        update = {keytoupdate:newrating}                             #update value for the selected key
        mydict.update(update)

    elif useroption =='r':
        filterrating = int(input('''Enter a rating:\n'''))                #if choose r, display rating above a certain rating
        print('ABOVE',filterrating)
        for key,value in sorted(mydict.items()):                             
            if value > filterrating:                      #if value larger than entered rating, display the output
                print("Jersey number:", str(key)+",","Rating:", value )


    elif useroption =='o':                          #if choose o, display the roster
        print("ROSTER")
        for key,value in sorted(mydict.items()):
            print("Jersey number:", str(key)+",","Rating:", value )
    usermenu()                   
    useroption = input('\nChoose an option:\n')                 #repeat the menu until q (quit the program)
    
