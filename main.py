import tkthread; tkthread.patch()
import threading
import random
import shutil
import tkinter
from discord_webhook import DiscordWebhook, DiscordEmbed
import string
import subprocess
from time import time
import time
from turtle import width
from unittest import async_case
import requests
from alive_progress import alive_bar
import ctypes
from cProfile import label
from http.client import GATEWAY_TIMEOUT
from tarfile import PAX_NUMBER_FIELDS
from tkinter import *
from tkinter import colorchooser
from tkinter.colorchooser import askcolor
import os
from ttkthemes import ThemedStyle
from tkinter import messagebox
import sv_ttk
from tkinter import ttk
from urllib.request import Request, urlopen
import discord
import re
from goto import with_goto
from multiprocessing import Process
from threading import Thread
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import aiohttp
from requests import post
import asyncio
    
root = Tk()


root.tk.call('source', 'forest-dark.tcl')
try:
    root.iconbitmap("kos.ico")
except TclError: 
    print ('No ico file found')

# Set the theme with the theme_use method
ttk.Style().theme_use('forest-dark')

root.title("Terminator Grabber")
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tabControl.add(tab1, text ='Check')
tabControl.add(tab2, text ='delete')
tabControl.add(tab3, text ='Spammer')
tabControl.pack(expand = 1, fill ="both")
root.geometry('850x540')


ecolor='#A5A5A5'

e = ttk.Style()

e.configure("EntryStyle.TEntry",foreground=ecolor,)
entry_e = StringVar()
e = ttk.Entry(tab1, style="EntryStyle.TEntry", textvariable=entry_e,width=100)
e.grid(row=7, padx=5, pady=70, sticky="ew")
e.place(x=10, y=100)
e.insert(0, 'Your discord webhook here')

#

d = ttk.Style()

d.configure("EntryStyle.TEntry",foreground=ecolor,)
entry_d = StringVar()
d = ttk.Entry(tab2, style="EntryStyle.TEntry", textvariable=entry_d,width=100)
d.grid(row=7, padx=5, pady=70, sticky="ew")
d.place(x=10, y=100)
d.insert(0, 'Your discord webhook here')

#

s = ttk.Style()

s.configure("EntryStyle.TEntry",foreground=ecolor,)
entry_s = StringVar()
s = ttk.Entry(tab3, style="EntryStyle.TEntry", textvariable=entry_s,width=100)
s.grid(row=7, padx=5, pady=5, sticky="ew")
s.insert(0, 'Your discord webhook here')
s.place(x=10, y=100)

#

s2 = ttk.Style()

s2.configure("EntryStyle.TEntry",foreground=ecolor,)
entry_s2 = StringVar()
s2 = ttk.Entry(tab3, style="EntryStyle.TEntry", textvariable=entry_s2,width=100)
s2.grid(row=10, padx=5, pady=5, sticky="ew")
s2.insert(0, 'Your first massage here')
s2.place(x=10, y=150)


#

s3 = ttk.Style()

s3.configure("EntryStyle.TEntry",foreground=ecolor,)
entry_s3 = StringVar()
s3 = ttk.Entry(tab3, style="EntryStyle.TEntry", textvariable=entry_s3,width=100)
s3.grid(row=11, padx=5, pady=5, sticky="ew")
s3.insert(0, 'Your seccond massage here')
s3.place(x=10, y=200)
#

s4 = ttk.Style()

s4.configure("EntryStyle.TEntry",foreground=ecolor,)
entry_s4 = StringVar()
s4 = ttk.Entry(tab3, style="EntryStyle.TEntry", textvariable=entry_s4,width=100)
s4.grid(row=13, padx=5, pady=5, sticky="ew")
s4.insert(0, 'Your webhook name here')
s4.place(x=10, y=250)






lableH = Label(tab1 , text="Enter your Webhook : " , fg="#A5A5A5")
lableH.grid( row=10 , column=0 , padx=136 )
lableH.place(x=10, y=70)
lableH = Label(tab2 , text="Enter your Webhook : " , fg="#A5A5A5")
lableH.grid( row=10 , column=0 , padx=136 )
lableH.place(x=10, y=70)
lableH1 = Label(tab3 , text="Your 2nd massage :  " , fg="#A5A5A5")
lableH1.grid( row=10 , column=0 , padx=136 )
lableH1.place(x=10, y=70)
lableH2 = Label(tab3 , text="Your massage :  "  , fg="#A5A5A5")
lableH2.grid( row=10 , column=0 , padx=136 )
lableH2.place(x=10, y=50)
lableH3 = Label(tab3 , text="Webhook Username :  "  , fg="#A5A5A5")
lableH3.grid( row=10 , column=0 , padx=136 )
lableH3.place(x=10, y=30)
lableH4= Label(tab3 , text="massage count : " , fg="#A5A5A5")
lableH4.grid( row=10 , column=0 , padx=136 )
lableH4.place(x=10, y=10)
lableH5= Label(tab3 , text="Embed's color : " , fg="#A5A5A5")
lableH5.grid( row=10 , column=0 , padx=136 )
lableH5.place(x=200, y=10)

