#!/usr/bin/env python
# coding: utf-8

# In[2]:

import pandas as pd
from arima import get_trend_pic
import tkinter as tk
from sklearn.externals import joblib 
import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import os
warnings.filterwarnings("ignore")
plt.style.use("fivethirtyeight")
import pandas as pd
import statsmodels.api as sm
import matplotlib
from tkinter import messagebox

matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 14

matplotlib.rcParams['ytick.labelsize'] = 14
matplotlib.rcParams['text.color'] = 'b';

def get_trend(item):

    get_trend_pic(item)    
    from PIL import ImageTk,Image  
    root = tk.Toplevel()  
    
    canvas = tk.Canvas(root, width = 1000, height = 1000)
    canvas.configure(background='black')
    canvas.pack()  
    img1=Image.open("devuzz.png")
    img2 = img1.resize((1008,500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img2)  
    
    canvas.create_image(500,500,image=img)
    identify_trend()                    
    
    root.mainloop()  

    
def disp(x,y):
    
 
    if y == 'Furniture':
        y=1
    elif y == 'Office Supplies':
        y=2
    elif y == 'Technology':
        y=3
    else:
        y=0
    data = [[x,y]] 
    

    new = pd.DataFrame(data, columns = ['Sales', 'Category'])  
    print(new)
    # Load the model from the file 
    knn_from_joblib = joblib.load('filename.pkl')  
  
    # Use the loaded model to make predictions 
    pre=knn_from_joblib.predict(new) 
    messagebox.showinfo("Profit expected",pre[0][0])

# In[ ]:
def identify_trend():

                        
    knn_from_joblib = joblib.load('filename2.pkl')
                        
    from keras.preprocessing import image
    test_image = image.load_img('s1.png', target_size = (64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result=knn_from_joblib.predict(test_image) 
  
    if result[0][0] == 1:
        prediction = 'continous'
    else:
        prediction = 'reversal'    
                      
    messagebox.showinfo("Trend is",prediction)
                        
