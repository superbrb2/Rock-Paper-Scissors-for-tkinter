from tkinter import *
import random
from tkinter.font import Font
import time

HEIGHT = 600
WIDTH = 700
images = False
player_RPS = ''
com_RPS = 'Scissors'


root = Tk()
root.title('Rock Paper Scissors')



def Com_turn(player_RPS):
    i = random.randint(1,3)

    if i == 1:
        com_RPS = 'Rock'
    if i == 2:
        com_RPS = 'Paper'
    if i == 3:
        com_RPS = 'Scissors'

    Compare_hands(player_RPS, com_RPS)



def Rock_button():
    global player_RPS
    player_RPS = 'Rock'
    Com_turn(player_RPS)


def Paper_button():
    global player_RPS
    player_RPS = 'Paper'
    Com_turn(player_RPS)
    

def Scissors_button():
    global player_RPS
    player_RPS = 'Scissors'
    Com_turn(player_RPS)
   

def Image_place():
    global com_RPS, player_RPS

    if player_RPS == 'Rock':
        RIL = Label(big_frame, image=Rock_image)
        RIL.place(relx=0.075, rely=0.5, relwidth=0.36,relheight=0.4)  
        
    if com_RPS == 'Rock':
        RIR = Label(big_frame, image=Rock_image)
        RIR.place(relx=0.55, rely=0.5, relwidth=0.36,relheight=0.4)

    if  player_RPS == 'Paper':
        PIL = Label(big_frame, image=Paper_image)
        PIL.place(relx=0.075, rely=0.5, relwidth=0.36,relheight=0.4) 

    if com_RPS == 'Paper':
        PIR = Label(big_frame, image=Paper_image)
        PIR.place(relx=0.55, rely=0.5, relwidth=0.36,relheight=0.4) 

    if player_RPS == 'Scissors':
        SIL = Label(big_frame, image=Scissors_image)
        SIL.place(relx=0.075, rely=0.5, relwidth=0.36,relheight=0.4)  

    if com_RPS == 'Scissors':
        SIR = Label(big_frame, image=Scissors_image)
        SIR.place(relx=0.55, rely=0.5, relwidth=0.36,relheight=0.4)  
    


def Compare_hands(player_RPS, com_RPS):

    if player_RPS == 'Rock':
        if player_RPS == 'Paper':
            win = 'Lose'
        else:
            win = 'Win'
    if player_RPS == 'Paper':
        if com_RPS == 'Scissors':
            win = 'Lose'
        else: 
            win = 'Win'
    if player_RPS == 'Scissors':
        if com_RPS == 'Rock':
            win = 'Lose'
        else:    
            win = 'Win'

    if player_RPS == com_RPS:
        win = 'Draw'

    results = "Your Move:\n" + player_RPS + "\n Computer's move:\n" + com_RPS + '\n\n' + win + '!'

   
    time.sleep(0.1)
    label['text'] = (results) 
    
    Image_place()
    



# --------------------------------------------------------------CANVAS
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
 
# --------------------------------------------------------------BACKGROUND
background = Frame(root, bg='light blue')
background.place(relheight=1, relwidth=1)

# --------------------------------------------------------------FRAMES
big_frame = Frame(root, bg='grey')
big_frame.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)


user_frame = Frame(big_frame, bg='light grey', bd=5)
user_frame.place(relheight=0.1, relwidth=0.9, rely=0.1, relx=0.05)

#--------------------------------------------------------------LABELS
label = Label(big_frame, font=('courier', 19), anchor='n', justify='center', bg='light grey', bd = 3)
label.place(relwidth=0.9, relheight=0.7, relx=0.05, rely=0.25)

#---------------------------------------------------------------IMAGES
Rock_image = PhotoImage(file='Final/images/rock.png')
Paper_image = PhotoImage(file='Final/images/paper.png')
Scissors_image = PhotoImage(file='Final/images/scissors.png')

#---------------------------------------------------------------BUTTONS

Rock = Button(user_frame, text='Rock', font=10, command=Rock_button)
Rock.place(relx=0.1, relheight=1, relwidth=0.2)


Paper = Button(user_frame, text='Paper', font=10, command=Paper_button)
Paper.place(relx=0.4, relheight=1, relwidth=0.2)
 

Scissors = Button(user_frame, text='Scissors', font=10, command=Scissors_button)
Scissors.place(relx=0.7, relheight=1, relwidth=0.2)


root.mainloop()
