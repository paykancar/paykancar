import tkinter as tk 
import tkinter.ttk as ttk


root = tk.Tk()
note = ttk.Notebook(root)
note.grid(row=0, column=0)

patients = ttk.Frame(note)
note.add(patients, text='Patients')

timers= ttk.Frame(note)
note.add(timers, text='Timers')
##################First row of patients#################
lf1 = tk.LabelFrame(patients, text='Patient 1')
lf1.grid(row=0, column=0)
tk.Label(lf1, text='Name').grid(row=0, column=0)
tk.Label(lf1, text='Time').grid(row=1, column=0)
name1 = tk.StringVar()
time1 = tk.StringVar()

tk.Entry(lf1, textvariable=name1).grid(row=0, column=1)
###################### Timer 1################
f1 = tk.Frame(lf1)
f1.grid(row=1, column=1)
h_p_1 = tk.StringVar()
h_p_1.set("12")
m_p_1 = tk.StringVar()
m_p_1.set("30")
s_p_1 = tk.StringVar()
s_p_1.set("30")
tk.Spinbox(f1, from_=0, to=23, wrap=True, width=2, textvariable=h_p_1, state="readonly").grid(row=0, column=0)
tk.Spinbox(f1, from_=0, to=59, wrap=True, width=2, textvariable=m_p_1, state="readonly").grid(row=0, column=1)
tk.Spinbox(f1, from_=0, to=59, wrap=True, width=2, textvariable=s_p_1, state="readonly").grid(row=0, column=2)

##################Second row of patients###################
lf2 = tk.LabelFrame(patients, text='Patient 2')
lf2.grid(row=1, column=0)
tk.Label(lf2, text='Name').grid(row=0, column=0)
tk.Label(lf2, text='Time').grid(row=1, column=0)
name2 = tk.StringVar()
time2 = tk.StringVar()

tk.Entry(lf2, textvariable=name2).grid(row=0, column=1)
###################### Timer 2################
f2 = tk.Frame(lf2)
f2.grid(row=1, column=1)
h_p_2 = tk.StringVar()
h_p_2.set("12")
m_p_2 = tk.StringVar()
m_p_2.set("30")
s_p_2 = tk.StringVar()
s_p_2.set("30")
tk.Spinbox(f2, from_=0, to=23, wrap=True, width=2, textvariable=h_p_1, state="readonly").grid(row=0, column=0)
tk.Spinbox(f2, from_=0, to=59, wrap=True, width=2, textvariable=m_p_1, state="readonly").grid(row=0, column=1)
tk.Spinbox(f2, from_=0, to=59, wrap=True, width=2, textvariable=s_p_1, state="readonly").grid(row=0, column=2)

##################Third row of patients###################
lf3 = tk.LabelFrame(patients, text='Patient 3')
lf3.grid(row=2, column=0)
tk.Label(lf3, text='Name').grid(row=0, column=0)
tk.Label(lf3, text='Time').grid(row=1, column=0)
name3 = tk.StringVar()
time3 = tk.StringVar()
###################
tk.Entry(lf3, textvariable=name3).grid(row=0, column=1)

###################### Timer 3################
f3 = tk.Frame(lf3)
f3.grid(row=1, column=1)
h_p_3 = tk.StringVar()
h_p_3.set("12")
m_p_3 = tk.StringVar()
m_p_3.set("30")
s_p_3 = tk.StringVar()
s_p_3.set("30")
tk.Spinbox(f3, from_=0, to=23, wrap=True, width=2, textvariable=h_p_3, state="readonly").grid(row=0, column=0)
tk.Spinbox(f3, from_=0, to=59, wrap=True, width=2, textvariable=m_p_3, state="readonly").grid(row=0, column=1)
tk.Spinbox(f3, from_=0, to=59, wrap=True, width=2, textvariable=s_p_3, state="readonly").grid(row=0, column=2)

##############First row of timer##################
p1 = tk.StringVar()
p1.set('Patient1')
tk.Label(timers, textvariable=p1).grid(row=0, column=0, padx=10, pady=10)
############################################################################
p2 = tk.StringVar()
p2.set('Patient2')
tk.Label(timers, textvariable=p2).grid(row=0, column=1,  pady=10)
############################################################################
p3 = tk.StringVar()
p3.set('Patient3')
tk.Label(timers, textvariable=p3).grid(row=0, column=2, padx=10, pady=10)
############################################################################
t1 = tk.StringVar()
t1.set("00:00:00")
tk.Label(timers, textvariable=t1).grid(row=1, column=0)
tk.Button(timers, text="start").grid(row=2, column=0)

t2 = tk.StringVar()
t2.set("00:00:00")
tk.Label(timers, textvariable=t2).grid(row=1, column=1)
tk.Button(timers,text="start").grid(row=2, column=1)

t3 = tk.StringVar()
t3.set('00:00:00')
tk.Label(timers, textvariable=t3).grid(row=1, column=2)
tk.Button(timers, text="start").grid(row=2, column=2)
########################################################################################
tk.Button(timers, text="cancel", bg="red").grid(row=4, column=0, sticky=tk.E+tk.W, columnspan=3)
####################################################################################################
def cal():
    val = .get()+ .get()+ .get()
    label.config(text=val)
root.mainloop()
