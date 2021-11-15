import tkinter,os,sys
from tkinter.constants import ANCHOR, BOTH, CENTER, TRUE
from tkinter.filedialog import askdirectory
root=tkinter.Tk()#Intialisiation of window
root.geometry('550x300')#setting size
root.title("Ide opener")

#Setting up mainframe
mainframe=tkinter.Frame(root,bg='gray1')
mainframe.pack(fill=BOTH,expand=TRUE) #Packking mainframe in root

#*****************************widgets in mainframe******************************************

# Path setting
path_var=tkinter.StringVar()
path_var.set("C:\\Users\\Tanmay Daga\\Documents\\Programming")
path_entry_box=tkinter.Entry(mainframe,textvariable=path_var,width=65,font="k 11 bold ",fg="chartreuse4")
path_entry_box.grid(row=0,column=0)

# Function for button
def openfolder():
    path=askdirectory()
    if path:
        path_var.set(path.replace("/","\\"))
        root.update()
# Setting up button
tkinter.Button(mainframe,text=". . .",command=openfolder).grid(row=0,column=1)

#Setting up options
vscode_var=tkinter.IntVar()
vscode_option=tkinter.Checkbutton(mainframe,text="VsCode",bg="gray1",fg="white",font="k 11 bold",variable=vscode_var,onvalue=1,selectcolor="gray1")
vscode_option.grid(row=3,column=0,sticky="w",ipady=5)

terminal_var=tkinter.IntVar()
terminal_option=tkinter.Checkbutton(mainframe,text="Terminal",bg="gray1",fg="white",font="k 11 bold",variable=terminal_var,onvalue=1,selectcolor="gray1")
terminal_option.grid(row=4,column=0,sticky="w")

intellij_var=tkinter.IntVar()
intellij_option=tkinter.Checkbutton(mainframe,text="Intellij",bg="gray1",fg="white",font="k 11 bold",variable=intellij_var,onvalue=1,selectcolor="gray1")
intellij_option.grid(row=5,column=0,sticky="w")

pycharm_var=tkinter.IntVar()
pycahrm_option=tkinter.Checkbutton(mainframe,text="Pycharm",bg="gray1",fg="white",font="k 11 bold",variable=pycharm_var,onvalue=1,selectcolor="gray1")
pycahrm_option.grid(row=6,column=0,sticky="w")

def ok_button():
    print(path_var.get())
    if bool(vscode_var.get()):
        os.system(f"cd \"{path_var.get()}\"")
        os.system("Code -n .")
    if bool(terminal_var.get()):
        os.system(f"start cmd /K cd \"{path_var.get()}\"") 
    if bool(intellij_var.get()):
        os.system(f"idea \"{path_var.get()}\"")
    if bool(pycharm_var.get()):
        os.system(f"pycharm \"{path_var.get()}\"")
    
tkinter.Button(mainframe,text="OK",width=5,font="k 11 bold",command=ok_button).grid(row=7,column=0,sticky="e")
tkinter.Button(mainframe,text="Exit",width=5,font="k 11 bold",command=sys.exit).grid(row=8,column=0,sticky="e")


root.mainloop()#Runnig the window
