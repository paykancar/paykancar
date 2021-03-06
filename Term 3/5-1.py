import tkinter as tk
import reg
import tkinter.ttk as ttk
def srch():
    file = open("names.txt", "r")
    top = tk.Toplevel()
    top.geometry(f"{root.winfo_width()}x{root.winfo_height()}")
    text = tk.Text(top)
    text.grid(row=0, column=0)
    for l in file:
        if search.get() in l:
            text.insert(tk.INSERT, l)




def register():
    reg.register(name.get() , last.get() , birth.get() , code.get())

root = tk.Tk() 

tk.Label(root, text="Name").grid(row=0, column=0)
tk.Label(root, text="Last name").grid(row=1, column=0)
tk.Label(root, text="Birthday").grid(row=2, column=0)
tk.Label(root, text="ID code").grid(row=3, column=0)

name = tk.Entry(root)
name.grid(row=0, column=1)
last = tk.Entry(root)
last.grid(row=1, column=1)
birth = tk.Entry(root)
birth.grid(row=2, column=1)
code = tk.Entry(root)
code.grid(row=3, column=1)

frame = tk.Frame(root)
frame.grid(row=5, column=1, columnspan=1)

tk.Button(frame, text="Register", command=register).grid(row=1, column=0)
tk.Button(frame, text="Cancel", command=root.destroy).grid(row=1, column=1)


ttk.Label(root, text="Search").grid(row=9, column=0)
search = tk.Entry(root) 
search.grid(row=9, column=1)
tk.Button(root, text="Search", command=srch).grid(row=10, column=1, columnspan=2)

root.mainloop()