def clear_search(event):
    global ecolor
    placeholder1 = e.get()
    if placeholder1 == 'Your discord webhook here' :
        print(ecolor)
        print(ecolor)
        print(placeholder1)

        e.delete(0, tk.END)

def clear_search2(event):
    placeholder2 = d.get()
    if placeholder2 == 'Your discord webhook here' :
        ecolor = "#FFFFFF"
        print(placeholder2)
        d.delete(0, tk.END)

def clear_search3(event):
    placeholder3 = s.get()
    if placeholder3 == 'Your discord webhook here' :
        ecolor = "#FFFFFF"
        print(placeholder3)
        s.delete(0, tk.END)

def clear_search4(event):
    placeholder4 = s2.get()
    if placeholder4 == 'Your first massage here' :
        ecolor = "#FFFFFF"
        print(placeholder4)
        s2.delete(0, tk.END)

def clear_search5(event):
    placeholder5 = s3.get()
    if placeholder5 == 'Your seccond massage here' :
        ecolor = "#FFFFFF"
        print(placeholder5)
        s3.delete(0, tk.END)

def clear_search6(event):
    placeholder6 = s4.get()
    if placeholder6 == 'Your webhook name here':
        ecolor = "#FFFFFF"
        print(placeholder6)
        s4.delete(0, tk.END)


e.bind("<Button-1>", clear_search)
d.bind("<Button-1>", clear_search2)
s.bind("<Button-1>", clear_search3)
s2.bind("<Button-1>", clear_search4)
s4.bind("<Button-1>", clear_search6)
s3.bind("<Button-1>", clear_search5)


pedaretmord = True
pedarethexcode = "FF0000"
image1 = 'lab.png'
a2 = 'https://cdn.discordapp.com/icons/273534239310479360/189e2c71499f5f709a17123dcca84ed6.webp'


def kosl():
    threading.Thread(target=kos).start()  

def kos():  
    gay=e.get()


    lable2 = Label(tab1 , text="your webhook is : ")
    
 
    
    
    lable2.grid(row=1 , column=0 )
    lable2.place(x=20, y=10)
    try :
        test = requests.get(gay)
    except test.exceptions.MissingSchema:
        messagebox.showerror("Error", "Something went wrong")
    except test.exceptions.SSLError:
        messagebox.showerror("Error", "Cannot connect to the discord servers please check your connection and try again")
    except test.exceptions.ConnectionError:
        messagebox.showerror("Error", "Cannot connect to the discord servers please check your connection and try again")
    print(test.status_code)
    if test.status_code == 404:
        print("\n THE WEBHOOK IS INVALID")
        lable7 = Label(tab1 , text="Not correct" , fg="red")
        lable7.grid( row=1 , column=0 , padx=136 )
        lable7.place(x=136, y=10)
        
        
    elif test.status_code == 200:


        lable = Label(tab1 , text="Correct        " , fg="green")
        lable.grid( row=1 , column=0 , padx=136 )
        lable.place(x=136, y=10)
    

        time.sleep(1)

        
    else:
        print("\n THE WEBHOOK IS INVALID")
        lable7 = Label(tab1 , text="Not correct" , fg="red")
        lable7.grid( row=1 , column=0 , padx=136 )
        lable7.place(x=136, y=10)

 
def stop():


    global pedaretmord
    pedaretmord = False
    print("stop spamming ")
    threading.Thread(target=clear).start()

def spammd():
    threading.Thread(target=spamm).start()  

      

def getColor():
    """Choose color.
    Returns tuple of RBG and HEX."""
    import tkinter as tk
    from tkinter.colorchooser import askcolor
    win = None
    if not tk._default_root:
        win = tk.Tk()
        win.wm_withdraw()
    color = askcolor()
    if win is not None: 
        win.destroy()
    return color


