from tkinter import *
import tkinter as tk
import pytz
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta
import requests
from PIL import Image, ImageTk
from tkinter import messagebox, ttk

root = Tk()  
root.title("Weather App 5")
root.geometry("750x470+300+200")  
root.resizable(False, False)  
root.config(bg="#202731")  

#icon 
image_icon=PhotoImage(file="Images/logo.png")
root.iconphoto(False,image_icon)

Round_box=PhotoImage(file="Images/Rounded Rectangle 1.png")
Label(root,image=Round_box,bg="#202731").place(x=30,y=60)


#label
label1=Label(root,text="Temperature",font=("Helvetica",11),fg="#323661",bg="#aad1c8")
label1.place(x=50,y=120)

label2=Label(root,text="Humidity",font=("Helvetica",11),fg="#323661",bg="#aad1c8")
label2.place(x=50,y=140)

label3=Label(root,text="Pressure",font=("Helvetica",11),fg="#323661",bg="#aad1c8")
label3.place(x=50,y=160)

label4=Label(root,text="Wind Speed",font=("Helvetica",11),fg="#323661",bg="#aad1c8")
label4.place(x=50,y=180)

label5=Label(root,text="Description",font=("Helvetica",11),fg="#323661",bg="#aad1c8")
label5.place(x=50,y=200)


#Search Box

Search_image=PhotoImage(file="Images/Rounded Rectangle 3.png")
myimage=Label(root,image=Search_image,bg="#202731")
myimage.place(x=270,y=122)


weat_image=PhotoImage(file="Images/Layer 7.png")
weatherimage=Label(root,image=weat_image,bg="#333c4c")
weatherimage.place(x=290,y=127)


textfield=tk.Entry(root,justify="center",width=15,font=("poppins",25,"bold"),bg="#a33c4c",border=0,fg="White")
textfield.place(x=370,y=130)

Search_icon=PhotoImage(file="Images/Layer 6.png")
myimage_icon=Button(root,image=Search_icon,borderwidth=0,cursor="hand2",bg="#333c4c")
myimage_icon.place(x=640,y=135)



#BottomBox
frame=Frame(root,width=900,height=180,bg="#7094d4")
frame.pack(side=BOTTOM)

#boxes
firstbox=PhotoImage(file="Images/Rounded Rectangle 2.png")
secondbox=PhotoImage(file="Images/Rounded Rectangle 2 copy.png")

Label(frame,image=firstbox,bg="#7094d4").place(x=30,y=20)
Label(frame,image=secondbox,bg="#7094d4").place(x=300,y=30)
Label(frame,image=secondbox,bg="#7094d4").place(x=400,y=30)
Label(frame,image=secondbox,bg="#7094d4").place(x=500,y=30)
Label(frame,image=secondbox,bg="#7094d4").place(x=600,y=30)


#Clock

clock=Label(root,font=("Helvetica",20),bg="#202731",fg="white")
clock.place(x=30,y=20)

#timezone

timezone=Label(root,font=("Helvetica",20),bg="#202731",fg="white")
timezone.place(x=500,y=20)

long_lat=Label(root,font=("Helvetica",10),bg="#202731",fg="white")
long_lat.place(x=500,y=50)


#thpwd
t=Label(root,font=("Helvetica",9),bg="#333c4c",fg="white")
t.place(x=150,y=120)

h=Label(root,font=("Helvetica",9),bg="#333c4c",fg="white")
h.place(x=150,y=140)

p=Label(root,font=("Helvetica",9),bg="#333c4c",fg="white")
p.place(x=150,y=160)

w=Label(root,font=("Helvetica",9),bg="#333c4c",fg="white")
w.place(x=150,y=180)

d=Label(root,font=("Helvetica",9),bg="#333c4c",fg="white")
d.place(x=150,y=200)




root.mainloop()
