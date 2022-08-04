"""
Jonathan Knox
DTO2007Y2A V1
5/07/22
"""

from ast import Lambda
from sqlite3 import paramstyle
import tkinter as tk

from tkinter import X, ttk
from tkinter import messagebox
from turtle import width
from wsgiref import validate

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.title("DTO2007Y2A")
        self.geometry("500x350")
        self.resizable(False, False)
        mainframe = ttk.Frame(self)
        mainframe.pack(side="top", fill="none", expand=False)
        self.final_price = 0
        
        self.temp_dimensions = {"height":'',"width":'',"length":''}
        
        self.region_multiplier= {'North island':1,'South island':1.5,'Stewart island':2}
        self.region_var=tk.DoubleVar()
        
        self.base_rates = {0:8.00,6000:12.00,100000:15.00}
        
        self.customer_details = {'first name':'','last name':'','address':'','phone':''}
        self.frame_list = {Start_Page:'',Page_1:'',Page_2:'',Page_3:''}
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
        self.config(width=500, height=350)
        self.grid_propagate(False)
        self.rowconfigure(2, weight=1)
        self.parent = parent
        reg = self.register(self.callback)
        
        info_text="Welcome to the Onlinz Shopping returns application.\n\nIf your product is returned undamaged within 30 days, you will receive\na full refund of the purchase price.\n\nThis program will help you calculate the courier cost and collect \ninformation needed to return the product."
        
        title_frame = tk.Frame(self,width=500,height=70,background='#FFFFFF',relief='raised',borderwidth=2)
        title_frame.grid_propagate(0)
        title_frame.grid(row=0, column=0, columnspan=4, sticky="w")
        
        page_title = tk.Label(title_frame, text="Onlinz Shopping returns", font=("Helvetica", 14),justify="center")
        page_title.configure(background='#FFFFFF')
        page_title.grid(row=0, column=0,pady=20,padx=20)

        main_label = tk.Label(self, justify='left',text=info_text, font=("Helvetica", 12))
        main_label.grid(row=1, column=0, columnspan=4, sticky="w",padx=10,pady=10)     
        
        name_label = ttk.Label(self, text="First Name:")
        name_label.grid(row=2, column=0, sticky="ws",padx=10,pady=10)
        
        self.name_entry = ttk.Entry(self,validate='key', validatecommand=(reg,'%P'))
        self.name_entry.grid(row=2, column=1, sticky="sw",padx=10,pady=10)
        
        self.next_button = ttk.Button(self,text='Next',command=lambda:parent.switch_frame(Page_1),state='disabled')
        self.next_button.grid(column=3,row=2,padx=5,pady=5,sticky='se')
    def callback(self,value):
        parent = self.parent
        if value:
            parent.customer_details['first name'] = value
            self.next_button.configure(state='normal')
            return True  
        if value == '':
            parent.customer_details['first name'] = ''
            self.next_button.configure(state='disabled')
            return True