def imagefn():
    threading.Thread(target=upload_file).start() 

def upload_file():
    global image1
    f_types = [('Jpg Files', '*.jpg'),
    ('PNG Files','*.png')]   # type of files to select 
    filename = tk.filedialog.askopenfilename(multiple=True,filetypes=f_types)
    col=2 # start from column 1
    row=1 # start from row 3 
    for f in filename:
        img=Image.open(f) # read the image file
        img=img.resize((85,85)) # new width & height
        img=ImageTk.PhotoImage(img)
        e1 =tk.Label(tab3)
        e1.grid(row=row,column=3)
        e1.place(x=750 , y=5)
        e1.image = img
        e1['image']=img # garbage collection 
        if(col==3): # start new line after third column
            row=row+1# start wtih next row
            col=1    # start with first column
        else:       # within the same row 
            col=col+1 # increase to next column   
       
        print(filename) 
       
        image1 = ''.join(filename)
        print(image1)
        threading.Thread(target=imgbbapi).start() 


a2 = image1

def imgbbapi():

    class imgBB:
    	def __init__(self,image_source):
    		self.image_source = image_source
    		self.json = None
    		self.url = None
    		self.thumbnail = None
    		self.filename = None
    		self.upload()
    	def upload(self):
            try:        
    		        # get image name from image path source
    		        image_name = self.image_source.split("/")[-1]
    		        # upload data if uploaf image from local storage
    		        if "http" not in self.image_source:
    		        	form_image = {"source":(image_name,open(self.image_source,"rb"),"multipart/form-data")}
    		        	form_data = {"upload-expiration":"","type":"file","action":"upload"}
    		        	result = post("https://imgbb.com/json",data=form_data,files=form_image).json()
    		        # and if image source is from url
    		        else:
    		        	form_data = {"source":self.image_source,"upload-expiration":"","type":"url","action":"upload"}
    		        	result = post("https://imgbb.com/json",data=form_data).json()
    		        self.json = result
    		        self.url = result["image"]["url"]
    		        self.thumbnail = result["image"]["thumb"]["url"]
    		        self.filename = result["image"]["name"]
            except:
                    messagebox.showerror("Error", "Cannot upload image")

    if __name__ == "__main__":
    	img_source = image1
    	IMG = imgBB(img_source)
    	print(IMG.url)
    global a2
    a2 = IMG.url
    print(a2)






def colorchooser():
    threading.Thread(target=colors).start()
def colors():
    global H5


    rgb, hexcode = getColor()
    global pedarethexcode
    global a2
    pedarethexcode = hexcode
    H5 = Label(tab3 , text=	"██", fg=pedarethexcode)
    H5.grid( row=10 , column=0 , padx=136 )
    H5.place(x=303, y=9)


def spamm():
    
    global a2
    global pedaretmord
    global H1,H2,H3,H4
    kos = 0

    marami = s2.get()
    harami = s3.get()
    garami = s4.get()
    webhookk = s.get()
    khasteshodam = a2
    print(khasteshodam)

    if harami == 'Your seccond massage here' :
            harami = " "
    elif bool(harami) == False:
        harami = " "       
    if garami == 'Your webhook name here' :
        pedaretmord = False
        messagebox.showerror("Error", "Please specify your webhook name")
        garami = ''
    elif bool(garami) == False:
        pedaretmord = False
        messagebox.showerror("Error", "Please specify your webhook name") 
        garami = ''            
    if khasteshodam == '' :
        khasteshodam = "https://cdn.discordapp.com/icons/273534239310479360/189e2c71499f5f709a17123dcca84ed6.webp"
    elif bool(khasteshodam) == False:
        khasteshodam = "https://cdn.discordapp.com/icons/273534239310479360/189e2c71499f5f709a17123dcca84ed6.webp"   
    elif khasteshodam == 'lab.png':
        khasteshodam = "https://cdn.discordapp.com/icons/273534239310479360/189e2c71499f5f709a17123dcca84ed6.webp" 
    if marami == 'Your first massage here' :
        marami = ""
    elif bool(marami) == False:
            marami = " "  
    if webhookk == 'Your discord webhook here' :
            pedaretmord = False
            messagebox.showerror("Error", "Please specify your webhook")
    elif bool(webhookk) == False:
            pedaretmord = False
            messagebox.showerror("Error", "Please specify your webhook")
            
    H1 = Label(tab3 , text=harami , fg="#A5A5A5")
    H1.grid( row=10 , column=0 , padx=136 )
    H1.place(x=142, y=70)
    H2 = Label(tab3 , text=marami , fg="#A5A5A5")
    H2.grid( row=10 , column=0 , padx=136 )
    H2.place(x=115, y=50)
    H3 = Label(tab3 , text=garami , fg="#A5A5A5")
    H3.grid( row=10 , column=0 , padx=136 )
    H3.place(x=155, y=30)
    while pedaretmord:

        
        kos=kos+1


        pattern = r'[#]'

        # Match all digits in the string and replace them with an empty string
        kircode = re.sub(pattern, '', pedarethexcode)
        print(kircode)
        print(harami)
 

        webhook = DiscordWebhook(url=webhookk, username=garami, avatar_url=khasteshodam)
    
        embed = DiscordEmbed(
            title="```"+harami+"```", description=marami, color=kircode
        )
        embed.set_author(
            name=harami,
            url=khasteshodam,
            icon_url=khasteshodam
            ,
        )
        webhook.add_embed(embed)
        response = webhook.execute()
        
        
        H4= Label(tab3 , text=str(kos) , fg="#A5A5A5")
        H4.grid( row=10 , column=0 , padx=136 )
        H4.place(x=117, y=10)
        
        print(kos)

        time.sleep(1)

   
    pedaretmord = True

