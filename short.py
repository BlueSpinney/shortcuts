import time
from tkinter import *
import tkinter
import pyautogui
import webbrowser
import random
from random import randint
from tkinter import messagebox
import os
from cryptography.fernet import Fernet
import subprocess






window = Tk()

counter = 0

yes = True


def b2():
    webbrowser.open('https://www.youtube.com/')
def b3():
    os.system('cmd /k"C: & cd C:\Program Files\Google\Chrome\Application\ & chrome.exe & exit"')

def something():
        warning = messagebox.askquestion("warning", "you are about to make something DAB")
        if warning == 'yes':
            
            var1 = randint(0, 11)
            if var1 == 1:
                b2()
            elif var1 == 2:
                b3()        
            elif var1 == 3:
                b6()
            elif var1 == 4:
                b8()
            elif var1 == 5:
                b10()
            elif var1 == 6:
                b11()
            elif var1 == 7:
                b12()
            elif var1 == 8:
                b18()
            elif var1 == 9:
                showposition()
            elif var1 == 10:
                love()
             
def b6():
    position = [0,0]
    messagebox.showinfo("mouse is cute","place your mouse")
    time.sleep(10)
    position = pyautogui.position()
    for each in range(100):
        pyautogui.click(position)      

 
def b8():
    webbrowser.open('https://www.youtube.com/watch?v=s-Dq5FJEH10')   
    
def b10():
    webbrowser.open('https://www.youtube.com/watch?v=LDU_Txk06tM')     

def b11():
    
    os.system('cmd /k"spotify.exe & exit"')
    pyautogui.click(0,0)
    time.sleep(3)
    pyautogui.click(866, 1017)
    pyautogui.click(1136, 975)
def b12():
    webbrowser.open('https://www.youtube.com/watch?v=KfNW2OmdumI&t=2555s')  


def b18():
    reslut = messagebox.askquestion("you look great today", "please plase youre mouse")
    if reslut == 'yes':
        
       time.sleep(5)
       position = pyautogui.position()
       text2.configure(text="youre mouse is at :" + '\n' + str(position))
       text2.pack()
def showposition():
    global yes
 
    position = pyautogui.position()

    text3.configure(text=position)
    text3.pack()
    if yes == True:

        text3.after(10,showposition)

    else:
        yes = True
        text3.configure(text="")
        

def add1():
    global yes
    yes = False
    
def b16():
    
    pathTO = var2.get()
    programm = var1.get()
    
    if var2.get() == "play" or var2.get() == "play ":
        if var1.get() == "play list":
            os.system('cmd /k"spotify.exe & exit"')
            time.sleep(3)
            pyautogui.click(500,100)
            pyautogui.click(445, 562)
            time.sleep(1)
            pyautogui.click(601, 522)
            var1.delete(0,END)
            var2.delete(0,END)
        else: 
            
            os.system('cmd /k"spotify.exe & exit"')
            time.sleep(4)
            pyautogui.click(500,100)
            pyautogui.click(415, 102)
            time.sleep(1)
            pyautogui.click(800, 26)
            pyautogui.typewrite(var1.get())
            time.sleep(2)
            pyautogui.click(1033, 136)
            pyautogui.click(1033, 136)
            pyautogui.click(859, 1013)
            pyautogui.click(983, 31)
            pyautogui.press('backspace',presses=50)
            var1.delete(0,END)
            var2.delete(0,END)
        
    elif var2.get() == "search" or var2.get() == "search ":
        
        os.system('cmd /k"C: & cd C:\Program Files\Google\Chrome\Application\ & chrome.exe & C: & exit"')
        print("test")
        pyautogui.click(500,100)
        time.sleep(2)
        pyautogui.click(818, 414)
        pyautogui.typewrite(var1.get())
        pyautogui.press('enter')
        var1.delete(0,END)
        var2.delete(0,END)
        
        
    elif var2.get() == "watch" or var2.get() == "watch ":
        webbrowser.open('https://www.youtube.com/')
        time.sleep(3)
        pyautogui.click(642, 96)
        pyautogui.typewrite(var1.get())
        pyautogui.press('enter')
        var1.delete(0,END)
        var2.delete(0,END)
        
    elif var2.get() == "open" or var2.get() == "open ":
        pyautogui.click(178,1070)
        pyautogui.typewrite(var1.get())
        pyautogui.press('enter')
        var1.delete(0,END)
        var2.delete(0,END)
    
    elif var2.get() == "!axis" or var2.get() == "!getaxis" or var2.get() == "!axis " or var2.get() == "!getaxis ":
        if var1.get() == "twitch":
            webbrowser.open('https://www.twitch.tv/')
        else:
            webbrowser.open_new(var1.get())
    elif pathTO[0:4] == "!cmd":
        
        print("\n")
        print("the variables are set do you wish to procede y/n" + '\n' + "location : " + pathTO[5:100] + '\n' + "name : " + programm)
        
        choice1 = input()
        
        if choice1 == "y":
                        
            print("\n")    
            os.system('cmd /k "cd "' + pathTO[5:100] + '"&"' + '"pyinstaller --onefile "' + programm + '".py & exit"')
            choice1 = ""
        else:
         print("\n")
         print("programm assably aborded")
         choice1 = ""

    else:
        
       with open('notes.txt' , "a") as file:
          file.write("- " + var1.get() + "\n \n")
    var1.delete(0,END)
    var2.delete(0,END)      
def love():
    
    global counter
    if counter == 0: 
        text.configure(text="      ///     /// \n    //////////////\n  /////////////////\n   /////////////// \n    //////////// \n     ////////// \n      //////// \n       ///// \n        // \n") 
        counter = 1
    elif counter == 1:
        text.configure(text="")
        counter = 0
        
window.title("dab")
window.configure(width=500, height=300)
window.configure(bg='lightgray')
window.attributes('-topmost', True)
 

button2 = Button (window,text="make youtube dab",command=b2)
    
button3 = Button (window,text= "make googel dab",command=b3)

button4 = Button (window,text= "make something dab",command=something)

button6 = Button (window,text= "click click",command=b6)

button8 = Button (window,text= "make tetris dab",command=b8)

button10 = Button (window,text= "make crabs dab",command=b10)

button11 = Button (window,text= "make party dab",command=b11)

button12 = Button (window, text= "make hacking dab", command=b12)

button16 = Button(window,text="do as I say",command=b16)

button17 = Button(window,text="love <3",command=love)

button18 = Button(window,text="mouse position",command=b18)

button21 = Button(window,text="show mouse position",command=showposition)

button22 = Button(window,text="hide mouse position",command=add1)




var1 = Entry(window,bd= 2.5)

var2 = Entry(window,bd= 5)

text = Label(window,text="",background= 'lightgray')

text2 = Label(window,text="",background= 'lightgray',font=('Arial',10))

text3 = Label(window,text="",font=('Arial',25),background='lightgray')



button2.pack()
button3.pack()
button4.pack()
button6.pack()
button8.pack()
button10.pack()
button11.pack()
button12.pack()
button18.pack()
button21.pack()
button22.pack()
button16.pack()
var2.pack()
var1.pack()
button17.pack()
text.pack()
window.mainloop()

