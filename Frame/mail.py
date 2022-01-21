import smtplib
from tkinter.messagebox import askokcancel, showinfo, WARNING
import mysql.connector

class Email:
    def __init__(self) :
        sender = "noreply.swiftbank@gmail.com"
        receiver = "1errolken@gmail.com"
        password = "@HOLA123mine" 
        SUBJECT="Password Recovery"
        user_pass=""
        message = 'Subject: {}\n\n{}'.format(SUBJECT,"You recently requested for password through our Swift Bank online portal\nIf this wasn't you, please get in touch with us as soon as possible.\nPassword:",str(user_pass))
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender,password)
        print("Logged in...")
        server.sendmail(sender, receiver,message)
        print("Email has been sent!")