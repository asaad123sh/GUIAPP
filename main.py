from cProfile import label
from fileinput import filename
import fractions
from genericpath import isfile
import tkinter as tk
from tkinter import Canvas, Frame, Label, filedialog, Text
import os

root = tk.Tk()
apps=[]


if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempApps = f.read()
        tempApps=tempApps.split(',')
        print(tempApps)
        apps=[x for x in tempApps if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()


    filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("executables","*exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label=tk.Label(frame, text=app, bg="grey")
        label.pack()

def runApp():
    for app in apps:
        os.startfile(app)



canvas = tk.Canvas(root, height=840, width=1248, bg="#263D42")
canvas.pack()


frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


openFile = tk.Button(root, text="OpenFile", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()



runApp=tk.Button(root, text="RunApp", padx=10, pady=5, fg="white", bg="#263D42", command=runApp)
runApp.pack()


for app in apps:
    lable=tk.Label(frame, text=app)
    lable.pack() 



root.mainloop()

with open('save.txt','w') as f:
    for app in apps:
        f.write(app + ',')