import json # it is used to change string into Python Dictionaries
import os # this is file opraction


def add_iteam_f():
    iteam_name = input("Enter the name of the iteam.")
    
            
    if iteam_name in inventory: # this is to check it itam alreay exists.
        print("Iteam already exists.")
    else:
        iteam_price = input("Enter the price of the iteam.")
        iteam_quanity = input("Enter the amount quanity that are availabel.")
                
        inventory[iteam_name]={
            "price":iteam_price,
            "quanity":iteam_quanity
            }
                
        with open (filename,"w") as file:
            json.dump(inventory, file, indent=4)


def restock():
    iteam_name = input("Enter the name of the iteam.")
            
    if iteam_name in inventory: # this is to check it itam alreay exists.
        iteam_quanity =int(input("Enter the amont to restock."))
        
        inventory[iteam_name]["quanity"] += iteam_quanity
        
        with open (filename,"w") as file:
            json.dump(inventory, file, indent=4)
        
    else:
        print("iteam doesn't exists.")
        

def sell_iteam():
    iteam_name = input("Enter the name of the iteam.")
            
    if iteam_name in inventory: # this is to check it itam alreay exists.
        iteam_quanity_sell =int(input("Enter the amont to sell."))
        
        inventory[iteam_name]["quanity"] -= iteam_quanity_sell
        
        with open (filename,"w") as file:
            json.dump(inventory, file, indent=4)
        
    else:
        print("iteam doesn't exists.")


def view_iteam():
    
    
    for iteam in inventory:
        
        print(iteam)
        



filename = "inventory.json"
inventory = {}

if not os.path.exists(filename):  # checks if file exists or not
    print("no file was fond. Creating a new file.") 
    with open (filename, "w") as file: # if file is not found it will create a new file inventory.json
        try:
            inventory = json.load(file)
        except json.JSONDecodeError:
            # Handle case where file exists but is empty or corrupted JSON
            print("Warning: inventory.json is empty or corrupted. Starting with an empty inventory.")
            inventory = {}


    while True:
        print("1.Add iteam\n 2.Sell iteam\n 3.Restock\n 4.View all iteam\n 5.Exit")
        menu_s = input()
        
        if menu_s ==1:
            add_iteam_f()
            
        elif menu_s ==2:
            restock()
                
        elif menu_s ==3:
            sell_iteam()
                
        elif menu_s ==4:
            view_iteam()
            
        elif menu_s ==5:
            print("Saving inventory and exiting...")
            with open(filename, "w") as file:
                json.dump(inventory, file, indent=4)
            break 
            
        