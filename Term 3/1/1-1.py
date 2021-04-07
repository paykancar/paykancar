import tkinter as tk 
def press():
    print(e1.get() + e2.get())
    
# widget (label, entry, button)
root = tk.Tk()
l1 =tk.Label(root, text="Ajisa is comming!")
l1.pack()
e1 = tk.Entry(root)
e1.pack()
e2 = tk.Entry(root)
e2.pack()
b1 = tk.Button(root, text="+", command=press)
b1.pack() 
root.mainloop()