my_list=['','O','']
from random import shuffle


def user_guess():
    guess=''
    while guess not in ['1','2','3']:
        guess=input("Pick ball position no.- 1 / 2 /3:  ")
    return int(guess)

def shuffle_list():
    shuffle(my_list)
    return my_list

def check_guess(gussed_index,mixedup_list):  # using variables of other funcitions as required arguments.
    if mixedup_list[gussed_index-1]=='O':
        print("correct guess")
    else:
         print("incorrect guess")
    
mixedup_list=shuffle_list()
gussed_index=user_guess()
check_guess(gussed_index,mixedup_list)
print(mixedup_list)