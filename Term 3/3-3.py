import tkinter as tk

root = tk.Tk()
conf = {
    "width":5,
    "height":5,
}
l1 = tk.Label(root, text="L1", font=("times",20),bg="purple")
l1.grid(row=0, column=0)
l2 = tk.Label(root, text="L2", font=("times",20),bg="red")
l2.grid(row=0, column=1, columnspan=2, sticky=tk.E+tk.W)
l3 = tk.Label(root, text="L3", font=("times",20),bg="orange")
l3.grid(row=1, column=0, rowspan=2, sticky=tk.N+tk.S)
l4 = tk.Label(root, text="L4", font=("times",20),bg="blue")
l4.grid(row=1, column=1)
l5 = tk.Label(root, text="L5", font=("times",20),bg="yellow")
l5.grid(row=1, column=2)
l6 = tk.Label(root, text="L6", font=("times",20),bg="brown")
l6.grid(row=2, column=1,columnspan=2, sticky=tk.E+tk.W)

root.mainloop()