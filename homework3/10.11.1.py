#Thuyen Truong
#1780701

class FoodItem:     #create class Food
    def __init__(self, name="None", fat=0, carbs=0, protein=0):       #set the default atrributes
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        

    def get_calories(self, num_servings):           #formula to calculate the calories
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):                             #format to print the food info
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))

def myinput():
    item1 = FoodItem()          #item one is default iteam (0,0,0)
    item2 = FoodItem()          #item using user inputs

    foodname = input()               #take user inputs
    foodfat = float(input())
    foodcarbs = float(input())
    foodprotein = float(input())
    

    item2.name = foodname              #get value of items using inputs
    item2.fat = foodfat
    item2.carbs = foodcarbs
    item2.protein = foodprotein
    
    num_servings = float(input())          #get the number of servings

    item1.print_info()
    print('Number of calories for', '{:.2f}'.format(num_servings), "serving(s):", '{:.2f}'.format(
                          item1.get_calories(num_servings)))        #print using the appropriate format (with 2 decimals)
    print()
    item2.print_info()
    print('Number of calories for', '{:.2f}'.format(num_servings), "serving(s):", '{:.2f}'.format(
                          item2.get_calories(num_servings)))         #print using the appropriate format (with 2 decimals)

if __name__ == "__main__": myinput()
