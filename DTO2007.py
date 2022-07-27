"""
Jonathan Knox
DTO2007Y2A V1
5/07/22
"""
from cProfile import label
import tkinter as tk
from tkinter import ttk

from matplotlib import container
root = tk.Tk()
temp_dimensions = {"height":'',"width":'',"length":''}
region_multiplier= {'north island':1,'south island':1.5,'stewart island':2}
customer_details = {'first name':'','last name':'','address':'','phone':''}

from tkinter import messagebox

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.title("DTO2007Y2A")
        self.geometry("500x500")
        mainframe = ttk.Frame(self)
        mainframe.pack(side="top", fill="both", expand=True)
        
        self.frame_list = {StartPage:''}
        for i, frame_name in enumerate(self.frame_list):
            frame = frame_name(self,mainframe)
            self.frame_list[frame_name] = frame
        self.switch_frame(StartPage)
    
    def switch_frame(self, page_name):
        self.frame_list[page_name].tkraise()
    
    @staticmethod
    def callback(input):
        try:
            float(input)
            return True
        except:
            if input == '':
                return True
            else:
                return False
    

class StartPage(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        reg=root.register(App.callback)
        for i,fields, in enumerate(temp_dimensions):
            labs = ttk.Label(root,text=fields)
            ents = ttk.Entry(root)
            ents.config(validate="key", validatecommand=(reg, '%P'),textvariable=temp_dimensions[fields])
            labs.grid(row=i,column=0)
            ents.grid(row=i,column=1)
            temp_dimensions[fields] = ents
        
class Page_2(tk.Frame):
    def __init__(self,parent,container):
        super().__init__(container)
        self.region_var=tk.StringVar()
        for i, radios in enumerate(region_multiplier):
            self.rad = ttk.Radiobutton(root,text=radios,value=region_multiplier[radios],variable=self.region_var)
            self.rad.grid(column=0,row=i)
        region_confirm = ttk.Button(root,text='confirm',command=get_customer_details)
        region_confirm.grid(column=0,row=i+1)
        
class Page_3(tk):
    def __init__(self,parent,container):
        super().__init__(container)
        for i,fields, in enumerate(customer_details):
            labs = ttk.Label(root,text=fields)
            ents = ttk.Entry(root)
            ents.config(validate="key",textvariable=customer_details[fields])
            labs.grid(row=i,column=0)
            ents.grid(row=i,column=1)
            customer_details[fields] = ents
            
"""def calculate():
    if temp_dimensions['height'].get() == '' or temp_dimensions['width'].get() == '' or temp_dimensions['length'].get() == '':
        messagebox.showerror('Python Error', 'Error: This is an Error Message!')
    else:
        total = tk.Label(root,textvariable=float(temp_dimensions['height'].get())* float(temp_dimensions['width'].get()) * float(temp_dimensions['length'].get()))
        total.grid(column=3,row =0)
        global volume_label
        volume_label.config(text=total.cget('textvariable'))
        clearFrame()
        region_select()"""
        
def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()