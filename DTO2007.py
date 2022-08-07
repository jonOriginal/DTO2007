"""
Jonathan Knox
DTO2007Y2A V1
5/07/22
"""

import tkinter as tk

from tkinter import END, X, ttk
from tkinter import messagebox

class Details(dict):
    def __getitem__(self, key):
        return dict.__getitem__(self, key)
    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
    def __delitem__(self, key):
        dict.__setitem__(self, key, '')
    
class Access():
    def __init__(self):
        self.address = Details({'address':'','city':'','postcode':''})
        self.dimensions = Details({"height":'',"width":'',"length":''})
        self.customer = Details({'first name':'','last name':'','phone':''})

class Builder():
    def header(self, master,title,greet=True):
        frame = tk.Frame(master,width=500,height=70,background='#FFFFFF',relief='raised',borderwidth=2)
        frame.grid(row=0, column=0, sticky='ew',columnspan=4)
        frame.grid_propagate(0)
        
        title = ttk.Label(frame, text=title, font=("Helvetica", 18), background='#FFFFFF')
        title.grid(row=1, column=0, sticky='ew', pady=20, padx=20)
        
        if greet == True:
            greet = tk.Label(frame, text=a.customer['first name'], font=('Arial', 18), background='#FFFFFF')
            greet.grid(row=0, column=0, sticky='ew')
            title.grid(row=1, column=0, sticky='ew', pady=2.5, padx=20)
            return greet
        
        else:
            return frame
    

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.title("DTO2007Y2A")
        self.geometry("500x350")
        self.resizable(False, False)
        mainframe = ttk.Frame(self)
        mainframe.pack(side="top", fill="none", expand=False)
        self.final_price = 0

        
        self.region_multiplier= {'North island':1,'South island':1.5,'Stewart island':2}
        self.region_var=tk.DoubleVar()
        self.base_rates = {0:8.00,6000:12.00,100000:15.00}
        
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
        
        self.page_greet = b.header(self,'Onlinz Shopping returns',False)

        main_label = tk.Label(self, justify='left',text=info_text, font=("Helvetica", 12))
        main_label.grid(row=1, column=0, columnspan=4, sticky="w",padx=10,pady=10)     
        
        name_label = ttk.Label(self, text="First Name:")
        name_label.grid(row=2, column=0, sticky="ws",padx=10,pady=10)
        
        self.name_entry = ttk.Entry(self,validate='key', validatecommand=(reg,'%P'))
        self.name_entry.grid(row=2, column=1, sticky="sw",padx=10,pady=10)
        
        self.next_button = ttk.Button(self,text='Next',command=lambda:parent.switch_frame(Page_1),state='disabled')
        self.next_button.grid(column=3,row=2,padx=6,pady=5,sticky='se')
        
        self.name_entry.bind('<Return>', lambda event: self.next_button.invoke())
        
    def callback(self,value):
        if value:
            a.customer['first name'] = value.title()
            self.next_button.configure(state='normal')
            return True  
        if value == '':
            del a.customer['first name']
            self.next_button.configure(state='disabled')
            return True

