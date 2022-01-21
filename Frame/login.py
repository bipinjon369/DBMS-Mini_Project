from tkinter import *
import mysql.connector
from Frame import home,common, start, forgotpassword,admin
from tkinter.messagebox import askokcancel, showinfo, WARNING
from tkinter import messagebox,simpledialog
mail_id=''
admin_mailid=""
class Login_Frame:
    def __init__(self):
        def signin_btn():
            global mail_id
            mail_id=lemailentry.get()
            email = lemailentry.get()
            pwd = lpassentry.get()
            if email=='' or pwd=='':#checks if email or password is empty
                answer=showinfo(title='Error',message='Email or Password cannot be empty.',icon=WARNING)
            elif (' ' in email) or (' ' in pwd):#checks for whitespaces in email and password
                answer=showinfo(title='Error',message='Email and Password cannot contain spaces.',icon=WARNING)
                lemailentry.delete(0, END)
                lpassentry.delete(0, END)
            elif(common.emailformat(email)==None):#checks email format
                answer=showinfo(title='Error',message='Please provide a valid a email address.',icon=WARNING)
                lemailentry.delete(0, END)
                lpassentry.delete(0, END)
            # elif(common.emailvalidator(email)==False):#checks if emails are valid or not
            #     answer=showinfo(title='Error',message='Email address does not exist.',icon=WARNING)
            #     lemailentry.delete(0, END)
            #     lpassentry.delete(0, END)
            else:
                mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="dbms")
                mycursor = mydb.cursor()
                mycursor.execute("select email,pwd from user_details where email='"+email+"'")
                result = mycursor.fetchone()
                if result == None:
                    answer = showinfo(title='Error',message='Email address not found.',icon=WARNING)
                elif pwd != result[1]:
                    answer = showinfo(title='Error',message='Invalid Password!.',icon=WARNING)
                else:
                    answer=showinfo(title='Successfull',message='Login Successful.')
                    window.destroy()
                    home.home()
                mydb.close()
        def goback_btn():
            window.destroy()
            start.Main_window()
        def forgot_pass():
            forgotpassword.fg_pass(window)
        def admin_login():
            global admin_mailid
            email = lemailentry.get()
            admin_mailid = lemailentry.get()
            pwd = lpassentry.get()
            if email=='' or pwd=='':#checks if email or password is empty
                answer=showinfo(title='Error',message='Email or Password cannot be empty.',icon=WARNING)
            elif (' ' in email) or (' ' in pwd):#checks for whitespaces in email and password
                answer=showinfo(title='Error',message='Email and Password cannot contain spaces.',icon=WARNING)
                lemailentry.delete(0, END)
                lpassentry.delete(0, END)
            elif(common.emailformat(email)==None):#checks email format
                answer=showinfo(title='Error',message='Please provide a valid a email address.',icon=WARNING)
                lemailentry.delete(0, END)
                lpassentry.delete(0, END)
            else:
                mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="dbms")
                mycursor = mydb.cursor()
                mycursor.execute("select email,password from admin where email='"+email+"'")
                result = mycursor.fetchone()
                if result == None:
                    answer = showinfo(title='Error',message='Email address not found.',icon=WARNING)
                elif pwd != result[1]:
                    answer = showinfo(title='Error',message='Invalid Password!.',icon=WARNING)
                else:
                    answer=showinfo(title='Successfull',message='Login Successful.')
                    window.destroy()
                    admin.Main_window()
                mydb.close()            
        window = Tk()
        common.center(window)
        window.title("Swift Bank Online Portal")
        window.iconbitmap(r'Frame/Login_img/icon.ico')
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

        background_img = PhotoImage(file = f"Frame/Login_img/background.png")
        background = canvas.create_image(
            500.0, 300.0,
            image=background_img)

        entry0_img = PhotoImage(file = f"Frame/Login_img/img_textBox0.png")
        entry0_bg = canvas.create_image(
            749.5, 210.5,
            image = entry0_img)

        lemailentry = Entry(
            bd = 0,
            bg = "#c4c4c4",
            font=("Poppins",15),
            highlightthickness = 0)

        lemailentry.place(
            x = 599.5, y = 176,
            width = 300.0,
            height = 67)
        entry1_img = PhotoImage(file = f"Frame/Login_img/img_textBox1.png")
        entry1_bg = canvas.create_image(
            749.5, 369.5,
            image = entry1_img)

        lpassentry = Entry(
            bd = 0,
            bg = "#c4c4c4",
            font=("Poppins",15),
            show="*",
            highlightthickness = 0)

        lpassentry.place(
            x = 599.5, y = 335,
            width = 300.0,
            height = 67)

        img0 = PhotoImage(file = f"Frame/Login_img/img0.png")
        lgbbtn = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = goback_btn,
            background="#D2E6FB",
            activebackground="#D2E6FB",
            relief = "flat")

        lgbbtn.place(
            x = 761, y = 455,
            width = 175,
            height = 60)

        img1 = PhotoImage(file = f"Frame/Login_img/img1.png")
        lsigninbtn = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = signin_btn,
            background="#D2E6FB",
            activebackground="#D2E6FB",
            relief = "flat")

        lsigninbtn.place(
            x = 565, y = 455,
            width = 175,
            height = 60)

        img2 = PhotoImage(file = f"Frame/Login_img/img2.png")
        lfgtpassbtn = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = forgot_pass,
            background="#D2E6FB",
            activebackground="#D2E6FB",
            relief = "flat")

        lfgtpassbtn.place(
            x = 776, y = 417,
            width = 163,
            height = 28)

        img3 = PhotoImage(file = f"Frame/Login_img/img3.png")
        ladminbtn = Button(
            image = img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = admin_login,
            background="#D2E6FB",
            activebackground="#D2E6FB",
            relief = "flat")

        ladminbtn.place(
            x = 16, y = 541,
            width = 37,
            height = 43)

        window.resizable(False, False)
        window.mainloop()