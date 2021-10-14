#1780701
#Thuyen Truong

a1 = int(input()) #these are user inputs
b1 = int(input())
c1 = int(input())

a2 = int(input())
b2 = int(input())
c2 = int(input())

solution_check = False #create boolean to check
for x in range (-10, 11):
    for y in range (-10, 11):
        
        if c1 == a1*x + b1*y and c2 == a2*x + b2*y: #if x and y statisfy both equations
            solution_check = True  #then solution found
            print(x,y)                #print
        
    if solution_check:  #if solution not found
        break           
        
else:   #if no solution found
    print('No solution')
        
            
            
       
    
            

   
            
            

    
