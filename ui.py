#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox
from utl1 import disp
from utl1 import get_trend

window=tk.Tk()

cate_var = tk.StringVar(window)
cate_var.set("Select category")

cate_var1 = tk.StringVar(window)
cate_var1.set("Select category")

cate_wid = tk.OptionMenu(window,cate_var,"Furniture","Office Supplies","Technology")
cate_wid1 = tk.OptionMenu(window,cate_var1,"Furniture","Office Supplies","Technology" )


lbl1=tk.Label(window,text="Enter sales expected")
entry2 = tk.Entry(window)
entry3 = tk.Entry(window)


def sub():
    lbl1.place_forget()
    entry2.place_forget()
    cate_wid1.place_forget()
    submit_button4.place_forget()
  
    cate_wid.place(x=220,y=280)
    
   
    submit_button2.place(x=220,y=320)   

def submit():
    cate_wid.place_forget()
    submit_button2.place_forget()
   
    x=cate_var.get()
    get_trend(x)
    
    
def sub2():
    cate_wid.place_forget()
    submit_button2.place_forget()
    lbl1.place(x=120,y=280)
    entry2.place(x=280,y=280)
    cate_wid1.place(x=200,y=320)

    submit_button4.place(x=200,y=350)   

    
def submit2():
    lbl1.place_forget()
    entry2.place_forget()
    cate_wid1.place_forget()
    submit_button4.place_forget()
  
    x=entry2.get()
    y=cate_var1.get()
    disp(x,y)
    
window.title("SMART DEMAND PREDICTOR")
window.geometry("500x500")
submit_button4 = tk.Button(window, text = "GO", command = submit2)
submit_button2 = tk.Button(window, text = "GO", command = submit)

#entry2 = Entry(window)
#entry2.pack()
        
submit_button1 = tk.Button(window, text = "Get trend", command = sub)
submit_button1.place(x=220,y=180)

submit_button3 = tk.Button(window, text = "Get profit", command = sub2)
submit_button3.place(x=220,y=220)
window.mainloop()



# In[ ]:




