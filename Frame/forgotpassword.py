from tkinter import *
from Frame import common
from tkinter.messagebox import askokcancel, showinfo, WARNING
import mysql.connector
import smtplib

def fg_pass(window):
    def submitbtn():
        email = recovemail.get()
        if email=='':#checks if email or password is empty
            answer=showinfo(title='Error',message='Email cannot be empty.',icon=WARNING)
        elif (' ' in email):#checks for whitespaces in email and password
            answer=showinfo(title='Error',message='Email cannot contain spaces.',icon=WARNING)
            recovemail.delete(0, END)
        elif(common.emailformat(email)==None):#checks email format
            answer=showinfo(title='Error',message='Please provide a valid  email address.',icon=WARNING)
            recovemail.delete(0, END)
        elif(common.emailvalidator(email)==False):#checks if emails are valid or not
            answer=showinfo(title='Error',message='Email address does not exist.',icon=WARNING)
            recovemail.delete(0, END)
        else:
            mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="dbms")
            mycursor = mydb.cursor()
            mycursor.execute("select email,pwd from user_details")
            result = mycursor
            dict={}
            for i,j in result:
                dict.setdefault(i,j)
            if email in dict:
                sender = "noreply.swiftbank@gmail.com"
                receiver = email
                password =  "@HOLA123mine"
                SUBJECT="Password Recovery"
                user_pass=dict[email]
                message = 'Subject: {}\n\n{}'.format(SUBJECT,"You recently requested for password through our Swift Bank online portal\nIf this wasn't you, please get in touch with us as soon as possible.\nPassword:"+user_pass)
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender,password)
                print("Logged in...")
                server.sendmail(sender, receiver,message)
                print("Email has been sent!")
                answer=showinfo(title='Success',message='Password has been sent to your registered Email Address.')
            else:
                answer=showinfo(title='Error',message='Email id not found!',icon=WARNING)
            mycursor.close()
            mydb.close()
            recovery.destroy()



    recovery = Toplevel(window)
    recovery.grab_set()
    centerfgwindow(recovery)
    recovery.title("Password Recovery")
    recovery.iconbitmap(r'Frame/PasswordRecovery_img/icon.ico')
    recovery.geometry("500x350")
    recovery.configure(bg = "#ffffff")
    canvas1 = Canvas(
        recovery,
        bg = "#ffffff",
        height = 350,
        width = 500,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas1.place(x = 0, y = 0)

    background_img1 = PhotoImage(file = f"Frame/PasswordRecovery_img/background.png")
    background1 = canvas1.create_image(
        250.0, 175.0,
        image=background_img1,
        )

    entry1_img = PhotoImage(file = f"Frame/PasswordRecovery_img/img_textBox0.png")
    entry1_bg = canvas1.create_image(
        250.0, 188.5,
        image = entry1_img,
        )

    recovemail = Entry(
        master=recovery,
        bd = 0,
        bg = "#c4c4c4",
        font=("Poppins",15),
        highlightthickness = 0)

    recovemail.place(
        x = 84.5, y = 154,
        width = 331.0,
        height = 67)

    img1 = PhotoImage(file = f"Frame/PasswordRecovery_img/img0.png")
    submit = Button(
        master=recovery,
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = submitbtn,
        background="#D2E6FB",
        activebackground="#D2E6FB",
        relief = "flat")

    submit.place(
        x = 163, y = 255,
        width = 175,
        height = 60)

    recovery.resizable(False, False)
    recovery.mainloop()
#width and height of this widnow is different
def centerfgwindow(rec_window):
    app_width=500 
    app_height=350
    screen_width = rec_window.winfo_screenwidth()
    screen_height = rec_window.winfo_screenheight()
    x=(screen_width / 2) - (app_width/2)
    y=(screen_height / 2) - (app_height/2)
    rec_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    rec_window.deiconify()