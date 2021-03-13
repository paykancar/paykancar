import tkinter as tk
import reg
import tkinter.ttk as ttk
from tkcalendar import DateEntry

def srch():
    file = open("names.txt", "r")
    top = tk.Toplevel()
    top.geometry(f"{root.winfo_width()}x{root.winfo_height()}")
    text = tk.Text(top)
    text.grid(row=0, column=0)
    for l in file:
        if search.get() in l:
            text.insert(tk.INSERT, l)

def callback(a ,b ,c):
    c = code.get()
    c1.config(bg="red")
    if c.isdigit():
        if len(c) == 10:
            c1.config(bg="green")
        elif len(c) > 10:
                code.set(c[:10])
                c1.config(bg="green")
    elif len(c) > 10:
        code.set(c[:10])

def alphabet1(a, b, c):
    if name.get().isalpha():
        n1.config(bg="green")
    else:
        n1.config(bg="red")
        
def alphabet2(a, b, c):
    if last.get().isalpha():
        l1.config(bg="green")
    else:
        l1.config(bg="red")

def register(a=None):
    reg.register
    (
    name.get() ,
    last.get() ,
    birth.get() ,
    code.get()
    )

    name.set("")
    last.set("") 
    code.set("")
    n1.config(bg="white")
    l1.config(bg="white")
    c1.config(bg="white")
    
root = tk.Tk() 
root.bind("<Return>", register)

tk.Label(root, text="Name").grid(row=0, column=0)
tk.Label(root, text="Last name").grid(row=1, column=0)
tk.Label(root, text="Birthday").grid(row=2, column=0)
tk.Label(root, text="ID code").grid(row=3, column=0)

name = tk.StringVar()
name.trace("w", alphabet1)

n1 = tk.Entry(root, textvariable=name)
n1.grid(row=0, column=1)

last = tk.StringVar()
last.trace("w", alphabet2)

l1 = tk.Entry(root, textvariable=last)
l1.grid(row=1, column=1)

birth = tk.StringVar()
b1 = DateEntry(root, width=12, background="darkred", foreground="blue",
 borderwidth=2, date_pattern="y-mm-dd")
b1.grid(row=2, column=1, sticky="we")

code = tk.StringVar()
code.trace("w", callback)

c1 = tk.Entry(root, textvariable=code)
c1.grid(row=3, column=1)

frame = tk.Frame(root)
frame.grid(row=5, column=1, columnspan=1)

tk.Button(frame, text="Register", command=register).grid(row=1, column=0)
tk.Button(frame, text="Cancel", command=root.destroy).grid(row=1, column=1)


ttk.Label(root, text="Search").grid(row=9, column=0)
search = tk.Entry(root) 
search.grid(row=9, column=1)
tk.Button(root, text="Search", command=srch).grid(row=10, column=1, columnspan=2)

root.mainloop()