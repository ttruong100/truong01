#Thuyen Truong
#1780701

#get first integer input from user
user_num1 = int(input("Enter integer:\n"))

#print the integer the user entered
print("You entered:" ,user_num1, end='\n')

#square the integer the user entered, multiply itself
userNumSquared = user_num1 * user_num1

#cubed the integer the user entered, multiply itself twice times
userNumCubed = user_num1 *user_num1 * user_num1

#display result of squared and cubed
print(user_num1, "squared is", userNumSquared, end='\n')
print("And", user_num1, "cubed is", userNumCubed, "!!", end='\n')

#get second integer input
user_num2 = int(input("Enter another integer:\n"))

#add first and second int
sumints = user_num1 + user_num2

#multiply first and second int
productints = user_num1 * user_num2

#display sum and product
print(user_num1, "+", user_num2, "is", sumints, end='\n')
print(user_num1, "*", user_num2, "is", productints, end='\n')






