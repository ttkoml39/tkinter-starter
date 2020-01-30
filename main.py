# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
window = Tk()         # Create the application window

# Add a label with the text "Welcome", font=("Arial Bold",50))
lbl = Label(window, text="Welcome")

# Place the label in the window at 0, 0
lbl.grid(column=0, row=0)


window.mainloop()     # Keep the window open
from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks app")
window.mainloop()
lbl = Label(window, text="Welcome")
lbl.grid(column=0, row=0)
from tkinter import*
window = Tk()
window.title("welcome to LikeGeeks app")
lbl = Label(window, text="Welcome")
lbl.grid(column=0, row=0)
window.mainloop()
lbl = Label(window, text="Welcome", font=("Arial Bond",50))
window.geometry('350x200')
btn = Button(window, text="Click Me")
btn.grid(column=1, row=0)
from tkinter import*
window = Tk()
window.title("Welcomr to LikeGeeks app")
window.geometry('350x200')
lbl = Label(window, text="welcome")