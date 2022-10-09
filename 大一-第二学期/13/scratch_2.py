import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")
# adding a label
aLabel = ttk.Label(win, text="Enter a name:")
aLabel.grid(column=0, row=0)


def clickMe():
    action.configure(text='Hello~' + name.get())


# adding a button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=1, row=1)
# adding a textbox entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)
win.mainloop()
