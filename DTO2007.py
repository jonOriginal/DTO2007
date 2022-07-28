"""
Jonathan Knox
DTO2007Y2A V1
5/07/22
"""

import tkinter as tk
from tkinter import ttk

from tkinter import messagebox
from tkinter.tix import *

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.title("DTO2007Y2A")
        self.geometry("500x500")
        mainframe = ttk.Frame(self)
        mainframe.pack(side="top", fill="both", expand=False)
        
        self.temp_dimensions = {"height":'',"width":'',"length":''}
        self.region_multiplier= {'north island':1,'south island':1.5,'stewart island':2}
        self.customer_details = {'first name':'','last name':'','address':'','phone':''}

        self.frame_list = {StartPage:'',Page_2:'',Page_3:''}
        for i, frame_name in enumerate(self.frame_list):
            frame = frame_name(self,mainframe)
            self.frame_list[frame_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.switch_frame(StartPage)
    
    def switch_frame(self, page_name):
        self.frame_list[page_name].tkraise()
    

class StartPage(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        self.temp_dimensions = parent.temp_dimensions
        self.error_container = {"height":'',"width":'',"length":''}
        
        reg=self.register(self.callback)
    
        for i,fields, in enumerate(self.temp_dimensions):
            labs = ttk.Label(self,text=fields,)
            self.ents = ttk.Entry(self)
            errs = ttk.Label(self,text='',foreground='red')

            self.ents.config(validate='all', validatecommand=(reg, '%P','%V',fields),textvariable=self.temp_dimensions[fields])

            errs.grid(row=i,column=2,sticky='w',padx=5,pady=5)
            labs.grid(row=i,column=0,padx=5, pady=5)
            self.ents.grid(row=i,column=1,padx=5, pady=5)

            self.error_container[fields] = errs
            self.temp_dimensions[fields] = self.ents
            
        self.error_label = ttk.Label(self,text='')
        self.error_label.grid(row=i+2,column=0)
        
        next_button = ttk.Button(self,text="Next",command=lambda:self.confirm_next(parent))
        next_button.grid(row=i+1,column=0,padx=5, pady=5)

    def callback(self,value,reason,name):
        try:
            float(value)
            if reason == 'focusout':
                if float(value) < 5 or float(value) > 100:
                    self.temp_dimensions[name].config(foreground='red')
                    self.error_container[name].config(text='Please enter a value between 5 and 100')
                else:
                    self.temp_dimensions[name].config(foreground='black')
                    self.error_container[name].config(text='')
            return True
        except:
            if value == '':
                return True
            else:
                return False
        
    def confirm_next(self,parent):
        values = [self.temp_dimensions['height'].get(),self.temp_dimensions['width'].get(),self.temp_dimensions['length'].get()]
        if all(values) == False:
            messagebox.showerror('Empty Fields', 'Please Fill all fields')
        elif all(map(lambda x: float(x) > 5 and float(x) < 100,values)) == False:
            messagebox.showerror('Invalid Fields', 'Please enter a value between 5 and 100')
        else:
            parent.switch_frame(Page_2)

class Page_2(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        self.region_multiplier = parent.region_multiplier
        self.region_var=tk.StringVar()
        
        for i, radios in enumerate(self.region_multiplier):
            self.rad = ttk.Radiobutton(self,text=radios,value=self.region_multiplier[radios],variable=self.region_var)
            self.rad.grid(column=0,row=i,padx=5,pady=5,sticky='w')
        region_confirm = ttk.Button(self,text='confirm',command=lambda:self.confirm_next(parent))
        region_confirm.grid(column=0,row=i+1,padx=5,pady=5,sticky='w')
        
    def confirm_next(self,parent):
        if self.region_var.get() == '':
            messagebox.showerror('Empty Fields', 'Please Fill all fields')
        else:
            parent.switch_frame(Page_3)
        
class Page_3(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        customer_details = parent.customer_details
        for i,fields, in enumerate(customer_details):
            labs = ttk.Label(self,text=fields)
            ents = ttk.Entry(self)
            ents.config(validate="key",textvariable=customer_details[fields])
            labs.grid(row=i,column=0)
            ents.grid(row=i,column=1)
            customer_details[fields] = ents

        
def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()