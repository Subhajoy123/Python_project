# The Rock_paper_scissor game
import random
print(" Rules  \n Rock breaks scissor \n scissor cuts paper \n paper covers rock \n") 
  
while True: 
    print("Enter choice \n 1. Rock \n 2. scissor \n 3. paper \n") 
     
    c= int(input(" Enter your choice "))  
    if c>3 or c<1: 
        c = int(input(" Enter a valid choice ")) 
    if c == 1: 
        n = "Rock"
    elif c == 2: 
        n = "Scissor"
    else: 
        n = "paper"  
    print("user choice is: ",n) 
    print("\n --computer's turn--")  
    m = random.randint(1, 3) 
    if m == 1: 
        co = "Rock"
    elif m == 2: 
        co = "Scissor"
    else: 
        co = "paper"
          
    print("Computer'c choice is: ",co)
    if c==m :
        r='d'
    elif (c == 1 and m == 2) or (c == 2 and m == 3) or (c == 3 and m == 1): 
        r='w'
    else: 
        r='l' 
    if r=='w': 
        print("\n CONGRATULATIONS you win!! ")
        
    elif r=='d': 
        print("\n It's a draw match!! ")
    else:
        print("\n SORRY you lose!! ")
    
    p = input(" \n \n Do you want to play again? (Y/N) \n") 
    if (p == 'n' or p == 'N'):
        break
print("\nThank you for playing ")
