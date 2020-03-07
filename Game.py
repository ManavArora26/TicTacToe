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
oWins = 0
xWins = 0
ties = 0


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"


def newGame():
    global con, Win_label
    time.sleep(1)
    for i in range(3):
        for j in range(3):
            board[i][j] = "-"
            btn[i][j].configure(image='', height=5, width=10)
    con = True
    Win_label.config(text="")


def check_game():
    global con
    if board[0][0] == board[0][1] == board[0][2] != "-" or board[1][0] == board[1][1] == board[1][2] != "-" or board[2][0] == board[2][1] == board[2][2] != "-":
        con = False
    elif board[0][0] == board[1][0] == board[2][0] != "-" or board[0][1] == board[1][1] == board[2][1] != "-" or board[0][2] == board[1][2] == board[2][2] != "-":
        con = False
    elif board[0][0] == board[1][1] == board[2][2] != "-" or board[0][2] == board[1][1] == board[2][0] != "-":
        con = False
    else:
        pass


def score():
    global xWins_label, oWins_label, Ties_label, Win_label
    oWins_label.config(text=str(oWins))
    Ties_label.config(text=str(ties))
    xWins_label.config(text=str(xWins))


def gui(event):
    global board, xWins, oWins, ties
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
        if (current_player == "O"):
            oWins += 1
            winner = "Player 2 "
        elif (current_player == "X"):
            xWins += 1
            winner = "Player 2 "
        Win_label.config(text=winner + " Won!")
        newGame()
    tieCheck = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != '-':
                tieCheck += 1
    if tieCheck == 9:
        ties += 1
        Win_label.config(text="It's a Tie!")
        newGame()
    score()


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

canvas = Canvas(root, width=240, height=240, bg="black")
canvas.grid(row=4, column=0, columnspan=3)

Win_label = Label(root, text="",
                  bg="black", fg="white", font="Times 20 bold")
canvas.create_window(100, 75, window=Win_label,  anchor="center")

oWins_label = Label(root, bg="black", fg="white", font="Times 20 bold")
canvas.create_window(60, 125, window=oWins_label,  anchor="center")
Ties_label = Label(root, bg="black", fg="white", font="Times 20 bold")
canvas.create_window(120, 125, window=Ties_label,  anchor="center")
xWins_label = Label(root, bg="black", fg="white", font="Times 20 bold")
canvas.create_window(180, 125, window=xWins_label, anchor="center")

oWinsLabel_label = Label(root, text="Player 1", bg="black",
                         fg="white", font="Times 10")
canvas.create_window(60, 150, window=oWinsLabel_label,  anchor="center")
TiesLabel_label = Label(root, text="Tie", bg="black",
                        fg="white", font="Times 10")
canvas.create_window(120, 150, window=TiesLabel_label,  anchor="center")
xWinsLabel_label = Label(root,  text="Player 2", bg="black",
                         fg="white", font="Times 10")
canvas.create_window(180, 150, window=xWinsLabel_label,  anchor="center")

score()

button2 = Button(text="New Game", command=newGame)
button2.configure(image='', width=10, height=1, bg='white',
                  relief=FLAT, activebackground='black')
canvas.create_window(30, 200, anchor=NW, window=button2)
button1 = Button(text="Exit", command=exit)
button1.configure(image='', width=10, height=1, bg='white',
                  relief=FLAT, activebackground='black')
canvas.create_window(140, 200, anchor=NW, window=button1)

root.mainloop()
