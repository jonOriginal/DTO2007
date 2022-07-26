"""
Jonathan Knox
DTO2007Y2A V1
5/07/22
"""
from cProfile import label
from tkinter import *
from tkinter import ttk
root = Tk()
temp_dimensions = {"height":'',"width":'',"length":''}
region_multiplier= {'north island':1,'south island':1.5,'stewart island':2}
customer_details = {'first name':'','last name':'','address':'','phone':''}
from tkinter import messagebox

class app(Tk):
    def __init__(self,x=0):
        self.x = x
    
    def greet(self):
        print(self.x)
        
def callback(input):
    try:
        float(input)
        return True
    except:
        if input == '':
            return True
        else:
            return False

def clearFrame():
    # destroy all widgets from frame
    for widget in root.winfo_children():
       widget.destroy()
    return

def calculate():
    if temp_dimensions['height'].get() == '' or temp_dimensions['width'].get() == '' or temp_dimensions['length'].get() == '':
        messagebox.showerror('Python Error', 'Error: This is an Error Message!')
    else:
        total = Label(root,textvariable=float(temp_dimensions['height'].get())* float(temp_dimensions['width'].get()) * float(temp_dimensions['length'].get()))
        total.grid(column=3,row =0)
        global volume_label
        volume_label.config(text=total.cget('textvariable'))
        clearFrame()
        region_select()
        
def region_select():
    
    region_var=StringVar()
    for i, radios in enumerate(region_multiplier):
        rad = ttk.Radiobutton(root,text=radios,value=region_multiplier[radios],variable=region_var)
        rad.grid(column=0,row=i)
    region_confirm = ttk.Button(root,text='confirm',command=get_customer_details)
    region_confirm.grid(column=0,row=i+1)
    
def get_customer_details():
    reg=root.register(callback)
    for i,fields, in enumerate(customer_details):
        labs = ttk.Label(root,text=fields)
        ents = ttk.Entry(root)
        ents.config(validate="key",textvariable=customer_details[fields])
        labs.grid(row=i,column=0)
        ents.grid(row=i,column=1)
        customer_details[fields] = ents

def get_dimensions():
    reg=root.register(callback)
    for i,fields, in enumerate(temp_dimensions):
        labs = ttk.Label(root,text=fields)
        ents = ttk.Entry(root)
        ents.config(validate="key", validatecommand=(reg, '%P'),textvariable=temp_dimensions[fields])
        labs.grid(row=i,column=0)
        ents.grid(row=i,column=1)
        temp_dimensions[fields] = ents

    confirm_button = ttk.Button(root,text='confirm',command=calculate)
    confirm_button.grid(column=0,row=4)
def main():
    app(5).greet()
    root.title("Onlinz")
    root.geometry('400x400')
    root.mainloop()
    get_dimensions()

if __name__ == "__main__":
    main()