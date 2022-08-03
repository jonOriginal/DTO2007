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
        self.geometry("500x320")
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
        self.rowconfigure(2, weight=1)
        
        reg = self.register(self.callback)
        
        info_text="Welcome to the Onlinz Shopping returns application.\n\nIf your product is returned undamaged within 30 days, you will receive\na full refund of the purchase price.\n\nThis program will help you calculate the courier cost and collect \ninformation needed to return the product."
        
        self.customer_details = parent.customer_details
        
        page_title = tk.Label(self, text="Onlinz Shopping returns", font=("Helvetica", 14))
        page_title.configure(background='#FFFFFF',width=45,height=3,relief='raised',borderwidth=2)
        page_title.grid(row=0, column=0, columnspan=4, sticky="w")

        main_label = tk.Label(self, justify='left',text=info_text, font=("Helvetica", 12))
        main_label.grid(row=1, column=0, columnspan=4, sticky="w",padx=10,pady=10)     
        
        name_label = ttk.Label(self, text="Name:")
        name_label.grid(row=2, column=0, sticky="ws",padx=10,pady=10)
        
        self.name_entry = ttk.Entry(self,validate='key', validatecommand=(reg,'%P'))
        self.name_entry.grid(row=2, column=1, sticky="sw",padx=10,pady=10)
        
        self.next_button = ttk.Button(self,text='Next',command=lambda:parent.switch_frame(Page_1),state='disabled')
        self.next_button.grid(column=3,row=2,padx=5,pady=5,sticky='se')

    def callback(self,value):
        if value:
            self.customer_details['first name'] = value
            self.next_button.configure(state='normal')
            return True  
        if value == '':
            self.next_button.configure(state='disabled')
            return True

class Page_1(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        self.config(width=500, height=350)
        self.grid_size = (3,4)
        
        self.error_container = {"height":'',"width":'',"length":''}
        self.base_rates = parent.base_rates
        self.temp_dimensions = parent.temp_dimensions
        
        page_title = tk.Label(self, text="Please enter the package dimesions and region", font=("Helvetica", 14))
        page_title.configure(background='#FFFFFF',width=45,height=3,relief='raised',borderwidth=2)
        page_title.grid(row=0, column=0, columnspan=4, sticky="w")
        
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
        self.next_button.grid(row=2,column=3,padx=2, pady=5,sticky='se')
        
        back_button = ttk.Button(navigation_grid,text="Back",command=lambda:parent.switch_frame(Start_Page))
        back_button.grid(row=1,column=3,padx=2, pady=5,sticky='se')

    def callback(self,value,reason,name):
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
            Page_3.update_listbox(Page_3)
            parent.switch_frame(Page_3)

class Page_3(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        page_title = tk.Label(self, text="Details:", font=("Helvetica", 14))
        page_title.configure(background='#FFFFFF',width=45,height=3,relief='raised',borderwidth=2)
        page_title.grid(row=0, column=0, columnspan=4, sticky="w")
        
        Page_3.customer_details = parent.customer_details
        
        Page_3.detail_box = tk.Listbox(self,height=10,width=50)
        Page_3.detail_box.grid(row=1,column=0,columnspan=4,padx=5,pady=5,sticky='w') 
        
        back_button = ttk.Button(self,text="back",command=lambda:parent.switch_frame(Page_2))
        back_button.grid(row=2,column=3,padx=5, pady=5,sticky='e')
        
    def update_listbox(self):
        for i,detail in enumerate(self.customer_details):
            self.detail_box.insert(i,f'{detail}: {self.customer_details[detail].get().title()}')
        self.detail_box.insert(i+1,f'{App.final_price}$')
    
def main():
    app = App()
    app.mainloop()
    
if __name__ == "__main__":
    main()