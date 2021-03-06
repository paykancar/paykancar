import tkinter as tk
import reg
import tkinter.ttk as ttk

def srch():
    file = open("names.txt", "r")
    top = tk.Toplevel()
    top.geometry(f"{root.winfo_width()}x{root.winfo_height}")
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

            






def register():
    reg.register(name.get() , last.get() , birth.get() , code.get())

root = tk.Tk() 

tk.Label(root, text="Name").grid(row=0, column=0)
tk.Label(root, text="Last name").grid(row=1, column=0)
tk.Label(root, text="Birthday").grid(row=2, column=0)
tk.Label(root, text="ID code").grid(row=3, column=0)

name = tk.StringVar()
n1 = tk.Entry(root, textvariable=name)
n1.grid(row=0, column=1)
last = tk.StringVar()
l1 = tk.Entry(root, textvariable=last)
l1.grid(row=1, column=1)
birth = tk.StringVar()
b1 = tk.Entry(root, textvariable=birth)
b1.grid(row=2, column=1)
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