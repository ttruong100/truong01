#Thuyen Truong
#1780701




#write a function to raise error when the input age is not in the inclusive range
def get_age():
    inputage = int(input())
    if inputage >= 18 and inputage <=75:
        return inputage
    else:
        raise ValueError('Invalid age.')

#write a function to calculate the burning heart rate
def fat_burning_heart_rate(inputage):
    rate = .70 * (220 - inputage)
    return rate

#write the exception handling
if __name__=="__main__":
    try:
        validage = get_age()       
        rate = fat_burning_heart_rate(validage)
        print('Fat burning heart rate for a', validage, "year-old:", rate, "bpm")  #try if the age is vaid and does not raise any error
    except ValueError as invalidrate:  #if the age error occur then print the followings
        print(invalidrate)
        print('Could not calculate heart rate info.\n')  