class Page_1(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        self.config(width=500, height=350)
        self.grid_propagate(False)
        self.rowconfigure(5, weight=1)
        
        self.parent = parent
         
        self.error_container = {"height":'',"width":'',"length":''}
        self.base_rates = parent.base_rates

        self.temp_dimensions = parent.temp_dimensions
        self.name = parent.customer_details['first name']
        
        title_frame = tk.Frame(self,width=500,height=70,background='#FFFFFF',relief='raised',borderwidth=2)
        title_frame.grid_propagate(0)
        title_frame.grid(row=0, column=0, columnspan=4, sticky="w")
        
        self.Page_greet = ttk.Label(title_frame, text='Hi,', font=("Helvetica", 12),justify='left',background='#FFFFFF')
        self.Page_greet.config(text=parent.customer_details['first name'])
        self.Page_greet.grid(row=0, column=0, columnspan=1, sticky="w",padx=15,pady=2.5)
        page_title = tk.Label(title_frame, text="Please enter the package dimensions and region:", font=("Helvetica", 14),background='#FFFFFF',justify='left')
        page_title.grid(row=1, column=0,padx=15,pady=2.5)
        
        self.final_price = parent.final_price
        
        self.region_multiplier = parent.region_multiplier
        self.region_var=parent.region_var
        
        reg=self.register(self.callback)

        
        dimension_title = ttk.LabelFrame(self, text="Measurements")
        dimension_title.grid(row=1, column=0, columnspan=2,rowspan=4, sticky="w",padx=10,pady=5)
        
        dimensions_label = ttk.Label(dimension_title, text="Enter the dimensions of the package in cm:")
        dimensions_label.grid(row=0, column=0, columnspan=2, sticky="w",padx=2.5,pady=5)
        
        self.entries = {"height":'',"width":'',"length":''}
        for i,fields, in enumerate(self.temp_dimensions):
            labs = ttk.Label(dimension_title,text=fields.title())
            self.ents = ttk.Entry(dimension_title)

            self.ents.config(validate='all', validatecommand=(reg, '%P','%V',fields))

            labs.grid(row=i+1,column=0,sticky='w',padx=5, pady=5)
            self.ents.grid(row=i+1,column=1,padx=5, pady=5)

            self.entries[fields] = self.ents
        
        for i,fields, in enumerate(self.error_container):
            self.error_container[fields] = ttk.Label(dimension_title,text='',foreground='red')
            self.error_container[fields].grid(row=5,column=0,sticky='w',padx=5, pady=5,columnspan=2)
        
        dropbox_title = ttk.Labelframe(self,text='Region')
        dropbox_title.grid(row=1,column=2,sticky='new',padx=2.5,pady=5,rowspan=2)
        dropbox_label = ttk.Label(dropbox_title,text='Select the region you are sending from:')
        dropbox_label.grid(row=0,column=0,sticky='w',padx=5,pady=5)
    
        self.dropbox = ttk.Combobox(dropbox_title,values=list(self.region_multiplier.keys()),state='readonly')
        self.dropbox.grid(row=1,column=0,sticky='ew',padx=15,pady=5)
        self.dropbox.bind('<<ComboboxSelected>>',self.confirm_next)
        
        price_title=ttk.LabelFrame(self,text='Price')
        price_title.grid(row=3,column=2,sticky='new',padx=2.5,pady=5,rowspan=2)
        
        price_label = ttk.Label(price_title,text='The price to return the package is:')
        price_label.grid(row=0,column=0,sticky='w',padx=5,pady=5)
        
        self.price_number = ttk.Label(price_title,text='$0.00',justify='center',font=('arial',11,'bold'))
        self.price_number.grid(row=1,column=0,padx=5,pady=5,rowspan=2)
        
        navigation_grid=ttk.Frame(self)
        navigation_grid.grid(row=5,column=2,sticky='se')
        
        self.next_button = ttk.Button(navigation_grid,text="Next",command=lambda:parent.switch_frame(Page_2),state='disabled')
        self.next_button.grid(row=0,column=1,padx=2, pady=5,sticky='se')
        
        back_button = ttk.Button(navigation_grid,text="Back",command=lambda:parent.switch_frame(Start_Page))
        back_button.grid(row=0,column=0,padx=2, pady=5,sticky='se')

        self.bind('<Expose>',lambda x:self.Page_greet.config(text=f"Hi, {parent.customer_details['first name']}"))
    def callback(self,value,reason,name):
        parent = self.parent
        try:
            value = float(value)
            if reason == 'focusout':
                if value < 5 or value > 100:
                    self.error_container[name].config(text='Please enter a value between 5 and 100')
                else:
                    self.error_container[name].config(text='')
            self.temp_dimensions[name] = value
            self.confirm_next()
            return True
        except:
            if value == '':
                self.temp_dimensions[name] = ''
                self.confirm_next()
                return True
            else:
                return False

    def update_price(self):
        try:
            multiplier=self.region_multiplier[self.dropbox.get()]
            volume = self.temp_dimensions['height']*self.temp_dimensions['width']*self.temp_dimensions['length']
            for i,vol in enumerate(self.base_rates):
                if volume > vol:
                    self.final_price = self.base_rates[vol]*multiplier
                    self.price_number.config(text=f'${self.final_price:.2f}')
        except:
            self.price_number.config(text='$0.00')

    def confirm_next(self,*args):
        values = [self.temp_dimensions['height'],self.temp_dimensions['width'],self.temp_dimensions['length']]
        region = self.dropbox.get()
        if all(values) == True and all(map(lambda x: float(x) >= 5 and float(x) <= 100,values)) == True and region:
            self.next_button.config(state='normal')
            self.update_price()
        else:
            self.next_button.config(state='disabled')
class Page_2(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        title_frame = tk.Frame(self,width=500,height=70,background='#FFFFFF',relief='raised',borderwidth=2)
        title_frame.grid_propagate(0)
        title_frame.grid(row=0, column=0, columnspan=4, sticky="w")
        
        self.Page_greet = ttk.Label(title_frame, text='Hi,', font=("Helvetica", 12),justify='left',background='#FFFFFF')
        self.Page_greet.config(text=parent.customer_details['first name'])
        self.Page_greet.grid(row=0, column=0, columnspan=1, sticky="w",padx=15,pady=2.5)
        page_title = tk.Label(title_frame, text="Please enter your details:", font=("Helvetica", 14),background='#FFFFFF',justify='left')
        page_title.grid(row=1, column=0,padx=15,pady=2.5)
        
        self.customer_details = parent.customer_details
        reg = self.register(self.callback)
        entries=[]
        for i,fields, in enumerate(self.customer_details):
            labs = ttk.Label(self,text=fields.title())
            ents = ttk.Entry(self)
            ents.config(validate="key", validatecommand=(reg, '%P',fields))
            labs.grid(row=i+1,column=0,padx=5,pady=5,sticky='w')
            ents.grid(row=i+1,column=1,padx=5,pady=5,sticky='w')
            entries.append(ents)
            
        next_button = ttk.Button(self,text="Next",command=lambda:parent.switch_frame(Page_3))
        next_button.grid(row=1,column=3,padx=5, pady=5,sticky='e')
        back_button = ttk.Button(self,text="back",command=lambda:parent.switch_frame(Page_1))
        back_button.grid(row=2,column=3,padx=5, pady=5,sticky='e')
        self.bind('<Expose>',lambda x:self.Page_greet.config(text=f"Hi, {parent.customer_details['first name']}"))
        self.bind('<Expose>',lambda x:entries[0].insert(0,parent.customer_details['first name']))
    def callback(self,value,name):
        self.customer_details[name] = value
        return True
        
class Page_3(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        title_frame = tk.Frame(self,width=500,height=70,background='#FFFFFF',relief='raised',borderwidth=2)
        title_frame.grid_propagate(0)
        title_frame.grid(row=0, column=0, columnspan=4, sticky="w")
        
        self.Page_greet = ttk.Label(title_frame, text='Hi,', font=("Helvetica", 12),justify='left',background='#FFFFFF')
        self.Page_greet.config(text=parent.customer_details['first name'])
        self.Page_greet.grid(row=0, column=0, columnspan=1, sticky="w",padx=15,pady=2.5)
        page_title = tk.Label(title_frame, text="Here are the return details:", font=("Helvetica", 14),background='#FFFFFF',justify='left')
        page_title.grid(row=1, column=0,padx=15,pady=2.5)
        
        self.customer_details = parent.customer_details
        
        text_frame = tk.Frame(self,width=490,height=200)
        text_frame.grid(row=2, column=0, columnspan=4, sticky="w")
        text_frame.grid_propagate(0)
        self.text = tk.Text(text_frame,width=400,height=40,relief='raised',borderwidth=2)
        self.text.grid(row=0,column=0,columnspan=4,rowspan=3,padx=5,pady=5,sticky='w')
        self.text.config(state='disabled')
        
        back_button = ttk.Button(self,text="back",command=lambda:parent.switch_frame(Page_2))
        back_button.grid(row=3,column=3,padx=5, pady=5,sticky='e')
        self.bind('<Expose>',lambda x:self.Page_greet.config(text=f"Hi, {parent.customer_details['first name']}"))
    
def main():
    app = App()
    app.mainloop()
    
if __name__ == "__main__":
    main()