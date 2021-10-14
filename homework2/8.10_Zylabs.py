#1780701
#Thuyen Truong



user_input = input() #get user input

no_space = user_input.replace(" ", "") #removing the spaces

reversed_input = no_space[::-1] #reverse the string




if reversed_input == no_space: #compare string to it reverse
    print(user_input, 'is a palindrome') 
else:
    print(user_input, 'is not a palindrome')