class Page_1(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        self.config(width=500, height=350)
        self.grid_propagate(False)
        self.rowconfigure(5, weight=1)
        
        self.parent = parent
        self.base_rates = parent.base_rates
        
        self.page_greet = b.header(self,'Please enter the package dimensions and region:')
        
        self.final_price = parent.final_price
        self.region_multiplier = parent.region_multiplier
        self.region_var=parent.region_var
        
        reg=self.register(self.callback)

        
        dimension_title = ttk.LabelFrame(self, text="Measurements")
        dimension_title.grid(row=1, column=0, columnspan=2,rowspan=4, sticky="w",padx=10,pady=5)
        
        dimensions_label = ttk.Label(dimension_title, text="Enter the dimensions of the package in cm:")
        dimensions_label.grid(row=0, column=0, columnspan=2, sticky="w",padx=2.5,pady=5)
        
        self.entries = {"height":'',"width":'',"length":''}
        for i,fields, in enumerate(a.dimensions):
            labs = ttk.Label(dimension_title,text=fields.title())
            self.ents = ttk.Entry(dimension_title)

            self.ents.config(validate='all', validatecommand=(reg, '%P','%V',fields))

            labs.grid(row=i+1,column=0,sticky='w',padx=5, pady=5)
            self.ents.grid(row=i+1,column=1,padx=5, pady=5)

            self.entries[fields] = self.ents
        
        self.error_container = {'width':'','height':'','length':''}
        
        for i,fields, in enumerate(self.error_container):
            self.error_container[fields] = ttk.Label(dimension_title,text='',foreground='red',justify='center')
            self.error_container[fields].grid(row=5,column=0,sticky='',padx=5, pady=5,columnspan=2)
        
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

        self.bind('<Expose>',lambda x:self.page_greet.config(text=f"Hi, {a.customer['first name']}"))
        self.dropbox.bind('<Return>', lambda event: self.next_button.invoke())
    def callback(self,value,reason,name):
        try:
            value = float(value)
            if reason == 'focusout':
                if value < 5 or value > 100:
                    self.error_container[name].config(text='Please enter a value between 5 and 100')
                else:
                    self.error_container[name].config(text='')
            a.dimensions[name] = value
            self.confirm_next()
            return True
        except:
            if value == '':
                del a.dimensions[name]
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
                    self.parent.final_price = self.base_rates[vol]*multiplier
                    self.price_number.config(text=f'${self.parent.final_price:.2f}')
        except:
            self.price_number.config(text='$0.00')

    def confirm_next(self,*args):
        values = [a.dimensions['height'],a.dimensions['width'],a.dimensions['length']]
        region = self.dropbox.get()
        if all(values) == True and all(map(lambda x: float(x) >= 5 and float(x) <= 100,values)) == True and region:
            self.next_button.config(state='normal')
            self.update_price()
        else:
            self.next_button.config(state='disabled')
class Page_2(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        self.grid_propagate(0)
        self.rowconfigure(7, weight=1)
        
        title_frame = tk.Frame(self,width=500,height=70,background='#FFFFFF',relief='raised',borderwidth=2)
        title_frame.grid_propagate(0)
        title_frame.grid(row=0, column=0, columnspan=4, sticky="w")
        
        self.Page_greet = ttk.Label(title_frame, text='Hi,', font=("Helvetica", 12),justify='left',background='#FFFFFF')
        self.Page_greet.config(text=a.customer['first name'])
        self.Page_greet.grid(row=0, column=0, columnspan=1, sticky="w",padx=15,pady=2.5)
        page_title = tk.Label(title_frame, text="Please enter your details:", font=("Helvetica", 14),background='#FFFFFF',justify='left')
        page_title.grid(row=1, column=0,padx=15,pady=2.5)
        self.parent = parent
        reg = self.register(self.callback)
        
        detail_frame = ttk.LabelFrame(self, text="Personal Details")
        detail_frame.grid(row=1, column=0, columnspan=2,rowspan=4, sticky="w",padx=10,pady=5)
        
        detail_label = ttk.Label(detail_frame,text='These details will be used by the courier')
        detail_label.grid(row=0,column=0,padx=5,pady=2.5,sticky='w',columnspan=2)
        
        self.entries=[]
        for i,fields, in enumerate(a.customer):
            labs = ttk.Label(detail_frame,text=fields.title())
            ents = ttk.Entry(detail_frame)
            ents.config(validate="key", validatecommand=(reg, '%P',fields))
            labs.grid(row=i+1,column=0,padx=2.5,pady=2.5,sticky='w')
            ents.grid(row=i+1,column=1,padx=2.5,pady=2.5,sticky='w')
            self.entries.append(ents)
        
        address_frame = ttk.LabelFrame(self, text="Shipping Address")
        address_frame.grid(row=1, column=2, columnspan=2,rowspan=4, sticky="w",padx=10,pady=5)
        reg_a = self.register(self.callback_a)
        address_label = ttk.Label(address_frame,text='This is the address you are sending from')
        address_label.grid(row=0,column=0,padx=5,pady=2.5,sticky='w',columnspan=2)
        address=[]
        for i,fields, in enumerate(a.address):
            labs = ttk.Label(address_frame,text=fields.title())
            ents = ttk.Entry(address_frame)
            ents.config(validate="key", validatecommand=(reg_a, '%P',fields))
            labs.grid(row=i+1,column=0,padx=2.5,pady=2.5,sticky='w')
            ents.grid(row=i+1,column=1,padx=2.5,pady=2.5,sticky='w')
            address.append(ents)
        
        navigation_grid=ttk.Frame(self)
        navigation_grid.grid(row=7,column=3,sticky='se',padx=4)
        
        self.next_button = ttk.Button(navigation_grid,text="Next",command=lambda:parent.switch_frame(Page_3))
        self.next_button.grid(row=0,column=1,padx=2, pady=5,sticky='se')
        back_button = ttk.Button(navigation_grid,text="Back",command=lambda:parent.switch_frame(Page_1))
        back_button.grid(row=0,column=0,padx=2, pady=5,sticky='se')
        
        self.bind('<Expose>',lambda x:self.update_widgets())
    def callback(self,value,name):
        if value != '':
            a.customer[name] = value.title()
        self.confirm_next()
        return True
    
    def callback_a(self,value,name):
        a.address[name] = value.title()
        self.confirm_next()
        return True
    
    def confirm_next(self):
        values = [a.customer['first name'],a.customer['last name'],a.customer['phone'],a.address['address'],a.address['city'],a.address['postcode']]
        if all(values) == True:
            self.next_button.config(state='normal')
        else:
            self.next_button.config(state='disabled')
    
    def update_widgets(self):
        self.Page_greet.config(text=f"Hi, {a.customer['first name']}")
        self.entries[0].delete(0,END)
        self.entries[0].insert(0,a.customer['first name'])
        
class Page_3(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        self.grid_propagate(0)
        self.rowconfigure(3, weight=1)
        self.parent = parent
        title_frame = tk.Frame(self,width=500,height=70,background='#FFFFFF',relief='raised',borderwidth=2)
        title_frame.grid_propagate(0)
        title_frame.grid(row=0, column=0, columnspan=4, sticky="w")
        
        self.Page_greet = ttk.Label(title_frame, text='Hi,', font=("Helvetica", 12),justify='left',background='#FFFFFF')
        self.Page_greet.config(text=a.customer['first name'])
        self.Page_greet.grid(row=0, column=0, columnspan=1, sticky="w",padx=15,pady=2.5)
        page_title = tk.Label(title_frame, text="Here are the return details:", font=("Helvetica", 14),background='#FFFFFF',justify='left')
        page_title.grid(row=1, column=0,padx=15,pady=2.5)
        
        
        text_frame = tk.Frame(self,width=490,height=200)
        text_frame.grid(row=2, column=0, columnspan=4, sticky="w")
        text_frame.grid_propagate(0)
        self.text = tk.Text(text_frame,width=400,height=40,relief='raised',borderwidth=2,font=("Arial",10))
        self.text.grid(row=0,column=0,columnspan=4,rowspan=3,padx=10,pady=10,sticky='w')
        self.text.config(state='disabled')
        
        navigation_grid=ttk.Frame(self)
        navigation_grid.grid(row=7,column=3,sticky='se',padx=4)
        
        back_button = ttk.Button(navigation_grid,text="Back",command=lambda:parent.switch_frame(Page_2))
        back_button.grid(row=3,column=0,padx=2, pady=5,sticky='se')
        
        finish_button = ttk.Button(navigation_grid,text="Finish",command=lambda:exit())
        finish_button.grid(row=3,column=1,padx=2, pady=5,sticky='se')
        self.bind('<Expose>',lambda x:self.update_widgets())
        
    def update_widgets(self):
        self.Page_greet.config(text=f"Hi, {a.customer['first name']}")
        self.text.config(state='normal')
        self.text.delete(1.0,'end')
        for i,field in enumerate(a.customer):
            self.text.insert(tk.END,f"{field.title()}: {a.customer[field]}\n")
        for i,field in enumerate(a.address):
            self.text.insert(tk.END,f"{field.title()}: {a.address[field]}\n")
        self.text.insert(tk.END,f"Price: ${self.parent.final_price:.2f}")
        self.text.config(state='disabled')

def main():
    global a
    global b
    b = Builder()
    a = Access()
    app = App()
    app.mainloop()
    
if __name__ == "__main__":
    main()