#Thuyen Truong
#1780701

class ItemToPurchase:       #create the class
    def __init__(self, item_name="none",item_price= float(0),item_quantity= int(0) ):  #create the attributes
        self.item_name = item_name         #name
        self.item_price = item_price        #price
        self.item_quantity = item_quantity    #quantity
    def print_item_cost(self):            #function to print
        cost = int(self.item_price * self.item_quantity)    #item cost
        price = int(self.item_price)                  #item price
        print(self.item_name, self.item_quantity, "@ $"+str(price), "=", "$"+str(cost))      #print using the correct format

def myinput():                  #function to takes input
    firstinput = ItemToPurchase()         #call the class
    secondinput = ItemToPurchase()

    print("Item 1")                        #first item info(name,price,quanlity)
    print("Enter the item name:")
    firstinput.item_name = input()          
    print("Enter the item price:")
    firstinput.item_price = float(input())
    print("Enter the item quantity:")
    firstinput.item_quantity = int(input())

    print("\nItem 2")                    #second item info (name, price, quanlity,)
    print("Enter the item name:")
    secondinput.item_name = input()
    print("Enter the item price:")
    secondinput.item_price = float(input())
    print("Enter the item quantity:")
    secondinput.item_quantity = int(input())

    print("\nTOTAL COST")                 #print the final output format
    firstinput.print_item_cost()             #print each item using the correct format
    secondinput.print_item_cost()

    cost1 = firstinput.item_quantity * firstinput.item_price         #price for first item
    cost2 = secondinput.item_quantity * secondinput.item_price        #price for second item



    mytotal = int(cost1 + cost2) 
    print("\nTotal:","$"+str(mytotal))      #print the total


if __name__ == '__main__': myinput()