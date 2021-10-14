#Thuyen Truong
#1780701


from datetime import datetime     #import datetime module

my_input = input()      #user can input file

my_output = open('parsedDates.txt','w')


my_file = open(my_input,'r')    #open input file in read mode

my_months = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
my_days = ('1,','2,','3,','4,','5,','6,','7,','8,''9,','10,' ,'11,', '12,' ,'13,' ,'14,' ,'15,' ,'16,', '17,' ,'18,' ,'19,' ,'20,' ,'21,' ,'22,', '23,', '24,' ,'25,' ,'26,' ,'27,' ,'28,', '29,', '30,','31,')

for line in my_file:
    comma = line.find(",")
    space = line.find(" ")
    
    if comma != -1 and space != -1:  #any line that has the comma and space

                split_the_date = line.split()               #split the date to restrict format
                
                a = split_the_date[0]               #month
                a1 = a.strip()
                
                b = split_the_date[1]               #day
                b2 = b.strip()
                b2_length = len(b)
                
                

                c = split_the_date[2]               #year
                c2 = c.strip()
                c2_length = len(c)
                
                if a in my_months:                  #month must be valid
                    if b2_length <= 3:              #day must be between 1-31
                        if c2_length in range(1,100000):   #year must be between 1-9999

                            new_list = ' '.join([str(elem) for elem in split_the_date]) #dates with the inital correct format list to string
                        
                            correct_list = (new_list +'\n')             #list with new character at the end

                            my_dates_into_datetime = datetime.strptime(correct_list,"%B %d, %Y\n") #convert string into datetime to compare
                

                            current_date = datetime.today()  #gets today's date
                            current_date_to_string = current_date.strftime("%B %d, %Y\n") #format current date into string to corrects the format of current date
                
                            current_date_into_datetime = datetime.strptime(current_date_to_string,"%B %d, %Y\n") #current date back to datetime with the correct format to compare
                
                            if my_dates_into_datetime <= current_date_into_datetime:  #compare the dates, if dates < or = to current date 
                                valid_dates = my_dates_into_datetime                #if true then store into variable

                                final_format = valid_dates.strftime("%#m/%#d/%Y")   #date to string to print out the correct format
                                
                    
                                with open('parsedDates.txt','w'):           #open the paredDates,txt to write output
                                    my_output.write(final_format)              #write the output
                                    my_output.write('\n')               #write the output with newline at the end

                        


my_output.close()
my_file.close()
