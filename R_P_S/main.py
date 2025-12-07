import random

user_score=0
computer_score=0

choice= ("r","p","s")
loop_choice=""



while loop_choice != "1":
    computer_choice=random.choice(choice)
    
    user_choice=input("Ehter you choice for rock paper and scissor :")    
    user_choice= str.lower(user_choice) 
   
    if user_choice in choice:
        
        if user_choice == computer_choice:
            print("Tie")
        elif user_choice == "r" and computer_choice == "s":
            print("User wins ")
            user_score += 1
        elif user_choice == "s" and computer_choice == "r":
            print("com win")
            computer_score += 1
        elif user_choice == "s" and computer_choice == "p":
            print("User wins ")
            user_score += 1
        elif user_choice == "p" and computer_choice == "s":
            print("com win")
            computer_score += 1
        elif user_choice == "p" and computer_choice == "r":
            print("User wins ")
            user_score += 1
        elif user_choice == "r" and computer_choice == "p":
            print("com win")
            computer_score += 1
    else :
        print ("Enter R, P, S")
        
    loop_choice= input("Enter 1 for exit and 2 for score and 3 for continue:")
    loop_choice=loop_choice.lower
    
    if loop_choice == "2":
        print("User score is :",user_score,"Coumputer score is :",computer_score)
    elif loop_choice == "1":
        print("Final score - User :",user_score," Computer :",computer_score)
        print("Thanks for playing")
        break
    elif loop_choice == "3":
        continue
        
    