import random

word =["python","java","code"]
s_word = random.choice(word) # select a random world from "word".

live = 5 # normanly its 6 
guessed_l = []

while live > 0 :                
    display_w = ""
    for char in s_word:        # this loop is use for showing "_" for eash letter in s_word.
        if char in guessed_l:
            display_w+=char
        else:
            display_w+="_"
    
    print(display_w)
    print("Lives left: ",live)
    
    if "_" not in display_w: # this check if ther is any "_"(ie. not gussed letter) in the string.
        print("You won!")
        break
    
    guess = input("Guess a letter from a-z")
    guess = guess.lower()  # after taking the guess from user it convet it to lowercase.
    
    if guess in guessed_l: # this check if the letter is already guessed.
        print(" Already guessed ")
        continue 
    
    guessed_l+=guess # not gussed letter are store in guessed_l to check again for next input.
    
    if guess in s_word: 
        print("Good Job!")
    else:
        live = live-1
        print("Wrong letter! try again ")
    
    if live == 0:
        print("Game Over! The word is: ",s_word)    
    