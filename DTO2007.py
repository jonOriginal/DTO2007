#------------------------------------------------------------------------------
#DTO2007YA 
#Jonathan Knox 
#------------------------------------------------------------------------------

import sys
import tkinter as tk 
from tkinter import END, X, ttk
from tkinter import messagebox
import time
class Get_details(dict):
    """Getter, setter and deleter for dictionary items"""
    def __getitem__(self, key) -> str:
        return dict.__getitem__(self, key)
    def __setitem__(self, key, value) -> None:
        dict.__setitem__(self, key, value)
    def __delitem__(self, key) -> None:
        dict.__setitem__(self, key, '')
     
class Access():
    """Holds variables and passes them to Get_details class"""
    def __init__(self):
        self.address = Get_details({'address':'','city':'','postcode':''})
        self.dimensions = Get_details({"height":'',"width":'',"length":''})
        self.customer = Get_details({'first name':'','last name':'','phone':''}) 
        self.region_multiplier= {'North island':1,'South island':1.5,'Stewart island':2}    #price multiplier : region
        self.rates = {0:8.00,6000:12.00,100000:15.00}                                       #volume : price dictionary
        self.price = 0                                                                      #final calculated price
        
class Builder():
    """This class builds generic tkinter elements"""
    @staticmethod
    def header(master: tk.Frame, title: str, greet :bool = True) -> tk.Label | tk.Frame:
        """Builds a header frame with a title and greeting

        Args:
            master (tk.Frame): The frame to add the header to
            title (str): The title of the header
            greet (bool, optional): Whether to generate header . Defaults to True.

        Returns:
            tk.Label | tk.Frame: returns either a label or a frame depending on the value of greet
        """
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
    def nav_buttons(master: tk.Frame, parent: classmethod,current:str,back = True,next = True,finish = False) -> tk.Button:
        """Generates navigation buttons for the application

        Args:
            master (tk.Frame): The frame to add the buttons to
            parent (classmethod): The master class for the application
            current (str): current page name
            back (bool, optional): Whether to include a back button. Defaults to True.
            next (bool, optional): Whether to include a next button . Defaults to True.
            finish (bool, optional): Whether to include a finish button. Defaults to False.

        Returns:
            tk.Button: Returns the next button
        """
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
    def entry(master: tk.Frame,Label: str,row: int,column: int,validatecommand:tuple,validate = 'key',width=15) -> tk.Entry:
        """Generates an entry field for the application

        Args:
            master (tk.Frame): The frame to add the entry to
            Label (str): The label text for the entry
            row (int): The row to add the entry to
            column (int): The column to add the entry to
            validatecommand (tuple): The validation command for the entry
            validate (str, optional): validation method . Defaults to 'key'.
            width (int, optional): width of the label. Defaults to 15.

        Returns:
            tk.Entry: Returns the entry field
        """
        frame = tk.Frame(master)
        frame.grid(row=row, column=column, sticky='ew',columnspan=1)
        label = ttk.Label(frame, text=Label,width=width)
        label.grid(row=0, column=0, sticky='w', pady=5, padx=5)
        entry = ttk.Entry(frame,validate=validate,validatecommand=validatecommand)
        entry.grid(row=0, column=1, sticky='w', pady=5, padx=5)
        return entry
    
    @staticmethod
    def lframe(master:tk.Frame,lable:str,text:str,row:int,column:int,columnspan=2,rowspan=4) -> tk.LabelFrame:
        """Generates a label frame for the application

        Args:
            master (tk.Frame): The frame to add the label frame to
            lable (str): The label text for the label frame
            text (str): The main text for the label frame
            row (int): The row to add the label frame to
            column (int): The column to add the label frame to
            columnspan (int, optional): The column span of the labelframe. Defaults to 2.
            rowspan (int, optional): The row span of the labelframe. Defaults to 4.

        Returns:
            tk.LabelFrame: Returns the label frame
        """        
        frame = ttk.LabelFrame(master,text=lable)
        frame.grid(row=row, column=column, sticky='ew',columnspan=columnspan,padx=5,pady=5,rowspan=rowspan)
        label = ttk.Label(frame, text=text)
        label.grid(row=0, column=0, sticky='w', pady=5, padx=5)
        return frame
    
    @staticmethod
    def label(master:tk.Frame,text:str,row:int,column:int,font=(),columnspan=1,rowspan=1,foreground='black',justify = 'left',sticky = 'ew') -> tk.Label:
        """generates a label for the application

        Args:
            master (tk.Frame): The frame to add the label to
            text (str): The text for the label
            row (int): The row to add the label to
            column (int): The column to add the label to
            font (tuple, optional): The font of the text. Defaults to ().
            columnspan (int, optional): Columnspan of the label. Defaults to 1.
            rowspan (int, optional): Rowspan of the label. Defaults to 1.
            foreground (str, optional): The text color. Defaults to 'black'.
            justify (str, optional): Text alignment. Defaults to 'left'.
            sticky (str, optional): Grid alignment. Defaults to 'ew'.

        Returns:
            tk.Label: Returns the label
        """
        label = ttk.Label(master,text=text,font=font,foreground=foreground,justify=justify)
        label.grid(row=row, column=column, sticky=sticky,columnspan=columnspan,padx=5,pady=5,rowspan=rowspan)
        return label
