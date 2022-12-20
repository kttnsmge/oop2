
from email.mime import image
from tkinter import *
from turtle import width
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
   


def change_seats1():
   
    seats_image2 = Image.open("seats2.jpg")
    resize_seats_image2 = seats_image2.resize((50,35))
    seats_icon2 = ImageTk.PhotoImage(resize_seats_image2)
    seatsButton1.configure(image= seats_icon2)
    seatsButton1.image = seats_icon2

def view(pencere):
    global seatsButton1, seatsButton2, seatsButton3, seatsButton4, seatsButton5, seatsButton6
    global  seatsButton7,  seatsButton8, seatsButton9, seatsButton10, seatsButton11, seatsButton12, seatsButton13, seatsButton14
    global  seatsButton15, seatsButton16, seatsButton17, seatsButton18, seatsButton19, seatsButton20

    root = tk.Toplevel()
    root.resizable(False, False)
    root.title("Selection...")
    root.geometry("1000x650")

    image1 = Image.open("loginpage.png")
    resize_image2 = image1.resize((1000, 650))
    image2 = ImageTk.PhotoImage(resize_image2)

    canvas = Canvas(root, width=1000, height=650)
    canvas.pack(fill=BOTH, expand=True)
    canvas.create_image(0,0, image=image2, anchor="nw")
    pencere.withdraw()

    cinema_image = Image.open("cinema.jpg")
    resize_cinema_image = cinema_image.resize((300,100))
    cinema_image2 = ImageTk.PhotoImage(resize_cinema_image)
    cinema_label = Label(canvas,image = cinema_image2, bg="black")
    cinema_label.place(x=350,y=30)

    selection_label = Label(canvas, text="-> Please select any seats...", font=("Lucida Sans",20,"bold"), width= 25, bg="black",fg="white")
    selection_label.place(x=265, y=125)
    
    seats_image1 = Image.open("seats1.jpg")
    resize_seats_image1 = seats_image1.resize((50,35))
    seats_icon1 =   ImageTk.PhotoImage(resize_seats_image1)


    seatsButton1 = Button(canvas, bg="black", image= seats_icon1,activebackground="black",command=lambda:change_seats1())
    seatsButton1.place(x=320, y=170)
    seatsButton2 = Button(canvas, bg="black", image= seats_icon1,activebackground="black")
    seatsButton2.place(x=400, y=170)
    seatsButton3 = Button(canvas, bg="black", image= seats_icon1,activebackground="black")
    seatsButton3.place(x=480, y=170)
    seatsButton4 = Button(canvas, bg="black", image= seats_icon1,activebackground="black")
    seatsButton4.place(x=560, y=170)
    seatsButton5 = Button(canvas, bg="black", image= seats_icon1,activebackground="black")
    seatsButton5.place(x=640, y=170)
    seatsButton6 = Button(canvas, bg="black", image= seats_icon1,activebackground="black")
    seatsButton6.place(x=320, y=230)
    seatsButton7 = Button(canvas, bg="black", image= seats_icon1,activebackground="black")
    seatsButton7.place(x=400, y=230)
    seatsButton8 = Button(canvas, bg="black", image= seats_icon1,activebackground="black")
    seatsButton8.place(x=480, y=230)
    seatsButton9 = Button(canvas, bg="black", image= seats_icon1,activebackground="black")
    seatsButton9.place(x=560, y=230)
    seatsButton10 = Button(canvas, bg="black", image= seats_icon1,activebackground="black")
    seatsButton10.place(x=640, y=230)
    seatsButton11 = Button(canvas, bg="black", image= seats_icon1,activebackground="black")
    seatsButton11.place(x=320, y=290)
    seatsButton12 = Button(canvas, bg="black", image= seats_icon1,activebackground="black")
    seatsButton12.place(x=400, y=290)
    seatsButton13 = Button(canvas, bg="black", image= seats_icon1,activebackground="black")
    seatsButton13.place(x=480, y=290)
    seatsButton14 = Button(canvas, bg="black", image= seats_icon1,activebackground="black")
    seatsButton14.place(x=560, y=290)
    seatsButton15 = Button(canvas, bg="black", image= seats_icon1,activebackground="black")
    seatsButton15.place(x=640, y=290)
    seatsButton16 = Button(canvas, bg="black", image= seats_icon1,activebackground="black")
    seatsButton16.place(x=320, y=350)
    seatsButton17 = Button(canvas, bg="black", image= seats_icon1,activebackground="black")
    seatsButton17.place(x=400, y=350)
    seatsButton18 = Button(canvas, bg="black", image= seats_icon1,activebackground="black")
    seatsButton18.place(x=480, y=350)
    seatsButton19 = Button(canvas, bg="black", image= seats_icon1,activebackground="black")
    seatsButton19.place(x=560, y=350)
    seatsButton20 = Button(canvas, bg="black", image= seats_icon1,activebackground="black")
    seatsButton20.place(x=640, y=350)

    select_button = Button(canvas,text="SELECT",fg="white", font=("Lucida Sans",20,"bold"),bg="black",activebackground="black",activeforeground="white")
    select_button.place(x=450,y=480)

        
        
        
    mainloop()