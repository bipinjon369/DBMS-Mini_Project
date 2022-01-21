from tkinter import *
from tkinter import messagebox
import mysql.connector
import requests
import re
def center(window):
    app_width=1000 
    app_height=600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x=(screen_width / 2) - (app_width/2)
    y=(screen_height / 2) - (app_height/2)
    window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    window.deiconify()
#to insert values into database
def connectcommit(arg):
    mydb=mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="dbms")
    mycursor=mydb.cursor()
    mycursor.execute(arg)
    mydb.commit()
    mycursor.close()
    mydb.close()
#checks if email format is correct
def emailformat(email):
    email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    match=email_regex.match(email)
    return match
#a online api which checks if emails are actually correct or not,this helps for the user to retrieve the password lateron which is sent through email.
def emailvalidator(email):
    email_address = email
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params = {'email': email_address})

    status = response.json()['status']
    if status == "valid":
        return True
    elif status == "invalid":
        return False
    else:
        return False


