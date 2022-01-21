from tkinter import *
import mysql.connector
from Frame import common, reg, login
from tkinter.messagebox import askokcancel, showinfo, WARNING
from tkinter import messagebox,simpledialog
#this frame let's you register and login
class Main_window:
    def __init__(self):
        def register_btn():
            window.destroy()
            reg.Reg_frame()
        def login_btn():
            window.destroy()
            login.Login_Frame()
        window = Tk()
        common.center(window)
        window.title("Swift Bank Online Portal")
        window.iconbitmap(r'Frame/Main_img/icon.ico')
        window.geometry("1000x600")
        window.configure(bg = "#ffffff")
        canvas = Canvas(
            window,
            bg = "#ffffff",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"Frame/Main_img/background.png")
        background = canvas.create_image(
            500.0, 300.0,
            image=background_img)

        img0 = PhotoImage(file = f"Frame/Main_img/img0.png")
        mregbtn = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = register_btn,
            background="#D2E6FB",
            activebackground="#D2E6FB",
            relief = "flat")

        mregbtn.place(
            x = 413, y = 226,
            width = 194,
            height = 60)

        img1 = PhotoImage(file = f"Frame/Main_img/img1.png")
        mloginbtn = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = login_btn,
            background="#D2E6FB",
            activebackground="#D2E6FB",
            relief = "flat")

        mloginbtn.place(
            x = 413, y = 322,
            width = 194,
            height = 60)
        window.resizable(False, False)
        window.mainloop()