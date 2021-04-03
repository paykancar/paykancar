import tkinter as tt
def up():
    global temp
    temp += 1
    fan()

def down():
    global temp
    temp -= 1
    fan()

def fan():
    temperature.set("Temperature: " + str(temp))
    if temp >= 0:
        fan_state.set("Fan is on")
        label2["background"] = "green"
    else:
        fan_state.set("Fan is off")
        label2["background"] = "red"

root = tt.Tk()
root.geometry("300x150")
temp = 0
temperature = tt.StringVar()
fan_state = tt.StringVar()
button1 = tt.Button(root, text="/\\", command=up)
button2 = tt.Button(root, text="\\/", command=down)
label1 = tt.Label(root, textvariable=temperature)
label2 = tt.Label(root, textvariable=fan_state)
button1.pack()
label1.pack()
button2.pack()
label2.pack()
root.mainloop()