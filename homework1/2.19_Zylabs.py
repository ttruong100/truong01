#Thuyen Truong
#1780701

#user input for lemon juice
lemon = float(input("Enter amount of lemon juice (in cups):\n"))
#user input for water
water = float(input("Enter amount of water (in cups):\n"))
#user input for agave nectar
agavenectar = float(input("Enter amount of agave nectar (in cups):\n"))
#user input for servings
servingsnum = float(input("How many servings does this make?\n"))
print(end='\n')
#display ingredients list (userinput) for serving (userinput)
print("Lemonade ingredients - yields", '{:.2f}'.format(servingsnum), "servings",end='\n')
print('{:.2f}'.format(lemon), "cup(s) lemon juice", end='\n')
print('{:.2f}'.format(water), "cup(s) water", end='\n')
print('{:.2f}'.format(agavenectar), "cup(s) agave nectar",end='\n')
print(end='\n')
#ask for user desire
desireserv = float(input("How many servings would you like to make?\n"))
print(end='\n')

#calculate ingredients per serving to desireserv (1 lemon/3serv 16 water/6serv 2.5agavenec/6serv)
callemon = (desireserv * lemon)/ servingsnum
calwater = (desireserv * water)/ servingsnum
calagavenectar = (desireserv * agavenectar)/ servingsnum

#display the result according to desireserv
print("Lemonade ingredients - yields",'{:.2f}'.format(desireserv), "servings",end='\n')
print('{:.2f}'.format(callemon), "cup(s) lemon juice", end='\n')
print('{:.2f}'.format(calwater), "cup(s) water", end='\n')
print('{:.2f}'.format(calagavenectar), "cup(s) agave nectar", end='\n')
print(end='\n')
#convert cups to gallons 16 cups in a gallon
convertlemon = callemon / 16
convertwater = calwater / 16
convertagavenectar = calagavenectar / 16

#display the output in gallon
print("Lemonade ingredients - yields",'{:.2f}'.format(desireserv), "servings",end='\n')
print('{:.2f}'.format(convertlemon), "gallon(s) lemon juice", end='\n')
print('{:.2f}'.format(convertwater), "gallon(s) water", end='\n')
print('{:.2f}'.format(convertagavenectar), "gallon(s) agave nectar", end='\n')





