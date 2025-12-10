
contacts = {}

user_input = ""

while user_input == "exit":
    user_input = input("Enter command (1.Add contact, 2.search, 3.Delete, 4.List all, 5.exit): ")
    
    if user_input == "1" or "Add contact":
        name = input("Enter contact name :")
        phone_number = input ("Enter phone number :")
        contacts[name]= phone_number
        print(name,"has been added to contacts.")
        
    elif user_input == "2" or "search":
        name = input("Enter contact name to search :")
        if name in contacts:
            print(name, " :", contacts[name])
        else:
            print(name, "not found in contacts.")
    
    elif user_input == "3" or "Delete":
        name = input("enter the contact name to delete :")
        if name in contacts:
            del contacts[name]
            print(name, "has been deleted form the contacts.")
        else:
            print(name, "not found in contacts.")
            
    elif user_input == "4" or "List all":
        if contacts:
            print("Contact list:")
            for name, phone_number in contacts.items():
                print(name, ":", phone_number)
        else:
            print("No contacts found.")
    
    elif user_input == "5" or "exit":
        print("Exiting the contact book.")
        break
    
        