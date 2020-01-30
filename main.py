# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library        # Create the application window

# Add a label with the text "Welcome", font=("Arial Bold",50))

   # Keep the window open
window = Tk() 
window.title("Welcome to LikeGeeks app")
lbl = Label(window, text="Welcome")
lbl.grid(column=0, row=0)
lbl = Label(window, text="Welcome")
lbl.grid(column=0, row=0)
lbl = Label(window, text="Welcome", font=("Arial Bond",50))
window.geometry('350x200')
btn = Button(window, text="Click Me")
btn.grid(column=1, row=0)
lbl = Label(window, text="welcome")
lbl.grid(column=0, row=0)
btn = Button(window, text="Click Me")
btn.grid(column=1, row=0)
btn = Button(window, text="Click Me", bg="orange",fg="red")
def clicked():
    lbl.configure(text="Button was clicked !!")
lbl = Label(window, text="Welcome")
lbl.grid(column=0, row=0)
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=2)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
def cicked():
    lbl.configure(text="Button was clicked !!")
txt = Entry(window,width=10)
window.mainloop()