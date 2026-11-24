from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
text = input("Enter the text which you want to display over their: ")
ttk.Label(frm, text=f"{text}").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()


anotherroot = Tk()

frame = ttk.Frame(anotherroot, padding=230)
frame.grid()
ttk.Notebook(frame)
ttk.Progressbar()
anotherroot.mainloop()