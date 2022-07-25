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
from tkinter import messagebox

def callback(input):
    try:
        float(input)
        return True
    except:
        if input == '':
            return True
        else:
            return False

def calculate():
    print(temp_dimensions['height'].get())
    if temp_dimensions['height'].get() == '' or temp_dimensions['width'].get() == '' or temp_dimensions['length'].get() == '':
        messagebox.showerror('Python Error', 'Error: This is an Error Message!')
    else:
        volume = float(temp_dimensions['height'].get())* float(temp_dimensions['width'].get()) * float(temp_dimensions['length'].get())
        total = Label(root,textvariable=float(temp_dimensions['height'].get())* float(temp_dimensions['width'].get()) * float(temp_dimensions['length'].get()))
        total.grid(column=2,row =0)
        root.mainloop()
   
def main():
    root.title("Onlinz")
    root.geometry('400x400')
    reg=root.register(callback)

    for i,fields, in enumerate(temp_dimensions):
        labs = ttk.Label(root,text=fields)
        ents = ttk.Entry(root)
        ents.config(validate="key", validatecommand=(reg, '%P'),textvariable=temp_dimensions[fields])
        labs.grid(row=i,column=0)
        ents.grid(row=i,column=1)
        temp_dimensions[fields] = ents

    confirm = ttk.Button(root,text='confirm',command=calculate)
    confirm.grid(column=0,row=4)

    root.mainloop()

if __name__ == "__main__":
    main()