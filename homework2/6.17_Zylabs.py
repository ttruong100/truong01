#Thuyen Truong
#1780701 


user_input = input()  #ask for user input


password = user_input.replace("i","!").replace("a","@").replace("m","M").replace("B","8").replace("o",".") #replace the characters accordingly 
password = password + "q*s"  #add q*s at the end
    
print(password) #print the stronger password

       
