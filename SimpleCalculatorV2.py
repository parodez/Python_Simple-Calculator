from tkinter import *

class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()
    
    def init_window(self):
        self.master.title('Simple Calculator')

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
        
        button_frame = Frame(self)
        button_frame.grid(row=2,
                          columnspan=3)

        add_button = Button(button_frame,
                            text='+',
                            width=7,
                            command=self.getSum)
        add_button.grid(row=0,
                        column=1,
                        pady=3)
        subtract_button = Button(button_frame,
                             text='-',
                             width=7,
                             command=self.getDifference)
        subtract_button.grid(row=0,
                         column=2,
                         pady=3)
        
        multiply_button = Button(button_frame,
                                 text='*',
                                 width=7,
                                 command=self.getProduct)
        multiply_button.grid(row=0,
                             column=3,
                             pady=3)
        
        divide_button = Button(button_frame,
                               text='/',
                               width=7,
                               command=self.getQuotient)
        divide_button.grid(row=0,
                           column=4,
                           pady=3)
        
        self.result_label = Label(self,
                                  relief=RIDGE,
                                  width=30)
        self.result_label.grid(row=3,
                               column=0,
                               columnspan=3)
        
        self.pack()

    def getNumbers(self):
        self.firstNum = self.firstNum_entry.get()
        self.secondNum = self.secondNum_entry.get()

    def getSum(self):
        self.getNumbers()

        sum = int(self.firstNum) + int(self.secondNum)

        self.result_label.config(text=f'Sum: {sum}')

    def getDifference(self):
        self.getNumbers()

        difference = int(self.firstNum) - int(self.secondNum)

        self.result_label.config(text=f'Difference: {difference}')

    def getProduct(self):
        self.getNumbers()

        product = int(self.firstNum) * int(self.secondNum)

        self.result_label.config(text=f'Product: {product}')

    def getQuotient(self):
        self.getNumbers()

        quotient = int(self.firstNum) / int(self.secondNum)

        self.result_label.config(text=f'Quotient: {quotient}')

root = Tk()
root.geometry('300x120')
app = Window(root)
root.mainloop()