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
root.mainloop()