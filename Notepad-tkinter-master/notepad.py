import tkinter,os,webbrowser,time
from typing import Counter
from tkinter.constants import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.colorchooser import *
class notepad(tkinter.Tk):
    '''Creates A Notepad'''
    # Variables First letter capital
    # Methods Small
    def __init__(self,title='Untitled',size='448x456'):
        '''Title should be a string,
        size should be string with "widthxheight"'''
        
        super().__init__()
        self.title(title)
        self.geometry(size)
        self.TextArea = tkinter.Text(self)
        self.TextArea.pack(expand=True, fill="both")
        
        # Scroll Bar
        Scrollv = tkinter.Scrollbar(self.TextArea)
        Scrollv.pack(side=RIGHT, fill="y")
        Scrollv.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=Scrollv.set)
        
        # Creating Variables
        self.File=None
        self.FullScreen=False
        self.MenuBar=True
        self.StatusBar=True
        self.Wrap=True
        self.Newwincouter=0
        self.Countertag=0
     
        self.fs=Button(self.TextArea,command=self.fullscreen)
        
    
        # Calling Functions
        self.menubar()
        self.statusbar()
    def menubar(self):

        '''Creates Menu Bar'''
        self.MENUBAR=tkinter.Menu(self,tearoff=0)
        self.config(menu=self.MENUBAR)

        # File Menu
        self.m1=tkinter.Menu(self.MENUBAR,tearoff=0)
        self.m1.add_command(label="New File",command=self.newfile,accelerator="Ctrl+n")
        self.m1.add_command(label="Open File",command=self.openfile,accelerator="Ctrl+o")
        self.m1.add_command(label="Save File",command=self.savefile,accelerator="Ctrl+s")
        self.m1.add_command(label="New Window",command=self.newwindow,accelerator="Ctrl+Alt+n")
        self.m1.add_command(label="Exit",command=self.exit,accelerator="Ctrl+q")
        self.MENUBAR.add_cascade(label="File",menu=self.m1)


        # Edit MenuBar
        self.m2=tkinter.Menu(self.MENUBAR,tearoff=0)
        self.m2.add_command(label="Cut",command=self.cut,accelerator="Ctrl+x")
        self.m2.add_command(label="Copy",command=self.copy,accelerator="Ctrl+c")
        self.m2.add_command(label="Paste",command=self.paste,accelerator="Ctrl+v")
        self.WordWrap=tkinter.Menu(self.m2,tearoff=0)
        self.WordWrap.add_command(label="Character",command=self.character)
        self.WordWrap.add_command(label="Word",command=self.word)
        self.WordWrap.add_command(label="Disable",command=self.disablewrap)
        self.m2.add_cascade(label='Word Wrap',menu=self.WordWrap)
        self.Search=tkinter.Menu(self.m2,tearoff=0)
        self.Search.add_command(label="Google",command=self.google)
        self.Search.add_command(label="Bing",command=self.bing)
        self.Search.add_command(label="DuckDuckGo",command=self.duckduckgo)
        self.m2.add_cascade(label='Search',menu=self.Search)
        self.m2.add_command(label="Delete",command=self.delete)
        self.m2.add_command(label="Delete All",command=self.deleteall,accelerator="Ctrl+d")
        self.MENUBAR.add_cascade(label="Edit",menu=self.m2)

        # View Menu
        self.m3=tkinter.Menu(self.MENUBAR,tearoff=0)
        self.m3.add_command(label="FullScreen",command=self.fullscreen,accelerator="Ctrl+Alt+f")
        
        self.MENUBAR.add_cascade(label="View",menu=self.m3)

        # Format Menu
        self.m4=tkinter.Menu(self.MENUBAR,tearoff=0)
        self.m4.add_command(label="Configure",command=self.formatconfig)
        self.MENUBAR.add_cascade(label="Format",menu=self.m4)
        
        # Help Menu
        self.m5=tkinter.Menu(self.MENUBAR,tearoff=0)
        self.m5.add_command(label="Help",command=self.help)
        self.MENUBAR.add_cascade(label="Help",menu=self.m5)

         # New File
        self.TextArea.bind("<Control_L><n>",self.newfile)
        self.TextArea.bind("<Control_R><n>",self.newfile)
        #Open File
        self.TextArea.bind("<Control_R><o>",self.openfile)
        self.TextArea.bind("<Control_L><o>",self.openfile)
        #Save fIle
        self.TextArea.bind("<Control_L><s>",self.savefile)
        self.TextArea.bind("<Control_R><s>",self.savefile)
       
        #QuitApp
        self.TextArea.bind("<Control_L><q>",self.exit)
        self.TextArea.bind("<Control_R><q>",self.exit)
        #Delete all
        self.TextArea.bind("<Control_R><d>",self.deleteall)
        self.TextArea.bind("<Control_L><d>",self.deleteall)
        # Full Screen
        self.bind("<Control_R><Alt_R><f>",self.fullscreen)
        self.bind("<Control_L><Alt_L><f>",self.fullscreen)
        self.bind("<Control_R><Alt_L><f>",self.fullscreen)
        self.bind("<Control_L><Alt_R><f>",self.fullscreen)
        # New Window
        self.bind("<Control_R><Alt_R><n>",self.newwindow)
        self.bind("<Control_L><Alt_L><n>",self.newwindow)
        self.bind("<Control_R><Alt_L><n>",self.newwindow)
        self.bind("<Control_L><Alt_R><n>",self.newwindow)
    def statusbar(self):
        self.Status=tkinter.Label(self,text="Typing...",justify=CENTER)
        self.Status.pack(side=BOTTOM,fill="x")
        
    
    # TODO File Menu commands
   
    def newfile(self,*args):
        
        if self.File==None:
            
            response=askyesno("Save file","Do you want to save file")
            self.Status.config(text="Save file?")
            if response==YES:
                self.savefile()
            else:
                self.Status.config(text="Typing..")
                self.deleteall()    
        else:
            
            self.deleteall()


    def openfile(self,*args):
        if self.File==None:
            response=askyesno("Save file","Do you want to save file")
            self.Status.config(text="Save file?")
            if response==YES:
                self.savefile()
        
        self.Status.config(text="Open File?")
        self.File=askopenfile(mode='r')
        if self.File==None:    
            pass
        else:
            self.deleteall()
            self.TextArea.insert(1.0,self.File.read())        
            
            self.title(self.File.name)
        self.Status.config(text='Typing...')  
              

    def savefile(self,*args):
        if self.File==None:
            self.Status.config(text="Save File?")
            self.File=asksaveasfile(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if self.File:
            self.Status.config(text="Saving File")
            with open(self.File.name,"w") as f:
                f.write(self.TextArea.get(1.0,END))
            self.title(self.File.name)                             
        self.Status.config(text="Typing...")



    def newwindow(self,*args):
        self.Newwincouter=notepad()
    
    def exit(self,*args):
        self.destroy()   

    # TODO Edit Menu commands
    def cut(self):
        self.TextArea.event_generate(("<<Cut>>"))
    def copy(self):
        self.TextArea.event_generate(("<<Copy>>"))
    def paste(self):
        self.TextArea.event_generate(("<<Paste>>"))
   
    def delete(self):
        self.Status.config(text='Select the Text to delete')
        if self.TextArea.tag_ranges(tkinter.SEL):
            self.TextArea.delete(tkinter.SEL_FIRST,tkinter.SEL_LAST)
            self.Status.config(text='Typing...')
        else:
            self.Status.config(text='No text selected')
            
    def deleteall(self,*args):
        self.TextArea.delete(1.0,END)

    def google(self):
        if self.TextArea.tag_ranges(tkinter.SEL):
            webbrowser.open(f"https://www.google.com/search?q={self.TextArea.get(tkinter.SEL_FIRST, tkinter.SEL_LAST)}")
        else:
            self.StatusBar.config(text="No Text Selected")
    def bing(self):
        if self.TextArea.tag_ranges(tkinter.SEL):
            webbrowser.open(f"https://www.bing.com/search?q={self.TextArea.get(tkinter.SEL_FIRST, tkinter.SEL_LAST)}")
        else:
            self.StatusBar.config(text="No Text Selected")
    def duckduckgo(self):
        if self.TextArea.tag_ranges(tkinter.SEL):
            webbrowser.open(f"https://www.duckduckgo.com/?q={self.TextArea.get(tkinter.SEL_FIRST, tkinter.SEL_LAST)}")
        else:
            self.StatusBar.config(text="No Text Selected")
    

    # TODO View Mwnu Commands
    def fullscreen(self,*args):
        if self.FullScreen==False:
            self.attributes('-fullscreen',True)
            self.FullScreen=True
            self.fs.pack(anchor='ne')
            
        else:
            self.attributes('-fullscreen',False)
            self.FullScreen=False
            self.fs.pack_forget()
            

    def character(self):
        self.TextArea.config(wrap=CHAR)
        self.Wrap=True    
    def word(self):
        self.TextArea.config(wrap=WORD)
        self.Wrap=True
    def disablewrap(self):
        self.TextArea.config(wrap='none')    
        self.Wrap=False
        Scrollh=tkinter.Scrollbar(self.TextArea,orient='horizontal')
        Scrollh.pack(side=BOTTOM, fill='x')
        Scrollh.config(command=self.TextArea.xview)
        self.TextArea.config(xscrollcommand=Scrollh.set)
    # TODO Format Menu commands
    def formatconfig(self):
        self.fc=tkinter.Tk()
        asktextareacolor=tkinter.Button(self.fc,text='Background color',command=self.bgchanger)
        asktextareacolor.pack()
        asktextcolor=tkinter.Button(self.fc,text='Foreground color',command=self.fgchanger)
        asktextcolor.pack()
        
        
    def bgchanger(self):
        Bgcolor=askcolor()
        if Bgcolor[0]==None:
            pass
        else:
            self.TextArea.config(bg=Bgcolor[1])
        self.fc.destroy()    
    def fgchanger(self):
        try:
            if self.TextArea.tag_ranges(tkinter.SEL):
                self.TextArea.tag_add(f'{self.Countertag}',tkinter.SEL_FIRST,tkinter.SEL_LAST)
                self.TextArea.tag_config(f'{self.Countertag}',foreground=f'{askcolor()[1]}')
                self.Countertag+=1
            else:
                self.TextArea.config(foreground=f'{askcolor()[1]}')
        except Exception as e:
            self.Status.config(text='No color selected')
            time.sleep(1)
            self.Status.config(text='Typing...')
        self.fc.destroy()

    # TODO Help Menu commands
    def help(self):
        showinfo('Help',"This is a notepad made by Tanmay Daga.\nFor more contact tanmaydaga06@gmail.com")

if __name__ == "__main__":
    root=notepad()
    root.mainloop()