class App(tk.Tk):
    """
    Main Application class
    
    Methods:
        __init__(): initialises the application, and sets the title, and size
        next(str): switches to the next page, given the current page
        back(str): switches to the previous page, given the current page
    """
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        
        #initialize the master tkinter frame
        self.title("DTO2007Y2A")
        self.geometry("500x350")
        self.resizable(False, False)
        mainframe = ttk.Frame(self)
        mainframe.pack(side="top", fill="none", expand=False)
        
        #create and initialize each page of the application
        self.frame_list = {Start_Page:'',Page_1:'',Page_2:'',Page_3:''}
        for frame_name in self.frame_list:
            frame = frame_name(self,mainframe)
            frame.config(width=500,height=350)
            self.frame_list[frame_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.grid_propagate(False)
    
        #raise the first page of the application
        self.frame_list[Start_Page].tkraise()

        
    def next(self,current: str) -> None:
        #find the page name of the next page
        index = list(self.frame_list.keys()).index(current)+1
        name = list(self.frame_list.keys())[index]
        
        #raise the next page of the application
        self.frame_list[name].tkraise()   
        
    def back(self,current: str) -> None:
        #find the page name of the previous page
        i = list(self.frame_list.keys()).index(current)-1
        name = list(self.frame_list.keys())[i]
        
        #raise the previous page of the application
        self.frame_list[name].tkraise()
        
class Start_Page(tk.Frame):
    '''first page of the application'''
    def __init__(self,parent,container) -> None:
        super().__init__(container)
        #configure the master frame
        self.rowconfigure(2, weight=1)
        reg = self.register(self.callback)

        #build the title
        self.page_greet = b.header(self,'Onlinz Shopping returns',False)
        
        #build the main text
        info_text="Welcome to the Onlinz Shopping returns application.\n\nIf your product is returned undamaged within 30 days, you will receive\na full refund of the purchase price.\n\nThis program will help you calculate the courier cost and collect \ninformation needed to return the product."
        b.label(self,info_text,1,0,font=('Arial', 12),justify='left',columnspan=4) 
        
        #build the name entry
        self.name_entry = b.entry(self,'First Name:',6,0,validatecommand=(reg,'%P'))
        self.name_entry.bind('<Return>', lambda event: self.next_button.invoke())
        #build the next button
        self.next_button = b.nav_buttons(self,parent,__class__,back=False)
        
        self.bind('<Expose>', lambda x: self.update_wdigets())
    def callback(self,value:str|int) -> bool:
        """callback function for the name entry

        Args:
            value (str | int): The value the entry will have if the validation is successful

        Returns:
            bool: Returns True if change is allowed, False otherwise
        """        
        if value:
            #if the value is not empty, activate the next button
            a.customer['first name'] = value.title()
            self.next_button.configure(state='normal')
            return True  
        if value == '':
            #if the value is empty, deactivate the next button
            self.next_button.configure(state='disabled')
            return True

    def update_wdigets(self) -> None:
        """updates the name entry with the current customer name"""
        self.name_entry.delete(0,END)
        self.name_entry.insert(0,a.customer['first name'])
        self.name_entry.focus()
        
class Page_1(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        #configure the master frame
        self.rowconfigure(5, weight=1)
        reg = self.register(self.callback)
        
        #build the title
        self.page_greet = b.header(self,'Please enter the package dimensions and region:')
        
        #build labelframe then create each entry 
        measurements = b.lframe(self,'Measurements','Enter the dimensions of the package in cm:',1,0)
        self.entries = {"height":'',"width":'',"length":''}
        for i,fields, in enumerate(a.dimensions):
            #validate all events for the entries so that only float values are allowed
            ents = b.entry(measurements,fields.title(),i+1,0,validate='all',validatecommand=(reg, '%P','%V',fields),width=14)
            ents.bind('<Return>', lambda event: event.widget.tk_focusNext().focus_set())
            self.entries[fields] = ents
        
        #build the error labels
        self.error_container = {'width':'','height':'','length':''}
        for i,fields, in enumerate(self.error_container):
            self.error_container[fields] = b.label(measurements,'',4,0,justify='center',columnspan=2,foreground='red',sticky=None)
        
        #build a region selection box
        region = b.lframe(self,'Region','Select the region you are sending from:',1,2,rowspan=2)
        self.dropbox = ttk.Combobox(region,values=list(a.region_multiplier.keys()),state='readonly')
        self.dropbox.grid(row=1,column=0,sticky='ew',padx=15,pady=5)
        
        #when the combo box is changed, confirm if the next button should be activated
        self.dropbox.bind('<<ComboboxSelected>>',lambda event: self.confirm_next())
        #when enter is pressed, try to invoke the next button
        self.dropbox.bind('<Return>', lambda event: self.next_button.invoke())
        
        #create price esitmate box
        estimate = b.lframe(self,'Price','The shipping cost to return the product:',3,2,rowspan=2)
        self.price_number = b.label(estimate,'$0.00',1,0,justify='center',columnspan=2,font=('Arial', 11, 'bold'),rowspan=2,sticky=None)
        
        #build the next button
        self.next_button = b.nav_buttons(self,parent,__class__)
        
        #when class frame is raised, call the update_widgets function
        self.bind('<Expose>',lambda x:self.update_widgets())
    def update_widgets(self) -> None:
        """update the widgets in the class frame"""
        #update the title greeting name
        self.page_greet.config(text=f"Hi, {a.customer['first name']}")
        
        #focus the first entry if all the entries are empty
        if all(list(a.dimensions.values())) == False:
            self.entries['height'].focus()
    
    def callback(self,value: str|float, reason: tk.EventType, name: str) -> bool:
        """callback function for the entry widgets

        Args:
            value (str | float): The value the entry will have if the validation is successful
            reason (tk.EventType): The reason the validation is being called
            name (str): The name of the entry being validated

        Returns:
            bool: Returns True if change is allowed, False otherwise
        """        
        try:
            value = float(value)
            
            #if the user has exited the entry, check if the value is between 5 and 100 and update the error label
            if reason == 'focusout':
                if value < 5 or value > 100:
                    self.error_container[name].config(text='Please enter a value  between 5 and 100.')
                else:
                    self.error_container[name].config(text='')
                    
            #set the corresponding variable to the value
            a.dimensions[name] = value
            
            #check if the next button should be activated and accept the change
            self.confirm_next()
            return True
        
        except:
            #if the value is not a float, clear the corresponding dictionary entry
            if value == '':
                del a.dimensions[name]
                
                #check if the next button should be activated and accept the change
                self.confirm_next()
                return True
            else:
                #if the value is not a float or empty deny the change
                return False

    def update_price(self):
        """update the price estimate label"""
        try:
            multiplier=a.region_multiplier[self.dropbox.get()]
            volume = a.dimensions['height']*a.dimensions['width']*a.dimensions['length']
            
            #calculate the price using the volume and the multiplier and update the label
            for i,vol in enumerate(a.rates):
                if volume > vol:
                    a.price = a.rates[vol]*multiplier
                    self.price_number.config(text=f'${a.price:.2f}')
        except:
            #if the dropbox or entry is empty, clear the label
            self.price_number.config(text='$0.00')

    def confirm_next(self):
        """confirm if the next button should be activated"""
        values = [a.dimensions['height'],a.dimensions['width'],a.dimensions['length']]
        region = self.dropbox.get()
        
        #if all three entries are filled and the region is not empty, activate the next button
        if all(values) == True and all(map(lambda x: float(x) >= 5 and float(x) <= 100,values)) == True and region:
            self.next_button.config(state='normal')
            self.update_price()
        #if any of the entries are empty or the region is empty, deactivate the next button
        else:
            self.next_button.config(state='disabled')
class Page_2(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        #configure the master frame
        self.rowconfigure(5, weight=1)
        reg = self.register(self.callback)
        reg_a = self.register(self.callback_a)
        
        #build the title
        self.page_greet = b.header(self,'Please enter your details:')
        
        #build the next button
        self.next_button = b.nav_buttons(self,parent,__class__)
        
        #build labelframe then create each entry for the customer details
        details = b.lframe(self,'Personal Details','These details will be used by the courier:',1,0)
        self.entries=[]
        for i,fields, in enumerate(a.customer):
            ents = b.entry(details,fields.title(),i+1,0,validate='key',validatecommand=(reg, '%P',fields))
            ents.bind('<Return>', lambda event: event.widget.tk_focusNext().focus_set())
            self.entries.append(ents)
        
        #build labelframe then create each entry for the address details
        addresses = b.lframe(self,'Address','Enter the address you are sending from:',1,2)
        address=[]
        for i,fields, in enumerate(a.address):
            ents  = b.entry(addresses,fields.title(),i+1,0,validate='key',validatecommand=(reg_a, '%P',fields),width=13)
            ents.bind('<Return>', lambda event: event.widget.tk_focusNext().focus_set())
            address.append(ents)
        address[-1].unbind('<Return>')
        address[-1].bind('<Return>', lambda event:self.next_button.invoke())
        
        #when class frame is raised, call the update_widgets() function
        self.bind('<Expose>',lambda x:self.update_widgets())
    def callback(self,value: str ,name:str) -> bool:
        """callback function for the customer detail widgets

        Args:
            value (str): The value the entry will have if the validation is successful
            name (str): The name of the entry being validated

        Returns:
            bool: Returns True if change is allowed, False otherwise
        """
        #if the value is not empty, set the corresponding variable to the value
        if value != '':
            a.customer[name] = value.title()
        
        #check if the next button should be activated and accept the change
        self.confirm_next()
        return True
    
    def callback_a(self,value: str ,name:str) -> bool:
        """callback function for the address detail widgets

        Args:
            value (str): The value the entry will have if the validation is successful
            name (str): The name of the entry being validated

        Returns:
            bool: Returns True if change is allowed, False otherwise
        """
        #set the corresponding variable to the value and check if the next button should be activated
        a.address[name] = value.title()
        self.confirm_next()
        return True
    
    def confirm_next(self):
        """confirm if the next button should be activated"""
        #if all the entries are filled, activate the next button
        if all(list(a.customer.values())) == True and all(list(a.address.values())) == True:
            self.next_button.config(state='normal')
        else:
            self.next_button.config(state='disabled')
    
    def update_widgets(self):
        """update the name in the title and name entry"""
        self.page_greet.config(text=f"Hi, {a.customer['first name']}")
        self.entries[0].delete(0,END)
        self.entries[0].insert(0,a.customer['first name'])
        self.entries[0].focus()
        
class Page_3(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        #configure the master frame
        self.rowconfigure(3, weight=1)
        
        #build the title
        self.page_greet = b.header(self,'Please confirm your details:')
        
        #build the text widget
        text_frame = tk.Frame(self,width=490,height=200)
        text_frame.grid(row=2, column=0, columnspan=4, sticky="w")
        text_frame.grid_propagate(0)
        self.text = tk.Text(text_frame,width=400,height=40,relief='raised',borderwidth=2,font=("Arial",10),state='disabled')
        self.text.grid(row=0,column=0,columnspan=4,rowspan=3,padx=10,pady=10,sticky='w')
        
        #build the copy button
        copy_button = ttk.Button(self,text='Copy to clipboard',command=self.copy_to_clipboard)
        copy_button.grid(row=3,column=0,sticky='w',padx=10,pady=10)
        
        #build the finish button
        self.next_button = b.nav_buttons(self,parent,__class__,finish=True,next=False)
        
        #when class frame is raised, call the update_widget() function
        self.bind('<Expose>',lambda x:self.update_widgets())
        
    def update_widgets(self):
        """update the text in the text widget and the name in the title"""
        #update the first name in the title
        self.page_greet.config(text=f"Hi, {a.customer['first name']}")
        
        #enable and clear the text widget
        self.text.config(state='normal')
        self.text.delete(1.0,'end')
        
        #build the text in the text widget for the customer details and address details
        for i,field in enumerate(a.customer):
            self.text.insert(tk.END,f"{field.title()}: {a.customer[field]}\n")
        for i,field in enumerate(a.address):
            self.text.insert(tk.END,f"{field.title()}: {a.address[field]}\n")
        
        #insert the total price in the text widget
        self.text.insert(tk.END,f"Price: ${a.price:.2f}")

        self.text.config(state='disabled')
    
    def copy_to_clipboard(self):
        """copy the text in the text widget to the clipboard"""
        self.clipboard_clear()
        self.clipboard_append(self.text.get('1.0','end'))
        self.update()

def main():
    """main function"""
    global a,b
    a,b = Access(),Builder()
    app = App()
    app.mainloop()
    
if __name__ == "__main__":
    """if this is the main file, run the main function"""
    main()