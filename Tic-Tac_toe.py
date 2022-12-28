from tkinter import *
import random

def next_turn():
    pass

def check_winnner():
    pass

def empty_spaces():
    pass

def new_game():
    pass


window = Tk()
window.title("Tic-Tac_toe made by Me!")
players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=_player + " turn", font=('consolas',40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas' ,20), command=new_game)
reset_button.pack(side="top")

window.mainloop()