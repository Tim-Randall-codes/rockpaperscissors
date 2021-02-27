import tkinter as tk
import random

Window1 = tk.Tk()

plays = 0
wins = 0

def paper():
    ranp = random.randint(1, 3)
    global plays
    global wins
    if ranp == 1:
        plays += 1
        wins += 1
        worl['text'] = "You win!"
        amount['text'] = "You have played "+ str(plays) + " games. You have won "+str(wins)
        compu['text'] = "The computer chose paper"
    else:
        plays += 1
        wins += 0
        worl['text'] = "You lose"
        amount['text'] = "You have played " + str(plays) + " games. You have won "+str(wins)
        if ranp == 2:
            compu['text'] = "The computer chose scissors"
        else:
            compu['text'] = "The computer chose rock"
            
def scissors():
    ranp = random.randint(1, 3)
    global plays
    global wins
    if ranp ==2:
        plays += 1
        wins += 1
        worl['text'] = "You win!"
        amount['text'] = "You have played "+str(plays)+" games. You have won "+str(wins)
        compu['text'] = "The computer chose scissors"
    else:
        plays += 1
        wins += 0
        worl['text'] = "You lose"
        amount['text'] = "You have played " +str(plays)+" games. You have won "+str(wins)
        if ranp ==1:
            compu['text'] = "The computer chose paper"
        else:
            compu['text'] = "The computer chose rock"

def rock():
    ranp = random.randint(1, 3)
    global plays
    global wins
    if ranp == 3:
        plays += 1
        wins += 1
        worl['text'] = "You WIN!"
        amount['text'] = "You have played "+str(plays)+" games. You have won "+str(wins)
        compu['text'] = "The computer chose rock"
    else:
        plays += 1
        wins += 0
        worl['text'] = "You lose"
        amount['text'] = "You have played "+str(plays)+" games. You have won "+str(wins)
        if ranp ==1:
            compu['text'] = "The computer chose paper"
        else:
            compu['text'] = "The computer chose scissors"

explainlabel = tk.Label(Window1, text="Press any button to play against the computer")
explainlabel.grid(column=0, row=0)

paperb = tk.Button(Window1, text="Paper", command=paper)
paperb.grid(row=1, column=0)

scissorsb = tk.Button(Window1, text="Scissors", command=scissors)
scissorsb.grid(row=1, column=1)

rockb = tk.Button(Window1, text="Rock", command=rock)
rockb.grid(row=1, column=2)

worl = tk.Label(Window1, text="")
worl.grid(row=2, column=0)

amount = tk.Label(Window1, text="")
amount.grid(row=3, column=0)

compu = tk.Label(Window1, text="")
compu.grid(row=2, column=1)

Window1.title("Rock, Paper, Scissors")
Window1.mainloop()
