choice_list=[" "," "," "," "," "," "," "," "," "]


def display_board(choice_list):
    print("        0           |           1          |        2            ")
    print("        3           |           4          |        5            ")
    print("        6           |           7          |        8            ")
        
    
    print(f"{ choice_list[0]}  |   { choice_list[1]}  |   { choice_list[2]}")
    print(f"{ choice_list[3]}  |   { choice_list[4]}  |   { choice_list[5]}")
    print(f"{ choice_list[6]}  |   { choice_list[7]}  |   { choice_list[8]}")


def player1_choice():
    choice1='wrong'
    acceptable_range=range(0,9)  # allows values from o to 8
    within_range=False
    
    while choice1.isdigit()==False or within_range==False:
        choice1=input("Player 1: Pick a position (0-8) ")
        
        if choice1.isdigit()==False:
            print("Sorry ! invalid choice ! ")
        
        
        if choice1.isdigit()==True:
            if int(choice1) in acceptable_range:
                within_range=True
                
                
            else:
                print("Sorry ! invalid choice ! ")
        
                within_range=False
                
    return int(choice1)


def user_position_p1(choice_list,choice1):
    user_placement=input("Type X to place at your selectd choice: ")
    choice_list[choice1]=user_placement
    
    return choice_list

def player2_choice():
    choice2='wrong'
    acceptable_range=range(0,9)  # allows values from o to 8
    within_range=False
    
    while choice2.isdigit()==False or within_range==False:
        choice2=input("Player 2:Pick a position (0-8) ")
        
        if choice2.isdigit()==False:
            print("Sorry ! invalid choice ! ")
        
        
        if choice2.isdigit()==True:
            if int(choice2) in acceptable_range:
                within_range=True
                
                
            else:
                print("Sorry ! invalid choice ! ")
        
                within_range=False
                
    return int(choice2)

def user_position_p2(choice_list,choice2):
    user_placement=input("Type O to place at your selectd choice: ")
    choice_list[choice2]=user_placement
    
    return choice_list

def game_rule(choice_list):
    if choice_list[0]==choice_list[1]==choice_list[2]=='X' or choice_list[0]==choice_list[1]==choice_list[2]=='O':
        print(f"Game Over !")
        return False
    elif choice_list[3]==choice_list[4]==choice_list[5]=='X' or choice_list[3]==choice_list[4]==choice_list[5]=='O':
        print(f"Game Over !")
        return False
    elif choice_list[6]==choice_list[7]==choice_list[8]=='X' or choice_list[6]==choice_list[7]==choice_list[8]== 'O':
        print(f"Game Over !")
        return False
    elif choice_list[0]==choice_list[3]==choice_list[6]=='X' or choice_list[0]==choice_list[3]==choice_list[6]== 'O':
        print(f"Game Over !")
        return False
    elif choice_list[1]==choice_list[4]==choice_list[7]=='X' or choice_list[1]==choice_list[4]==choice_list[7]== 'O':
        print(f"Game Over !")
        return False
    elif choice_list[2]==choice_list[5]==choice_list[8]=='X' or choice_list[2]==choice_list[5]==choice_list[8]== 'O':
        print(f"Game Over !")
        return False
    elif choice_list[0]==choice_list[4]==choice_list[8]=='X' or choice_list[0]==choice_list[4]==choice_list[8]== 'O':
        print(f"Game Over !")
        return False
    elif choice_list[2]==choice_list[4]==choice_list[6]=='X' or choice_list[2]==choice_list[4]==choice_list[6]== 'O':
        print(f"Game Over !")
        return False
    
    
def gameon_choice():
    choice="wrong"
    while choice not in ['Y','N']:
        choice=input("Do you wana play again? Y/N: ")
        if choice == 'Y':
            return True 
        if choice == 'N':
            return False  
 
 

choice_list=[" "," "," "," "," "," "," "," "," "]

def clear_display_board(choice_list):
    print(f"{ choice_list[0]}  |   { choice_list[1]}  |   { choice_list[2]}")
    print(f"{ choice_list[3]}  |   { choice_list[4]}  |   { choice_list[5]}")
    print(f"{ choice_list[6]}  |   { choice_list[7]}  |   { choice_list[8]}")


gameon=True 

while gameon==True:
    
    r=True
    
    while r==True:
        display_board(choice_list)
        choice1=player1_choice()
        choice_list=user_position_p1(choice_list,choice1)

        display_board(choice_list)
        r=game_rule(choice_list)
        if r==False:
            gameon=gameon_choice()
            if gameon==True:
                from IPython.display import clear_output
                clear_output(wait=True)
                choice_list=[" "," "," "," "," "," "," "," "," "]
                clear_display_board(choice_list)
                
                break
            else:
                print("Thanks for Playing Tic Tac Toe Game !")
                break 
        print("--------------------------------------------------------------------")
        print("--------------------------------------------------------------------")
        
#         display_board(choice_list)
        choice2=player2_choice()
        choice_list=user_position_p2(choice_list,choice2)

        display_board(choice_list)
        r=game_rule(choice_list)
        if r==False:
            gameon=gameon_choice()
            if gameon==True:
                from IPython.display import clear_output
                clear_output(wait=True)
                choice_list=[" "," "," "," "," "," "," "," "," "]
                clear_display_board(choice_list)
 
                
                break
            else:
                print("Thanks for Playing Tic Tac Toe Game !")
                break
        print("--------------------------------------------------------------------")
        print("--------------------------------------------------------------------")
