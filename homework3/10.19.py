#Thuyen Truong
#1780701

class ItemToPurchase:       #create the class
    def __init__(self, item_name="none",item_price= float(0),item_quantity= int(0), item_description = "none"):  #create the attributes
        self.item_name = item_name         #name
        self.item_price = item_price        #price
        self.item_quantity = item_quantity    #quantity
        self.item_description = item_description #description

    def print_item_cost(self):            #function to print
        cost = int(self.item_price * self.item_quantity)    #item cost
        price = int(self.item_price)                  #item price
        print(self.item_name, self.item_quantity, "@ $"+str(price), "=", "$"+str(cost))      #print using the correct format
    
    def print_item_description(self):             #item description like the format
        print(self.item_name+":", self.item_description)

    def calculate_cost(self):
        return (self.item_price * self.item_quantity)             #calculate the cost of individual item

class ShoppingCart:
    
    def __init__(self, customer_name="none", current_date="January 1,2016"):              #set the default values for these attributes 
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []           #cart_items is a list
       
        
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)        #append item to cart items

    def remove_item(self, item_name):                #remove the desired name if in the cart
        myitem = 0
        for i in self.cart_items:
            if i.item_name == item_name:
                self.cart_items.remove(i)          
                myitem != 0 

        if myitem:
            print('Item not found in the cart. Nothing removed')        #remove nothing if the item is not in the cart

    def modify_item(self, ItemToPurchase):                 #change the item value
        moditem = 0
        for i in self.cart_items:
            if i.item_name == ItemToPurchase.item_name:               #if item found in cart
                moditem = i                            #change the item to the desired value
            if moditem:
                print("Item is not found in cart. Nothing modified")       #if item not found in cart then print nothing modified
    def get_num_items_in_cart(self):            #get current items in the cart
        itemscount = 0

        for i in self.cart_items:
            itemscount += i.item_quantity                    #count the item in the cart

        return itemscount        #return the value

    def get_cost_of_cart(self):          #def to get the cost for each item
        itemscost = 0                    
 
        for i in self.cart_items: 
            itemscost += i.calculate_cost() 
        return itemscost       #return the value for the cost
        
    def print_total(self):                                   #print the total cost of the items
        total_cost = self.get_cost_of_cart()
        if total_cost > 0:
            print(self.customer_name+"'s", "Shopping Cart -", self.current_date)
            print("Number of Items:", self.cart_items)
            for i in self.cart_items:
                i.print_item_cost()
            print("\nTotal:", "$"+str(total_cost))
        else:
            print("SHOPPING CART IS EMPTY")                   #if cost is < 0 then the shop is empty

    def print_descriptions(self):                         #print description of the items
        print(self.customer_name+"'s", "Shopping Cart -", self.current_date)
        print("\nItem Descriptions")
        for i in self.cart_items:
            i.print_item_description()

  
def print_menu(shopcart):      #create a menu for the user to select
    mycart = shopcart     
    print('\nMENU')
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - Change item quantity')
    print('''i - Output items' descriptions''')
    print('o - Output shopping cart')
    print('q - Quit') 

                                                                    
    useroption = input('\nChoose an option:\n')     #call the menu

    while useroption != 0:
        
        if useroption == 'q':                     #if choose q, quit the program
                quit()
        elif useroption =='a':   
            additem = print("ADD ITEM TO CART")              #if choose a, add item to the list
            entername = input('Enter the item name:\n')   
            enterdescription = input('Enter the item description:\n')
            enterprice = int(input('Enter the item price:\n'))
            enterquantity = int(input("Enter the item quantity:\n"))
            ShoppingCart.add_item(ItemToPurchase)

        elif useroption =='r':                     #if choose r remove the selected item
            removeitem = print("REMOVE ITEM FROM CART")
            enteritem = input('''Enter name of item to remove:\n''')
            ShoppingCart.remove_item(item_name)          

        elif useroption =='c':
            modifyitem = print("CHANGE ITEM QUANTITY")
            enteritemname = input('Enter the item name:\n')            #if choose c, change the item quantity 
            enternewquantity = int(input('''Enter the new quantity:\n'''))
            ShoppingCart.modify_item(ItemToPurchase)

        elif useroption =='i':
            ShoppingCart.print_descriptions()


        elif useroption =='o':                          #if choose o, display the cart
            ShoppingCart.print_total()
                    
        useroption = input('Choose an option:\n')   

def myinput():      #def to get input from user
    shopcart = ShoppingCart()             #call the class
    print("Enter customer's name:")
    shopcart.customer_name = input()         #get the input of customer's name
    print("Enter today's date:")
    shopcart.current_date = input()       #get the input of current date

    print("\nCustomer name:",shopcart.customer_name)       #print the input customer name
    print("Today's date:", shopcart.current_date)            #print the input current date

    print_menu(shopcart)
if __name__ == '__main__': myinput()
