"""
Jonathan Knox
DTO2007Y2A V1
5/07/22
"""

import tkinter as tk
from tkinter import X, ttk
from tkinter import messagebox
from turtle import width

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.title("DTO2007Y2A")
        self.geometry("500x300")
        self.resizable(False, False)
        mainframe = ttk.Frame(self)
        mainframe.pack(side="top", fill="both", expand=False)
        
        self.temp_dimensions = {"height":'',"width":'',"length":''}
        
        self.region_multiplier= {'north island':1,'south island':1.5,'stewart island':2}
        self.region_var=tk.DoubleVar()
        
        self.base_rates = {0:8.00,6000:12.00,100000:15.00}
        
        self.customer_details = {'first name':'','last name':'','address':'','phone':''}

        self.frame_list = {Start_Page:'',Page_1:'',Page_2:''}
        for i, frame_name in enumerate(self.frame_list):
            frame = frame_name(self,mainframe)
            self.frame_list[frame_name] = frame
            frame.grid(row=0, column=0, sticky="nsew",)
        self.switch_frame(Start_Page)
    
    def switch_frame(self, page_name):
        self.frame_list[page_name].tkraise()
    
class Start_Page(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        self.rowconfigure(7, weight=5)
        page_title = tk.Label(self, text="Please select the region you are sending from", font=("Helvetica", 14))
        page_title.configure(background='#FFFFFF',width=45,height=3,relief='raised',borderwidth=2)
        page_title.grid(row=0, column=0, columnspan=4, sticky="w")
        
        self.region_multiplier = parent.region_multiplier
        self.region_var=parent.region_var
        
        for i, radios in enumerate(self.region_multiplier):
            self.rad = ttk.Radiobutton(self,text=radios,value=self.region_multiplier[radios],variable=self.region_var)
            self.rad.grid(column=0,row=i+1,padx=10,pady=5,sticky='w')
        
        next_button = ttk.Button(self,text='next',command=lambda:self.confirm_next(parent))
        next_button.grid(column=3,row=1,padx=5,pady=5,sticky='e')
        
    def confirm_next(self,parent):
        print(self.region_var.get())
        if self.region_var.get() == 0:
            messagebox.showerror('Empty Fields', 'Please Fill all fields')
        else:
            parent.switch_frame(Page_1)
class Page_1(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        self.temp_dimensions = parent.temp_dimensions
        self.error_container = {"height":'',"width":'',"length":''}
        self.base_rates = parent.base_rates

        page_title = tk.Label(self, text="Please Enter the package dimesions:", font=("Helvetica", 14))
        page_title.configure(background='#FFFFFF',width=45,height=3,relief='raised',borderwidth=2)
        page_title.grid(row=0, column=0, columnspan=4, sticky="w")
        
        self.region_var=parent.region_var
        reg=self.register(self.callback)
    
        for i,fields, in enumerate(self.temp_dimensions):
            labs = ttk.Label(self,text=fields+' (cm)',)
            self.ents = ttk.Entry(self)
            errs = ttk.Label(self,text='',foreground='red')

            self.ents.config(validate='all', validatecommand=(reg, '%P','%V',fields),textvariable=self.temp_dimensions[fields])

            errs.grid(row=i+1,column=1,sticky='w',padx=5,pady=5)
            labs.grid(row=i+1,column=0,padx=5, pady=5)
            self.ents.grid(row=i+1,column=1,padx=5, pady=5)

            self.error_container[fields] = errs
            self.temp_dimensions[fields] = self.ents
        
        self.price_label = ttk.Label(self,text='$')
        self.price_label.grid(row=2,column=2)
        
        self.check_button = ttk.Button(self,text="Check",command=lambda:self.check_volume())
        self.check_button.grid(row=1,column=2,padx=5, pady=5)
        
        self.next_button = ttk.Button(self,text="Next",command=lambda:parent.switch_frame(Page_2),state='disabled')
        self.next_button.grid(row=1,column=3,padx=5, pady=5,sticky='e')
        
        back_button = ttk.Button(self,text="back",command=lambda:parent.switch_frame(Start_Page))
        back_button.grid(row=2,column=3,padx=5, pady=5,sticky='e')

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
                self.check_volume()
            return True
        except:
            if value == '':
                return True
            else:
                return False
        
    def check_volume(self):
        multiplier=float(self.region_var.get())
        self.confirm_next()
        try:
            volume = float(self.temp_dimensions['height'].get()) * float(self.temp_dimensions['width'].get()) * float(self.temp_dimensions['length'].get())
            for i,vol in enumerate(self.base_rates):
                if volume > vol:
                    self.price_label.config(text=f'{self.base_rates[vol]*multiplier}$')
                    
        except:
            pass
    def confirm_next(self):
        values = [self.temp_dimensions['height'].get(),self.temp_dimensions['width'].get(),self.temp_dimensions['length'].get()]
        if all(values) == True and all(map(lambda x: float(x) >= 5 and float(x) <= 100,values)) == True:
            self.next_button.config(state='normal')

class Page_2(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        page_title = tk.Label(self, text="Please enter your details:", font=("Helvetica", 14))
        page_title.configure(background='#FFFFFF',width=45,height=3,relief='raised',borderwidth=2)
        page_title.grid(row=0, column=0, columnspan=4, sticky="w")
        
        self.customer_details = parent.customer_details
        for i,fields, in enumerate(self.customer_details):
            labs = ttk.Label(self,text=fields)
            ents = ttk.Entry(self)
            ents.config(validate="key",textvariable=self.customer_details[fields])
            labs.grid(row=i+1,column=0,padx=5,pady=5,sticky='w')
            ents.grid(row=i+1,column=1,padx=5,pady=5,sticky='w')
            self.customer_details[fields] = ents
            
        next_button = ttk.Button(self,text="Next",command=lambda:self.confirm_next(parent))
        next_button.grid(row=1,column=3,padx=5, pady=5,sticky='e')
        back_button = ttk.Button(self,text="back",command=lambda:parent.switch_frame(Page_1))
        back_button.grid(row=2,column=3,padx=5, pady=5,sticky='e')
    
    def confirm_next(self,parent):
        values = [self.customer_details['first name'].get(),self.customer_details['last name'].get(),self.customer_details['address'].get(),self.customer_details['phone'].get()]
        if all(values) == False:
            messagebox.showerror('Empty Fields', 'Please Fill all fields')
        else:
            parent.switch_frame(Page_1)
        
def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()