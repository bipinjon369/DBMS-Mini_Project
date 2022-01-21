from tkinter import *
import mysql.connector
from Frame import common, start,Register_Details
from tkinter.messagebox import askokcancel, showinfo, WARNING
from tkinter import messagebox,simpledialog
email_2=""
class Reg_frame:
    def __init__(self):
        def goback_btn():
            window.destroy()
            start.Main_window()
        def signup_btn():
            email=remailentry.get()
            pwd=rpassentry.get()
            confirm=rconfirmpassentry.get()
            if pwd==confirm:
                if email=='' or pwd=='':#checks if email or password is empty
                    answer=showinfo(title='Error',message='Email or Password cannot be empty.',icon=WARNING)
                elif (' ' in email) or (' ' in pwd):#checks for whitespaces in email and password
                    answer=showinfo(title='Error',message='Email and Password cannot contain spaces.',icon=WARNING)
                    remailentry.delete(0, END)
                    rpassentry.delete(0, END)
                elif(common.emailformat(email)==None):#checks email format
                    answer=showinfo(title='Error',message='Please provide a valid  email address.',icon=WARNING)
                    remailentry.delete(0, END)
                    rpassentry.delete(0, END)
                elif(len(pwd)>15):
                    answer=showinfo(title='Error',message='Password cannot contain more than 15 characters.',icon=WARNING)
                # elif(common.emailvalidator(email)==False):#checks if emails are valid or not
                #     answer=showinfo(title='Error',message='Email address does not exist.',icon=WARNING)
                #     remailentry.delete(0, END)
                #     rpassentry.delete(0, END)
                else:#need to add a function here to check if email already exists in database

                    try:
                        mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="dbms")
                        mycursor = mydb.cursor()
                        mycursor.execute("select account_no from user_details")
                        result=mycursor.fetchall()
                        list=[]
                        for i in range(len(result)):
                            list.append(result[i][0])
                        value=max(list)+11
                        mycursor.execute("insert into user_details(email,pwd,account_no) values('"+email+"','"+pwd+"','"+str(value)+"')")
                        mydb.commit()
                        mycursor.close()
                        mydb.close()
                    except:
                        answer=showinfo(title='Error',message='Email Id already exists!',icon=WARNING)
                        remailentry.delete(0, END)
                        rpassentry.delete(0, END)
                    else:
                        answer=showinfo(title='Thank You for Registering!',message='Thank You for Registering.\nYou will now be redirected to fill out some basic details.')
                        window.destroy()
                        global email_2
                        email_2=email
                        Register_Details.Reg_details()
            else:
                showinfo(title='Error',message='Passwords Do not Match',icon=WARNING)
            

        window = Tk()
        common.center(window)
        window.title("Swift Bank Online Portal")
        window.iconbitmap(r'Frame/Register_img/icon.ico')
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

        background_img = PhotoImage(file = f"Frame/Register_img/background.png")
        background = canvas.create_image(
            500.0, 300.0,
            image=background_img)

        entry0_img = PhotoImage(file = f"Frame/Register_img/img_textBox0.png")
        entry0_bg = canvas.create_image(
            749.5, 210.5,
            image = entry0_img)
        #Register Page Email Entry Box
        remailentry = Entry(
            bd = 0,
            bg = "#c4c4c4",
            font=("Poppins",15),
            highlightthickness = 0)
        
        remailentry.place(
            x = 599.5, y = 176,
            width = 300.0,
            height = 67)

        entry1_img = PhotoImage(file = f"Frame/Register_img/img_textBox1.png")
        entry1_bg = canvas.create_image(
            749.5, 369.5,
            image = entry1_img)
        #Register Page Password Entry Box
        rpassentry = Entry(
            bd = 0,
            bg = "#c4c4c4",
            font=("Poppins",15),
            show="*",
            highlightthickness = 0)

        rpassentry.place(
            x = 599.5, y = 335,
            width = 300.0,
            height = 67)

        entry00_img = PhotoImage(file = f"Frame/Register_img/img_textBox1.png")
        entry00_bg = canvas.create_image(
            749.5, 469.5,
            image = entry00_img)

        rconfirmpassentry = Entry(
            bd = 0,
            bg = "#c4c4c4",
            font=("Poppins",15),
            show="*",
            highlightthickness = 0)

        rconfirmpassentry.place(
            x = 599.5, y = 435,
            width = 300.0,
            height = 67)
        #Register Page Sign UP Button
        img0 = PhotoImage(file = f"Frame/Register_img/img0.png")
        rsupbtn = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = goback_btn,
            background="#D2E6FB",
            activebackground="#D2E6FB",
            relief = "flat")

        rsupbtn.place(
            x = 768, y = 535,
            width = 175,
            height = 60)
        #Go back button(to main page)
        img1 = PhotoImage(file = f"Frame/Register_img/img1.png")
        rgobackbtn = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = signup_btn,
            background="#D2E6FB",
            activebackground="#D2E6FB",
            relief = "flat")
        
        rgobackbtn.place(
            x = 565, y = 535,
            width = 175,
            height = 60)

        window.resizable(False, False)
        window.mainloop()