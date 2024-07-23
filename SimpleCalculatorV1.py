from tkinter import *

class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()
    
    def init_window(self):
        self.master.title('GUI')

        firstNum_label = Label(self,
                               text='First Number: ')
        firstNum_label.grid(row=0,
                            column=0,
                            pady=3)
        self.firstNum_entry = Entry(self,
                               width=20)
        self.firstNum_entry.grid(row=0,
                            column=1,
                            columnspan=2)
        secondNum_label = Label(self,
                                text='Second Number: ')
        secondNum_label.grid(row=1,
                             column=0,
                             pady=3)
        self.secondNum_entry = Entry(self,
                                width=20)
        self.secondNum_entry.grid(row=1,
                             column=1,
                             columnspan=2)

        add_button = Button(self,
                            text='ADD',
                            width=7,
                            command=self.getSum)
        add_button.grid(row=2,
                        column=1,
                        pady=3)
        quit_button = Button(self,
                             text='QUIT',
                             width=7,
                             command=self.client_exit)
        quit_button.grid(row=2,
                         column=2)
        
        self.result_label = Label(self,
                                  relief=RIDGE,
                                  width=30)
        self.result_label.grid(row=3,
                               column=0,
                               columnspan=3)
        
        self.pack()

    def client_exit(self):
        exit()

    def getSum(self):
        firstNum = self.firstNum_entry.get()
        secNum = self.secondNum_entry.get()

        sum = int(firstNum) + int(secNum)

        self.result_label.config(text=f'The answer is {sum}')

root = Tk()
root.geometry('300x120')
app = Window(root)
root.mainloop()