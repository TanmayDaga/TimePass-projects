# This is a calculator created by Tanmay
import getpass
from os import mkdir
import tkinter,os,time
from functools import partial
from tkinter import PhotoImage
from tkinter.constants import SEL
class Calculator(tkinter.Tk):
    '''This class creates calculator using tkinter module'''
    def __init__(self):
        super().__init__()
        
        # Changing height and width of window
        self.geometry('279x316')
        self.resizable(False,False)
        self.title('Calculator')
        image=PhotoImage('download.ico')
        self.iconbitmap(image)
        # Creating tkinter varible to store what user has entered
        self.__store_value=tkinter.StringVar()
        self.__store_value.set('')
        #Creating entry widget for input
        self.__input_user=tkinter.Entry(self,font='lucidia 20 bold',textvariable=self.__store_value) 
        self.__input_user.pack(fill='x')
        self.bind('<Return>',partial(self.click,'='))
        # This Buttons will be ther in calculator
        self._button_dict={"C":"C","(":"(",")":")","/":"/",
                          "9":9,"8":8,"7":7,"*":"*",
                          "6":6,"5":5,"4":4,"+":"+",
                          "3":3,"2":2,"1":1,"-":"-",
                          "His":"His","0":0,".":".","=":"="}
                          
    
    def create_button(self,row=5,column=4):
        '''Creates button in the window,button_dict contains name of each button and an arguement to be given to click function when pressed,no of rows in calculator and no. of columns'''
        self.__main_frame=tkinter.Frame(self)
        self.__main_frame.pack(fill='both')
        k=0
        for i in range(row):
            for r in range(column):
                
                try:
                    button=tkinter.Button(self.__main_frame,text=list(self._button_dict.keys())[k],command=partial(self.click,self._button_dict[list(self._button_dict.keys())[k]]),font='lucidia 20 bold')
                    button.grid(row=i,column=r,ipadx=15)
                    self._button_dict[list(self._button_dict.keys())[k]]=button
                    k+=1
                
                except Exception as e:
                    k+=1

                
        #    configuring each button
        self._button_dict['His'].grid(ipadx=1)
        self._button_dict['C'].grid(ipadx=13)
        self._button_dict['('].grid(ipadx=18)
        self._button_dict[')'].grid(ipadx=18)
        self._button_dict['.'].grid(ipadx=18)
        self._button_dict['+'].grid(ipadx=11)
        self._button_dict['='].grid(ipadx=12)
        self._button_dict[r'*'].grid(ipadx=14)

        
       
    def click(self,arg,*event):
        if arg=='C':
            '''If click on C clears the text area'''
            self.__store_value.set('')
            self.update()
        elif arg=='His':
            if os.path.exists(f"C:\\Users\\{getpass.getuser()}\\Calculator\\Log.txt"):
                self.__his=tkinter.Tk()
                self.__his.title('History')
                im=PhotoImage('History.ico')
                self.__his.iconbitmap(im)
                with open(f"C:\\Users\\{getpass.getuser()}\\Calculator\\Log.txt") as f:
                    for i in f.read().split('\n'):
                        if i=='':
                            pass
                        else:
                            tkinter.Label(self.__his,text=i,relief='solid').pack()
            else:
                self.__store_value.set("Error")
                self.update()
                
        
        elif arg=='=':
            if self.__store_value.get()=='':
                pass
            else:
        
                try:
                    l=self.__store_value.get()
                    self.__store_value.set(eval(self.__store_value.get()))
                    
                    if os.path.exists(f"C:\\Users\\{getpass.getuser()}\\Calculator\\Log.txt"):
                        with open(f'C:\\Users\\{getpass.getuser()}\\Calculator\\Log.txt',"a") as f:
                            f.write(f"{l}={eval(l)}\n")
                    else:
                        try:
                            os.mkdir(f'C:\\Users\\{getpass.getuser()}\\Calculator')
                        except Exception as e:
                            pass
                        with open(f'C:\\Users\\{getpass.getuser()}\\Calculator\\Log.txt',"a") as f:
                            f.write(f"{l}={eval(l)}\n")
                except Exception as e:
                    self.__store_value.set('Error')
                    self.update()
        else:
            if self.__store_value.get()=='Error':
                self.__store_value.set(arg)
                self.update()
            else:
                self.__store_value.set(f'{self.__store_value.get()}{arg}')
                self.update()
    def on_closing(self):
        try:
            os.remove(f'C:\\Users\\{getpass.getuser()}\\Calculator\\Log.txt')
                
        except Exception as e:
            pass
        self.destroy()
if __name__ == "__main__":
    app=Calculator()
    app.create_button()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()

    
