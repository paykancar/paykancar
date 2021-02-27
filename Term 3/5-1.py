import tkinter as tk
import reg

def register():
    reg.register((name.get() , last.get() , birth.get() , code.get())

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

root.mainloop()