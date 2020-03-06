from tkinter import *
import time
import random
root = Tk()
root.title("Tic Tac Toe")
# root.iconbitmap('.ico')

oImage = PhotoImage(file="oImage.png")
xImage = PhotoImage(file="xImage.png")

btn, board = [], []

current_player = "X"
con = True
winner = None


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"


def newGame():
    for i in range(3):
        for j in range(3):
            board[i][j] = "-"


def check_game():
    global con
    if board[0][0] == board[0][1] == board[0][2] != "-" or board[1][0] == board[1][1] == board[1][2] != "-" or board[2][0] == board[2][1] == board[2][2] != "-":
        winner = current_player
        con = False
    elif board[0][0] == board[1][0] == board[2][0] != "-" or board[0][1] == board[1][1] == board[2][1] != "-" or board[0][2] == board[1][2] == board[2][2] != "-":
        winner = current_player
        con = False
    elif board[0][0] == board[1][1] == board[2][2] != "-" or board[0][2] == board[1][1] == board[2][0] != "-":
        winner = current_player
        con = False
    else:
        pass


def gui(event):
    global board
    b = event.widget
    x = str(b.cget('textvariable'))
    x, y = int(x[0]), int(x[2])
    col = "white"
    check_game()
    if con:
        if board[x][y] == '-':
            board[x][y] = current_player
            if (current_player == "X"):
                photo = xImage
            elif (current_player == "O"):
                photo = oImage
            b.configure(image=photo, height=80, width=72)
            flip_player()
    check_game()
    if con == False:
        flip_player()
        print(current_player + " Wins!")
        root.destroy()
    tie = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != '-':
                tie += 1
    if tie == 9:
        print("Its a Tie!")
        root.destroy()


'''--------------------Main------------------------'''

for i in range(3):
    board.append(['-', '-', '-'])
    b = []
    for j in range(3):
        col = "white"
        b.append(Button(bg=col, height=5, width=10, textvariable=[i, j]))
        b[j].grid(row=i, column=j)
        b[j].bind("<ButtonRelease-1>", gui)
    btn.append(b)
root.mainloop()
