import random
import time
from tkinter import*

root = Tk()
root.geometry("850x500+300+300")
root.title("Puzzle Game")
root.configure(background='Light Blue')

Tops = Frame(root,bg='Light Blue',width=1350,height=100,relief=RIDGE,pady=2)
Tops.grid(row=0,column=0)
lblTitle = Label(Tops,font=("Arial",80,"bold"), text= "Puzzle Game", bd=10,bg="Light Blue",fg="Cornsilk", justify=CENTER)
lblTitle.grid(row=0,column=0)
MainFrame = Frame(root,bg='Powder Blue',width=1350,height=600,relief=RIDGE,bd=10)
MainFrame.grid(row=1,column=0,padx=30)
LeftFrame = Frame(MainFrame,width=700,height=500,relief=RIDGE,bd=10,pady=2,bg="Light Blue")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame,width=540,height=500,relief=RIDGE,bd=10,padx=1,pady=2,bg="Light Blue")
RightFrame.pack(side=RIGHT)

RightFrame1= Frame(RightFrame,width=540,height=200,relief=RIDGE,bd=10,pady=2,padx=1,bg="Light Blue")
RightFrame1.grid(row=0,column=0)

RightFrame2a= Frame(RightFrame,width=540,height=140,relief=RIDGE,bd=10,pady=2,padx=1,bg="Light Blue")
RightFrame2a.grid(row=1,column=0)

RightFrame2b= Frame(RightFrame,width=540,height=140,relief=RIDGE,bd=10,pady=2,padx=1,bg="Light Blue")
RightFrame2b.grid(row=2,column=0)

NumberofClicks=0
displayClicks= StringVar()
displayClicks.set("Number of Clicks "+ "\n" +"0")
gameStateString= StringVar()

def updateCounter():
    global NumberofClicks,displayClicks
    displayClicks.set("Number of Clicks "+ "\n" +str(NumberofClicks) )

def gameStateUpdate(gameState):
    global gameStateString
    gameStateString.set(gameState)

class button:
    def __init__(self,text_,x,y):
        self.enterValue= text_
        self.textTaken= StringVar()
        self.textTaken.set(text_)
        self.x= x
        self.y= y
        self.btnNumber= Button(LeftFrame, textvariable= self.textTaken,font=("Arial",80),bd=3, command=lambda i= self.x, j= self.y : emptySpotChecker (i,j))
        self.btnNumber.place(x= self.x*150, y= self.y*150, width=170, height=170)

def shuffle():
     global btnNumbers,NumberofClicks
     nums = []
     for x in range(12):
         x+=1
         if x==12:
             nums.append("")
         else:
             nums.append(str(x))
     for y in range(len (btnNumbers)):
         for x in range(len (btnNumbers[y])):
             num= random.choice(nums)
             btnNumbers [y][x].textTaken.set(num)
             nums.remove(num)
             NumberofClicks=0
             updateCounter()
             gameStateUpdate("")

lblDisplayClicks= Label(RightFrame1,textvariable=displayClicks,font=("Arial",40)).place(x=0,y=10,width=520, height=160) 
btnShuffle= Button(RightFrame2a, text="New Game",font=("Arial",40),bd=5, command=shuffle).place(x=0,y=10,width=520, height=100) 
       
lblDisplayClicks= Label(RightFrame2b,textvariable=gameStateString,font=("Arial",40)).place(x=0,y=10,width=520, height=100) 
btnNumbers = []
name=0
for y in range(3):
    btnNumbers_=[]
    for x in range(4):
        name+=1
        if name == 12:
            name=" "
        btnNumbers_.append(button(str(name),x,y))
    btnNumbers.append(btnNumbers_)

shuffle()

def emptySpotChecker(y,x):
    global btnNumbers,NumberofClicks

    if not btnNumbers[x][y].textTaken.get()=="":
        for i in range(-1,2):
            newX=x+i

            if not (newX<0 or len(btnNumbers)-1 < newX or i ==0):
                if btnNumbers[newX][y].textTaken.get()=="":
                    text= btnNumbers[x][y].textTaken.get()
                    btnNumbers[x][y].textTaken.set(btnNumbers[newX][y].textTaken.get())
                    btnNumbers[newX][y].textTaken.set(text)
                    WinCheck()
                    break
        for j in range(-1,2):
            newY=y+j

            if not (newY<0 or len(btnNumbers[0])-1 < newY or j ==0):
                if btnNumbers[x][newY].textTaken.get()=="":
                    text= btnNumbers[x][y].textTaken.get()
                    btnNumbers[x][y].textTaken.set(btnNumbers[x][newY].textTaken.get())
                    btnNumbers[x][newY].textTaken.set(text)
                    WinCheck()
                    break
        NumberofClicks+=1
        updateCounter()

def WinCheck():
    lost=False
    for y in range(len(btnNumbers)):
        for x in range(len(btnNumbers[y])):
            if btnNumbers[y][x].enterValue!=btnNumbers[y][x].textTaken.get():
                lost=True
                break
            if not lost:
                gameStateUpdate("You Are Winner!")

root.mainloop()
