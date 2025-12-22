import os

def add_expanse ():
    expanse_name = input("Enter the Describe of Expanse")
    expanse_price = input("Enter the amount for your expanse")
    with open("expanses.txt","a") as f:
        f.write(expanse_name,",",expanse_price,"\n")
    print("Saved!")

def view_total():
    total=0
    with open("expanses.txt","r") as f:
         for line in f:
             clean_line = line.string()
             expanse_D_and_P = clean_line.split(",")
             
         
