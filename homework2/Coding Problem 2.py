#Thuyen Truong
#1780701


from datetime import datetime     #import datetime module

my_input = input()      #user can input file

my_output = open('parsedDates.txt','w')


my_file = open(my_input,'r')    #open input file in read mode

my_months = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}

for line in my_file:
    comma = line.find(",")
    space = line.find(" ")
    
    if comma != -1 and space != -1:  #any line that has the comma and space
        
        for key in my_months: #if it has the months in the dictionary
            if key in line:
                my_dates = line  #dates with the inital correct format
                
                my_dates_into_datetime = datetime.strptime(my_dates, "%B %d, %Y\n") #convert string into datetime to compare
                
                
                #after_convert = my_dates_into_datetime.strftime("%B %d, %Y\n")
                #validate = after_convert.find("%B %d, %Y\n")

                #print(after_convert)
                #print(validate)
                
                

               
                current_date = datetime.today()  #gets today's date
                current_date_to_string = current_date.strftime("%B %d, %Y\n") #format current date into string to corrects the format of current date
                
                current_date_into_datetime = datetime.strptime(current_date_to_string,"%B %d, %Y\n") #current date back to datetime with the correct format to compare
                
                if my_dates_into_datetime <= current_date_into_datetime:  #compare the dates, if dates < or = to current date 
                    valid_dates = my_dates_into_datetime                #if true then store into variable

                    final_format = valid_dates.strftime("%#m/%#d/%Y")   #date to string to print out the correct format
                    print(final_format)
                    
                    with open('parsedDates.txt','w'):           #open the paredDates,txt to write output
                        my_output.write(final_format)              #write the output
                        my_output.write('\n')               #write the output with newline at the end

                


my_output.close()
my_file.close()
