"""
Jonathan Knox
DTO2007Y2A V1
5/07/22
"""

import tkinter as tk

from tkinter import END, X, ttk
from tkinter import messagebox

class Details(dict):
    def __getitem__(self, key) -> str:
        return dict.__getitem__(self, key)
    def __setitem__(self, key, value) -> None:
        dict.__setitem__(self, key, value)
    def __delitem__(self, key) -> None:
        dict.__setitem__(self, key, '')
    
class Access():
    def __init__(self):
        self.address = Details({'address':'','city':'','postcode':''})
        self.dimensions = Details({"height":'',"width":'',"length":''})
        self.customer = Details({'first name':'','last name':'','phone':''})
        self.region_multiplier= {'North island':1,'South island':1.5,'Stewart island':2}
        self.rates = {0:8.00,6000:12.00,100000:15.00}
        self.price = 0
        
class Builder():
    @staticmethod
    def header(master,title,greet=True) -> tk.Label:
        frame = tk.Frame(master,width=500,height=70,background='#FFFFFF',relief='raised',borderwidth=2)
        frame.grid(row=0, column=0, sticky='ew',columnspan=4)
        frame.grid_propagate(0)
        
        title = ttk.Label(frame, text=title, font=("Helvetica", 14), background='#FFFFFF')
        title.grid(row=1, column=0, sticky='ew', pady=20, padx=20)
        
        if greet == True:
            greet = tk.Label(frame, text=a.customer['first name'], font=('Arial', 12), background='#FFFFFF',justify='left')
            greet.grid(row=0, column=0,sticky='w',padx=15,pady=2.5)
            title.grid(row=1, column=0, sticky='ew', pady=2.5, padx=15)
            return greet
        
        else:
            return frame
    @staticmethod
    def nav(master,parent,current,back=True,next=True,finish=False) -> tk.Button:
        
        frame = tk.Frame(master)
        frame.grid(row=6, column=3, sticky='se',columnspan=2)
        
        next_button = ttk.Button(frame, text='Next', command=lambda: parent.next(current),state='disabled')
        back_button = ttk.Button(frame, text='Back', command=lambda: parent.back(current))
        finish_button = ttk.Button(frame, text='Finish', command=lambda: exit())
        
        if next:
            next_button.grid(row=0, column=1, sticky='se', pady=5, padx=2.5)
        if back:
            back_button.grid(row=0, column=0, sticky='se', pady=5, padx=2.5)
        if finish:
            finish_button.grid(row=0, column=1, sticky='se', pady=5, padx=2.5)
        
        return next_button
    
    @staticmethod
    def entry(master,Label,row,column,validatecommand,validate = 'key',width=15) -> tk.Entry:
        frame = tk.Frame(master)
        frame.grid(row=row, column=column, sticky='ew',columnspan=1)
        label = ttk.Label(frame, text=Label,width=width)
        label.grid(row=0, column=0, sticky='w', pady=5, padx=5)
        entry = ttk.Entry(frame,validate=validate,validatecommand=validatecommand)
        entry.grid(row=0, column=1, sticky='w', pady=5, padx=5)
        return entry
    
    @staticmethod
    def lframe(master,lable,text,row,column,columnspan=2,rowspan=4) -> tk.LabelFrame:
        frame = ttk.LabelFrame(master,text=lable)
        frame.grid(row=row, column=column, sticky='ew',columnspan=columnspan,padx=5,pady=5,rowspan=rowspan)
        label = ttk.Label(frame, text=text)
        label.grid(row=0, column=0, sticky='w', pady=5, padx=5)
        return frame
    
    @staticmethod
    def label(master,text,row,column,font=(),columnspan=1,rowspan=1,foreground='black',justify = 'left',sticky = 'ew') -> tk.Label:
        label = ttk.Label(master,text=text,font=font,foreground=foreground,justify=justify)
        label.grid(row=row, column=column, sticky=sticky,columnspan=columnspan,padx=5,pady=5,rowspan=rowspan)
        return label
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.title("DTO2007Y2A")
        self.geometry("500x350")
        self.resizable(False, False)
        mainframe = ttk.Frame(self)
        mainframe.pack(side="top", fill="none", expand=False)
        
        self.frame_list = {Start_Page:'',Page_1:'',Page_2:'',Page_3:''}
        for i, frame_name in enumerate(self.frame_list):
            frame = frame_name(self,mainframe)
            frame.config(width=500,height=350)
            self.frame_list[frame_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.grid_propagate(False)
    
        self.frame_list[Start_Page].tkraise()
    
    def next(self,current):
        i = list(self.frame_list.keys()).index(current)+1
        name = list(self.frame_list.keys())[i]
        self.frame_list[name].tkraise()   
        
    def back(self,current):
        i = list(self.frame_list.keys()).index(current)-1
        name = list(self.frame_list.keys())[i]
        self.frame_list[name].tkraise()
        
class Start_Page(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        self.rowconfigure(2, weight=1)
        reg = self.register(self.callback)
        info_text="Welcome to the Onlinz Shopping returns application.\n\nIf your product is returned undamaged within 30 days, you will receive\na full refund of the purchase price.\n\nThis program will help you calculate the courier cost and collect \ninformation needed to return the product."
        
        self.page_greet = b.header(self,'Onlinz Shopping returns',False)

        b.label(self,info_text,1,0,font=('Arial', 12),justify='left',columnspan=4) 
        
        name_entry = b.entry(self,'First Name:',6,0,validatecommand=(reg,'%P'))
        name_entry.focus()
        self.next_button = b.nav(self,parent,__class__,back=False)
        name_entry.bind('<Return>', lambda event: self.next_button.invoke())
        
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
        self.rowconfigure(5, weight=1)
        
        self.page_greet = b.header(self,'Please enter the package dimensions and region:')
        
        reg = self.register(self.callback)
        
        measurements = b.lframe(self,'Measurements','Enter the dimensions of the package in cm:',1,0)
        
        self.entries = {"height":'',"width":'',"length":''}
        for i,fields, in enumerate(a.dimensions):
            ents = b.entry(measurements,fields.title(),i+1,0,validate='all',validatecommand=(reg, '%P','%V',fields),width=14)
            self.entries[fields] = ents
        
        self.error_container = {'width':'','height':'','length':''}
        for i,fields, in enumerate(self.error_container):
            self.error_container[fields] = b.label(measurements,'',4,0,justify='center',columnspan=2,foreground='red',sticky=None)
            
        region = b.lframe(self,'Region','Select the region you are sending from:',1,2,rowspan=2)
    
        self.dropbox = ttk.Combobox(region,values=list(a.region_multiplier.keys()),state='readonly')
        self.dropbox.grid(row=1,column=0,sticky='ew',padx=15,pady=5)
        
        estimate = b.lframe(self,'Price','The shipping cost to return the product:',3,2,rowspan=2)
        self.price_number = b.label(estimate,'',1,0,justify='center',columnspan=2,font=('Arial', 11, 'bold'),rowspan=2,sticky=None)
        
        self.next_button = b.nav(self,parent,__class__)
        
        self.dropbox.bind('<<ComboboxSelected>>',self.confirm_next)
        self.bind('<Expose>',lambda x:self.page_greet.config(text=f"Hi, {a.customer['first name']}"))
        self.dropbox.bind('<Return>', lambda event: self.next_button.invoke())
    def callback(self,value,reason,name):
        try:
            value = float(value)
            if reason == 'focusout':
                if value < 5 or value > 100:
                    self.error_container[name].config(text='Please enter a value  between 5 and 100.')
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
            multiplier=a.region_multiplier[self.dropbox.get()]
            volume = a.dimensions['height']*a.dimensions['width']*a.dimensions['length']
            for i,vol in enumerate(a.rates):
                if volume > vol:
                    a.price = a.rates[vol]*multiplier
                    self.price_number.config(text=f'${a.price:.2f}')
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
        self.rowconfigure(5, weight=1)
        
        self.page_greet = b.header(self,'Please enter your details:')
        reg = self.register(self.callback)
        reg_a = self.register(self.callback_a)
        details = b.lframe(self,'Personal Details','These details will be used by the courier:',1,0)
        
        self.entries=[]
        for i,fields, in enumerate(a.customer):
            ents = b.entry(details,fields.title(),i+1,0,validate='key',validatecommand=(reg, '%P',fields))
            self.entries.append(ents)
        
        addresses = b.lframe(self,'Address','Enter the address you are sending from:',1,2)
        
        address=[]
        for i,fields, in enumerate(a.address):
            ents  = b.entry(addresses,fields.title(),i+1,0,validate='key',validatecommand=(reg_a, '%P',fields),width=13)
            address.append(ents)
        
        self.next_button = b.nav(self,parent,__class__)
        
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
        self.page_greet.config(text=f"Hi, {a.customer['first name']}")
        self.entries[0].delete(0,END)
        self.entries[0].insert(0,a.customer['first name'])
        
class Page_3(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        self.rowconfigure(3, weight=1)
        
        self.page_greet = b.header(self,'Please confirm your details:')
        
        text_frame = tk.Frame(self,width=490,height=200)
        text_frame.grid(row=2, column=0, columnspan=4, sticky="w")
        text_frame.grid_propagate(0)
        self.text = tk.Text(text_frame,width=400,height=40,relief='raised',borderwidth=2,font=("Arial",10),state='disabled')
        self.text.grid(row=0,column=0,columnspan=4,rowspan=3,padx=10,pady=10,sticky='w')
        
        copy_button = ttk.Button(self,text='Copy to clipboard',command=self.copy_to_clipboard)
        copy_button.grid(row=3,column=0,sticky='w',padx=10,pady=10)
        
        self.next_button = b.nav(self,parent,__class__,finish=True,next=False)
        self.bind('<Expose>',lambda x:self.update_widgets())
        
    def update_widgets(self):
        self.page_greet.config(text=f"Hi, {a.customer['first name']}")
        self.text.config(state='normal')
        self.text.delete(1.0,'end')
        for i,field in enumerate(a.customer):
            self.text.insert(tk.END,f"{field.title()}: {a.customer[field]}\n")
        for i,field in enumerate(a.address):
            self.text.insert(tk.END,f"{field.title()}: {a.address[field]}\n")
        self.text.insert(tk.END,f"Price: ${a.price:.2f}")
        self.text.config(state='disabled')
    
    def copy_to_clipboard(self):
        self.clipboard_clear()
        self.clipboard_append(self.text.get('1.0','end'))
        self.update()

def main():
    global a
    global b
    b = Builder()
    a = Access()
    app = App()
    app.mainloop()
    
if __name__ == "__main__":
    main()