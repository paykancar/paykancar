import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

note = ttk.Notebook(root)
note.grid(row=0, column=0)
#################################################
patients = ttk.Frame(note)
note.add(patients, text="Patients")
timers =ttk.Frame(note)
note.add(timers, text="Timers")
#################################################
lf1 = tk.LabelFrame(patients, text="patient1")
lf1.grid(row=0, column=0)

tk.Label(lf1, text="Name").grid(row=0, column=0)
tk.Label(lf1, text="Time").grid(row=1, column=0)
name1 = tk.StringVar()
time1 = tk.StringVar()
tk.Entry(lf1, textvariable=name1).grid(row=0, column=1)
tk.Entry(lf1, textvariable=time1).grid(row=1, column=1)

lf2 = tk.LabelFrame(patients, text="patient2")
lf2.grid(row=1, column=0)

tk.Label(lf2, text="Name").grid(row=0, column=0)
tk.Label(lf2, text="Time").grid(row=1, column=0)
name2 = tk.StringVar()
time2 = tk.StringVar()
tk.Entry(lf2, textvariable=name1).grid(row=0, column=1)
tk.Entry(lf2, textvariable=time1).grid(row=1, column=1)
#################################################
root.mainloop()