import tkinter as tk

root = tk.Tk()
spin_cnf  = {
    "from_":0,
    "to":9,
    "wrap":True,
    "width":5,
    "font":("TIMS",20)
}
frame = tk.Frame(root)
frame.pack()
spin1 = tk.Spinbox(frame, cnf=spin_cnf)
spin1.pack(side=tk.LEFT)
spin2 = tk.Spinbox(frame, cnf=spin_cnf)
spin2.pack(side=tk.LEFT)
spin3 = tk.Spinbox(frame, cnf=spin_cnf)
spin3.pack(side=tk.LEFT)
b = tk.Button(root, text="Calculate", font=("times",20))
b.pack()
root.mainloop()