def clear():
    time.sleep(1)
    H1.place_forget()
    H2.place_forget()
    H3.place_forget()
    H4.place_forget()
    KosH4= Label(tab3 , text='                ' , fg="#A5A5A5")
    KosH4.grid( row=10 , column=0 , padx=136 )
    KosH4.place(x=117, y=10)


def thedelete():
    threading.Thread(target=delete).start()
def delete():
    gay=d.get()
    print(gay)
    try:
        check = requests.get(gay)
    except requests.exceptions.MissingSchema:
        messagebox.showerror("Error", "Something went wrong")
    except requests.exceptions.SSLError:
        messagebox.showerror("Error", "Cannot connect to the discord servers please check your connection and try again")
    except requests.exceptions.ConnectionError:
        messagebox.showerror("Error", "Cannot connect to the discord servers please check your connection and try again")
    print(check.status_code)
    if check.status_code == 200:
        print("dadash ba movafaghiyat webhook az ro zamin mahv shod !\n\nbar tabl shadaneh bekoob!\n\npirooz va mardaneh bekoob!\n\n:D")
        requests.delete(gay)
        lableH = Label(tab2 , text="Your webhook has been deleted successfully :)                  " , fg="green")
        lableH.grid( row=1 , column=0 , padx=136 )
        lableH.place(x=136, y=10)
    elif check.status_code == 404:
        print("eh hazf nashod ke bad shod ke \n:(")
        print("dadash ba movafaghiyat webhook az ro zamin mahv shod !\n\nbar tabl shadaneh bekoob!\n\npirooz va mardaneh bekoob!\n\n:D")
        
        lableR = Label(tab2 , text="Cannot delete this webhook because it does not exist :(" , fg="#FF0000")
        lableR.grid( row=1 , column=0 , padx=136 )
        lableR.place(x=136, y=10)

    else:
        lableR = Label(tab2 , text="Cannot delete this webhook  :(                                  " , fg="#FF0000")
        lableR.grid( row=1 , column=0 , padx=136 )
        lableR.place(x=136, y=10)
	



but = ttk.Button(tab1, text="Check" , command=kosl, width=100)
but.grid(row=9 ,padx=10 , pady=10 )
but.place(y=200 , x=10)


but2 = ttk.Button(tab3, text="Spam" ,command=spammd, width=100 )
but2.grid(row=20, padx=10 , pady=10 )
but2.place(x=10, y=300)
        

but3 = ttk.Button(tab2, text="Delete"  ,command=thedelete, width=100 )
but3.grid(row=13, padx=10 , pady=10) 
but3.place(y=200 , x=10)

but4 = ttk.Button(tab3, text="Stop spamming"  ,command=stop, width=100 )
but4.grid(row=40, padx=10 , pady=10) 
but4.place(x=10, y=350)
but5 = ttk.Button(tab3, text="Embed's color"  ,command=colorchooser, width=100 )
but5.grid(row=50, padx=10 , pady=10) 
but5.place(x=10, y=400)
but6 = ttk.Button(tab3, text="Profile Picture"  ,command=imagefn, width=100 )
but6.grid(row=70, padx=10 , pady=10) 
but6.place(x=10, y=450)




root.mainloop()     

