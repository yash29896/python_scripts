#!/usr/bin/env python
# coding: utf-8

# In[3]:


key=['    ']*9
plr=[]
valid_input=('X','O')
plr=[]
name_flag=0
played=[]
game_win=False
winner=[]


def print_board():
    print('          |          |           ')
    print(f'   {key[6]}   |    {key[7]}  |    {key[8]}   ')
    print('_____|_____|_____')
    print('          |          |           ')
    print(f'   {key[3]}   |   {key[4]}   |    {key[5]}   ')
    print('_____|_____|_____')
    print('          |          |           ')
    print(f'   {key[0]}   |   {key[1]}   |    {key[2]}   ')
    print('          |          |           ')

def plr_sym_sel():
    if name_flag==0:
        while name_flag==0:
            plr1=input("PLAYER1 select a symbol(X,O)  ").capitalize()
            if plr1 not in valid_input:
                print('INVALID SYMBOL PLEASE CHOOSE BETWEEN (X,O)  ')
                continue
            else:
                name_flag==1
                plr2=[a for a in valid_input if a!=plr1]
                plr.append(plr1[0].strip())
                plr.append(plr2[0].strip())
                return [plr1+' ',plr2[0]+' ']


def enter_sym(x):
    cntr=9

    while True:
        pos=int(input(f"PLAYER{x} TURN :  "))
        print(pos)
        if pos in range(1,10) and pos not in played and cntr !=0:
            key[pos-1]=plr[x-1]
            played.append(pos)
            break
        elif cntr==0:
            print
        else:
            print("ANOTHER PLAYER HAS ALREADY OCCUPIED THAT CELL ")


    


def check_win_logic():

    row=[0]*3
    row[0]=[a.strip() for a in key[:3]]
    row[1]=[a.strip() for a in key[3:6]]
    row[2]=[a.strip() for a in key[6:9]]
    for i in range(0,3):
        if row[i][0] in valid_input and row[i][0]==row[i][1]==row[i][2]:
            winner.append(row[i][0])
            return True
        elif row[0][i] in valid_input and row[0][i]==row[1][i]==row[2][i]:
            winner.append(row[i][0])
            return True
        else:
            pass
        
    if row[0][0] in valid_input and row[0][0]==row[1][1]==row[2][2]:
            winner.append(row[0][0])
            return True
    elif row[0][2] in valid_input and row[0][2]==row[1][1]==row[2][0]:
            winner.append(row[0][2])
            return True
    else:
        return False
               


def declare_winner():
    test=[a.strip() for a in plr]
    if test.index(winner[0].capitalize())==0:
        print("Player1 Wins")
    else:
        print("Player2 Wins")


def play_again():
    response=input("Play Again Y/N")
    return response.capitalize()=='Y'
      


def refresh():
    for n in range(0,9):
        key[n]='    '
    plr.clear()
    global name_flag
    name_flag=0
    played.clear()
    global game_win
    game_win=False
    winner.clear()
    plr.clear()


def game_play():
    while True:
        enter_sym(1)
        print_board()
        game_win=check_win_logic()
        if game_win:
            return True
        elif len(played)==9:
            return False
        enter_sym(2)
        game_win=check_win_logic()
        print_board()
        if game_win:
            return True
        elif len(played)==9:
            return False


while True:
    plr=plr_sym_sel()
    print_board()
    

    
    game_win=game_play()
    
    if game_win:
        declare_winner()
        if not play_again():
            break
        else:
            refresh()
    else:
        print("DRAW")
        if not play_again():
            break
        else:
            refresh()
    
        
            
    


# In[ ]:




