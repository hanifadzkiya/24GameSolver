import tkinter as game
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

emblem = ['C', 'D', 'H', 'S']
List_Num = []
List_Card = []
Score = 0
Eval = 0
solution = ''


def InitCard():
    global List_Card

    for em in emblem:
        for i in range(1,13):
            List_Card.append(str(i) + em + '.png')

def GetCard():
    global List_Card

    file_name = random.choice(List_Card)
    List_Card.remove(file_name)     

    return file_name

def Print_Result():
    pos = 500
    global Score
    global solution
    global List_Num
    global Eval

    if len(List_Card) != 0:
        for i in range(4):
            file_name = GetCard()
            if len(file_name)<7:
                List_Num.append(int(file_name[0]))
            else:
                List_Num.append(int(file_name[0]+file_name[1]))
            img = Image.open(file_name)
            img = img.resize((200, 250), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            card = game.Label(root, image=img, bg='green')
            card.x = img
            card.place(x=pos, y=200)
            pos += 250

    sol = game.Label(root,
                text=solution,
                font=('Helvetica', 30, 'bold', 'italic'),
                bg='Green',
                fg='Green')
    sol.place(x=100, y=550)

    val = game.Label(root,
                text="%.2f"%Eval,
                font=('Helvetica', 30, 'bold', 'italic'),
                bg='Green',
                fg='Green')
    val.place(x=100, y=700)

    score = game.Label(root,
                text="%.2f"%Score,
                font=('Helvetica', 30, 'bold', 'italic'),
                bg='Green',
                fg='Green')
    score.place(x=1200, y=600)

def Print_Solution():
    global List_Num

    if len(List_Card) != 0:
        Solver()

        sol = game.Label(root,
                text=solution,
                font=('Helvetica', 30, 'bold', 'italic'),
                bg='Green',
                fg='white')
        sol.place(x=100, y=550)

        val = game.Label(root,
                text="%.2f"%Eval,
                font=('Helvetica', 30, 'bold', 'italic'),
                bg='Green',
                fg='white')
        val.place(x=100, y=700)

        score = game.Label(root,
                text="%.2f"%Score,
                font=('Helvetica', 30, 'bold', 'italic'),
                bg='Green',
                fg='White')
        score.place(x=1200, y=600)

        List_Num = []
    else:
        ExitApplication()


def ExitApplication():
    MsgBox = game.messagebox.askquestion ('Play Again','Your deck is empty, Do you want to play again?',icon = 'warning')
    if MsgBox == 'no':
       root.destroy()
    else:
       InitCard()

def Layout(Card):
    game.Label(root,
             text='WELCOME TO',
             fg='white',
             bg='green',
             font='Helvetica 40 bold italic').pack()

    game.Label(root,
             text='FAKE 24 GAME SOLVER',
             fg='white',
             bg='green',
             font='Helvetica 40 bold italic').pack()

    game.Button(root, image=Card, bg='green',
              command=Print_Result).place(x=100, y=200)

    game.Button(root, text='SOLVE', bg='white', font='Helvetica 30 bold italic',
              command=Print_Solution).place(x=650, y=600)

    game.Label(root,
             text="SOLUTION : ",
             font=('Helvetica', 30, 'bold', 'italic'),
             bg='Green',
             fg='White').place(x=100, y=500)

    game.Label(root,
             text="EVALUATION : ",
             font=('Helvetica', 30, 'bold', 'italic'),
             bg='Green',
             fg='White').place(x=100, y=650)

    game.Label(root,
             text="SCORE : ",
             font=('Helvetica', 30, 'bold', 'italic'),
             bg='Green',
             fg='White').place(x=1200, y=500)

    root.state('zoomed')
    root.configure(background='green')


def Solver():
    global solution
    global Score
    global Eval

    point = 0
    lastsymbol = ""

    # Score += point
    List_Num.sort(reverse = True) #Sort Descending
    solution = str(List_Num[0])
    point = 0
    lastsymbol = ""
    for i in range(1,4):
        #Pertambahan
        maks_equationlocal = solution + "+" + str(List_Num[i]) 
        maks_localpoint = eval(maks_equationlocal)
        lastsymbol_local = "+"
        #Pengurangan
        localequation = solution + "-" + str(List_Num[i]) 
        localpoint = eval(localequation) 
        if(abs(localpoint-24) < abs(maks_localpoint-24)):
            maks_localpoint = localpoint
            maks_equationlocal = localequation
            lastsymbol_local = "-"
        #Perkalian
        localequation = solution + "*" + str(List_Num[i]) 
        localpoint = eval(localequation) 
        if(abs(localpoint-24) < abs(maks_localpoint-24)):
            maks_localpoint = localpoint
            maks_equationlocal = localequation
            lastsymbol_local = "*"
        if(lastsymbol == "+" or lastsymbol == "-"):
            localequation = "(" + solution + ")*" + str(List_Num[i]) 
            localpoint = eval(localequation) 
            if(abs(localpoint-24) < abs(maks_localpoint-24)):
                maks_localpoint = localpoint
                maks_equationlocal = localequation
                lastsymbol_local = "*"
        #Pembagian
        localequation = solution + "/" + str(List_Num[i]) 
        localpoint = eval(localequation)
        if(abs(localpoint-24) < abs(maks_localpoint-24)):
            maks_localpoint = localpoint
            maks_equationlocal = localequation
            lastsymbol_local = "/"
        if(lastsymbol == "+" or lastsymbol == "-"):
            localequation = "(" + solution + ")/" + str(List_Num[i]) 
            localpoint = eval(localequation) 
            if(abs(localpoint-24) < abs(maks_localpoint-24)):
                maks_localpoint = localpoint
                maks_equationlocal = localequation
                lastsymbol_local = "/"
        solution = maks_equationlocal
        maks_global = maks_localpoint
        if(lastsymbol_local == "+"):
            point += 5
        elif(lastsymbol_local == "-"):
            point += 4
        elif(lastsymbol_local == "*"):
            point += 3
        elif(lastsymbol_local == "/"):
            point += 2
    point -= abs(maks_global - 24) - solution.count("(")
    Score = point
    Eval = eval(solution)

if __name__ == '__main__':
    root = game.Tk()

    Card = Image.open("Card.png")
    Card = Card.resize((200, 250), Image.ANTIALIAS)
    Card = ImageTk.PhotoImage(Card)

    InitCard()
    Layout(Card)

    root.mainloop()
