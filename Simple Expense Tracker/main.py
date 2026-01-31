import os # this is to check if file is present with in the scope of the program

# this program take iteam name and price and add it ti file "expanses.txt" in "iteam_name,iteam_price" format
def add_expanse ():
    expanse_name = input("Enter the Describe of Expanse\n")
    expanse_price = input("Enter the amount for your expanse\n ")
    with open("expanses.txt","a") as expanse_file:
        expanse_file.write(f"{expanse_name},{expanse_price}\n")
    print("Saved!")

def view_total():
    total=0
    with open("expanses.txt","r") as expanse_file:
         for line in expanse_file:
             
             clean_line = line.strip() # this clean the strint of any space 
             expanse_D_and_P = clean_line.split(",") # .split is used to with "," when function find "," it split the variable.
             
             name = expanse_D_and_P[0] # the first part is name 
             price = int(expanse_D_and_P[1]) # sceond part is price 
             
             print("Iteam: ",name,"  ","Price: ",price)
             total += price # total = toal+price
             
    print("--------------------")
    print("GRAND TOTAL: ",total)
    print("--------------------")

def remove_expanse():
    expanse_name = input("Enter the name of the expanse to remove: \n")
    
    # Read all expenses
    expenses = []
    with open("expanses.txt","r") as expanse_file:
        expenses = expanse_file.readlines()
    
    # Filter out the expense to remove
    found = False
    with open("expanses.txt","w") as expanse_file:
        for line in expenses:
            clean_line = line.strip()
            if clean_line:  # ignore empty lines
                name = clean_line.split(",")[0]
                if name.lower() != expanse_name.lower():  # keep all except the one to remove
                    expanse_file.write(line)
                else:
                    found = True
    
    if found:
        print("Expanse removed!")
    else:
        print("Expanse not found!")

def update_expanse_name():
    target_name = input("Enter the name of the expanse to update the NAME for: \n")

    with open("expanses.txt", "r") as expanse_file:
        expenses = expanse_file.readlines()

    found = False
    with open("expanses.txt", "w") as expanse_file:
        for line in expenses:
            clean_line = line.strip()
            if not clean_line:
                continue
            parts = clean_line.split(",", 1)
            name = parts[0]
            price = parts[1] if len(parts) > 1 else ""

            if name.lower() == target_name.lower():
                found = True
                new_name = input(f"Enter new name (leave blank to keep '{name}'): \n")
                if not new_name:
                    new_name = name
                expanse_file.write(f"{new_name},{price}\n")
            else:
                expanse_file.write(line)

    if found:
        print("Name updated!")
    else:
        print("Expanse not found!")

def update_expanse_price():
    target_name = input("Enter the name of the expanse to update the PRICE for: \n")

    with open("expanses.txt", "r") as expanse_file:
        expenses = expanse_file.readlines()

    found = False
    with open("expanses.txt", "w") as expanse_file:
        for line in expenses:
            clean_line = line.strip()
            if not clean_line:
                continue
            parts = clean_line.split(",", 1)
            name = parts[0]
            price = parts[1] if len(parts) > 1 else ""

            if name.lower() == target_name.lower():
                found = True
                new_price = input(f"Enter new price (leave blank to keep '{price}'): \n")
                if not new_price:
                    new_price = price
                expanse_file.write(f"{name},{new_price}\n")
            else:
                expanse_file.write(line)

    if found:
        print("Price updated!")
    else:
        print("Expanse not found!")

filename = "expanses.txt"

if not os.path.exists(filename):  # checks if file exists or not
    print("no file was fond. Creating a new file ") 
    with open (filename, "w") as expanse_file: # if file is not found it will create a new file expanses.txt
        pass # this done because i use with to open a file and there must be a code when using with
    
while True: # loop only start with true ie. 1, 2, 3 are true and other are false

    print("\n1. Add expanse")
    print("\n2. View expanse")
    print("\n3. Update expanse NAME")
    print("\n4. Update expanse PRICE")
    print("\n5. Remove expanse")
    print("\n6. Exit")
        
    choioce = input("Choose: ")
        
        
    if choioce == "1" :
        add_expanse()
        
    elif choioce == "2" :
        view_total()
    
    elif choioce == "3" :
        update_expanse_name()
    
    elif choioce == "4" :
        update_expanse_price()
    
    elif choioce == "5" :
        remove_expanse()
            
    elif choioce == "6" :
        break
        