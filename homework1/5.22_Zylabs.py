# Thuyen Truong
# 1780701


# print a menu of automotive services
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")


# ask the user for two services from the menu

firstservice = input("Select first service:\n")
secondservice = input("Select second service:\n")
print()

# create a dict for services

servmenu = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-':0}




#cost per service
serv1price = servmenu[firstservice]
serv2price = servmenu[secondservice]
totalprice = servmenu[firstservice] + servmenu[secondservice]

#output an invoice for the services selected

if firstservice == "-":
    print("Davy's auto shop invoice")
    print()
    print("Service 1: No service")
    print("Service 2:", secondservice + ",", "${}".format(serv2price))
    print()
    print("Total:", "${}".format(serv2price))

elif secondservice == "-":
    print("Davy's auto shop invoice")
    print()
    print("Service 1:", firstservice + ",", "${}".format(serv1price))
    print("Service 2: No service")
    print()
    print("Total:", "${}".format(serv1price))

else:
    print("Davy's auto shop invoice")
    print()
    print("Service 1:", firstservice + ",", "${}".format(serv1price))
    print("Service 2:", secondservice + ",", "${}".format(serv2price))
    print()
    print("Total:", "${}".format(totalprice))






