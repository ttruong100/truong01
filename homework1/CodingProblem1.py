# Thuyen Truong
# 1780701

#ask user for current date by month, day and year

print("Birthday Calculator")
print("Current Day")
currentmonth = input("Month: ")
currentday = int(input("Day: "))
currentyear = int(input("Year: "))

#ask user for birth date by month day and year
print("Birthday")
birthmonth = input("Month: ")
birthdate = int(input("Day: "))
birthyear = int(input("Year: "))

#calculate birthday by year
cal_birthday = currentyear - birthyear

#user birthday haven't passed yet
not_passed_birthday = cal_birthday - 1

if currentday == birthdate and currentmonth == birthmonth:
    print("You are", cal_birthday, "years old.")
    print("Happy Birthday!")
elif (currentmonth == birthmonth and currentday < birthdate) or (currentmonth < birthmonth) :
    print("You are", not_passed_birthday, "years old.")
else:
    print("You are", cal_birthday, "years old." )
