from distutils.log import INFO
from textwrap import fill
from tkinter import *
from tkinter.messagebox import askokcancel, showinfo, WARNING
from Frame import common,login
import mysql.connector

class Main_window:
    def __init__(self):
        window = Tk()
        #centering the window to the screen
        common.center(window)
        window.title("Filo")
        window.iconbitmap(r'Frame/admin_img/icon.ico')
        window.geometry("1000x600")
        window.configure(bg = "#D2E6FB")
        
        def logout():
            window.destroy()
            login.Login_Frame()
        
        def manage_accounts():
            contentframe=Frame(window,width=720,height=600,bg='#D2E6FB')
            contentframe.place(x=280,y=0)
            Label(contentframe,text="Manage Accounts",font=("Poppins",22),background='#D2E6FB',foreground='#000000').place(x=10,y=10)
            def acc_details():
                detailsframe=Frame(contentframe,width=720,height=490,bg='#D2E6FB')
                detailsframe.place(x=0,y=110)
                def search():
                    try:
                        acc_no=int(accnoentry.get())
                    except:
                        answer=showinfo(title='Error',message='Account number invalid!',icon=WARNING)
                        accnoentry.delete(0,END)
                    if len(str(acc_no))!=7:
                        answer=showinfo(title='Error',message='Account number invalid!',icon=WARNING) 
                        accnoentry.delete(0,END)
                    try:    
                        mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="dbms")
                        mycursor = mydb.cursor()
                        mycursor.execute("select * from user_details where account_no='"+str(acc_no)+"'")
                        result=mycursor.fetchone()
                    except:
                        answer=showinfo(title='Error',message='Account number doesnt exist!',icon=WARNING)
                        accnoentry.delete(0,END) 
                    name=result[0]
                    email=result[1]
                    account_no=result[3]
                    aadhar_no=result[4]
                    mobile=result[5]
                    state=result[6]
                    balance=result[7]

                    Label(detailsframe,text="Name: "+str(name),font=("Poppins",16),background='#D2E6FB',foreground='#000000').place(x=10,y=100)
                    Label(detailsframe,text="Email Address: "+str(email),font=("Poppins",16),background='#D2E6FB',foreground='#000000').place(x=10,y=150)
                    Label(detailsframe,text="Account Number: "+str(account_no),font=("Poppins",16),background='#D2E6FB',foreground='#000000').place(x=10,y=200)
                    Label(detailsframe,text="Aadhar Number: "+str(aadhar_no),font=("Poppins",16),background='#D2E6FB',foreground='#000000').place(x=10,y=250)
                    Label(detailsframe,text="Mobile Number: "+str(mobile),font=("Poppins",16),background='#D2E6FB',foreground='#000000').place(x=10,y=300)
                    Label(detailsframe,text="State: "+str(state),font=("Poppins",16),background='#D2E6FB',foreground='#000000').place(x=10,y=350)
                    Label(detailsframe,text="Balance: "+str(balance),font=("Poppins",16),background='#D2E6FB',foreground='#000000').place(x=10,y=400)
                
                Label(detailsframe,text="Account Number: ",font=("Poppins",16),background='#D2E6FB',foreground='#000000').place(x=0,y=40)
                accnoentry = Entry(detailsframe,bd = 0,bg = "#FFFFFF",font=("Poppins",15),highlightthickness = 0)
                accnoentry.place(x=200,y=40,width=350)
                Button(detailsframe,text='Search',command=search,font=("Poppins",16),background='#A3D0FF',foreground='#000000',activeforeground="#A3D0FF",activebackground="#262626",bd=0,highlightthickness=0,relief='sunken').place(x=560,y=40,width=150,height=42)

            def delete_account():
                def delete():
                    try:
                        acc_no=int(accnoentry.get())
                    except:
                        answer=showinfo(title='Error',message='Account number invalid!',icon=WARNING)
                        accnoentry.delete(0,END)
                    if len(str(acc_no))!=7:
                        answer=showinfo(title='Error',message='Account number invalid!',icon=WARNING) 
                        accnoentry.delete(0,END)
                    try:    
                        mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="dbms")
                        mycursor = mydb.cursor()
                        mycursor.execute("delete from debit_card where acc_no='"+str(acc_no)+"'")
                        mycursor.execute("delete from cred_card where acc_no='"+str(acc_no)+"'")
                        mycursor.execute("delete from contact_form where account_no='"+str(acc_no)+"'")
                        mycursor.execute("delete from trans_his where cr_acc='"+str(acc_no)+"' or deb_acc='"+str(acc_no)+"'")
                        mycursor.execute("delete from user_details where account_no='"+str(acc_no)+"'")
                        mydb.commit()
                        answer=showinfo(title='Success',message=str(acc_no)+' has been deleted successfully!',icon='info')
                        accnoentry.delete(0,END)
                    except:
                        answer=showinfo(title='Error',message='Account number doesnt exist!',icon=WARNING) 
                        accnoentry.delete(0,END)                    

                deleteframe=Frame(contentframe,width=720,height=490,bg='#D2E6FB')
                deleteframe.place(x=0,y=110)
                Label(deleteframe,text="Account Number: ",font=("Poppins",16),background='#D2E6FB',foreground='#000000').place(x=0,y=40)
                accnoentry = Entry(deleteframe,bd = 0,bg = "#FFFFFF",font=("Poppins",15),highlightthickness = 0)
                accnoentry.place(x=200,y=40,width=350)
                Button(deleteframe,text='Delete',command=delete,font=("Poppins",16),background='#A3D0FF',foreground='#000000',activeforeground="#A3D0FF",activebackground="#262626",bd=0,highlightthickness=0,relief='sunken').place(x=560,y=40,width=150,height=42)

            Button(contentframe,text='View Account Details',command=acc_details,font=("Poppins",16),background='#A3D0FF',foreground='#000000',activeforeground="#A3D0FF",activebackground="#262626",bd=0,highlightthickness=0,relief='sunken').place(x=0,y=70,width=360,height=42)
            Button(contentframe,text='Delete Accounts',command=delete_account,font=("Poppins",16),background='#A3D0FF',foreground='#000000',activeforeground="#A3D0FF",activebackground="#262626",bd=0,highlightthickness=0,relief='sunken').place(x=360,y=70,width=360,height=42)

        
            acc_details()      

        menuframe=Frame(window,width=280,height=600,bg='#262626')
        menuframe.place(x=0,y=0)

        manage_accounts()

        def contact():
            contactframe=Frame(window,width=720,height=600,bg='#D2E6FB')
            contactframe.place(x=280,y=0)
            Label(contactframe,text="Support Dashboard",font=("Poppins",22),background='#D2E6FB',foreground='#000000').place(x=10,y=10)
            mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="dbms")
            mycursor = mydb.cursor()
            mycursor.execute("select * from contact_form")
            result=mycursor.fetchall()
            queryframe=Frame(contactframe,width=720,height=540,bg='#D2E6FB')
            queryframe.place(x=0,y=60)

            mycursor.close()
            mydb.close()
            global count,b1,b2
            count=0
            def navigateprev():
                global count
                if count==0:
                    count=0
                else:
                    count=count-1
                acc_no=result[count][0]
                subject=result[count][1].rstrip('\n')
                issue=result[count][2].rstrip('\n')
                tcanvas = Canvas(queryframe, width=720, height=540,bd = 0,bg = "#D2E6FB",highlightthickness = 0,relief = "ridge")
                tcanvas.place(x=0,y=0)
                Label(tcanvas,text="Account Number: "+str(acc_no),font=("Poppins",16),background='#D2E6FB',foreground='#000000').place(x=10,y=50)
                Label(tcanvas,text="Subject: ",font=("Poppins",18),background='#D2E6FB',foreground='#3C7AB9').place(x=10,y=100)
                Label(tcanvas,text=subject,font=("Poppins",16),background='#D2E6FB',foreground='#000000').place(x=10,y=150)
                Label(tcanvas,text="Issue: ",font=("Poppins",18),background='#D2E6FB',foreground='#3C7AB9').place(x=10,y=200)
                Label(tcanvas,text=issue+"\n",font=("Poppins",16),background='#D2E6FB',foreground='#000000').place(x=10,y=250)
                Button(queryframe,text='Previous',command=navigateprev,font=("Poppins",16),background='#A3D0FF',foreground='#000000',activeforeground="#A3D0FF",activebackground="#262626",bd=0,highlightthickness=0,relief='sunken').place(x=400,y=490,width=150,height=42)
                Button(queryframe,text='Next',command=navigatenext,font=("Poppins",16),background='#A3D0FF',foreground='#000000',activeforeground="#A3D0FF",activebackground="#262626",bd=0,highlightthickness=0,relief='sunken').place(x=560,y=490,width=150,height=42)

            def navigatenext():
                length=len(result)
                
                global count,b1,b2
                if count==length-1:
                    count=length-1
                else:
                    count=count+1
                acc_no=result[count][0]
                subject=result[count][1].rstrip('\n')
                issue=result[count][2].rstrip('\n')
                tcanvas = Canvas(queryframe, width=720, height=540,bd = 0,bg = "#D2E6FB",highlightthickness = 0,relief = "ridge")
                tcanvas.place(x=0,y=0)
                Label(tcanvas,text="Account Number: "+str(acc_no),font=("Poppins",16),background='#D2E6FB',foreground='#000000').place(x=10,y=50)
                Label(tcanvas,text="Subject: ",font=("Poppins",18),background='#D2E6FB',foreground='#3C7AB9').place(x=10,y=100)
                Label(tcanvas,text=subject,font=("Poppins",16),background='#D2E6FB',foreground='#000000').place(x=10,y=150)
                Label(tcanvas,text="Issue: ",font=("Poppins",18),background='#D2E6FB',foreground='#3C7AB9').place(x=10,y=200)
                Label(tcanvas,text=issue+"\n",font=("Poppins",16),background='#D2E6FB',foreground='#000000').place(x=10,y=250)
                Button(queryframe,text='Previous',command=navigateprev,font=("Poppins",16),background='#A3D0FF',foreground='#000000',activeforeground="#A3D0FF",activebackground="#262626",bd=0,highlightthickness=0,relief='sunken').place(x=400,y=490,width=150,height=42)
                Button(queryframe,text='Next',command=navigatenext,font=("Poppins",16),background='#A3D0FF',foreground='#000000',activeforeground="#A3D0FF",activebackground="#262626",bd=0,highlightthickness=0,relief='sunken').place(x=560,y=490,width=150,height=42)

            navigateprev()
            global b1,b2
            b1=Button(queryframe,text='Previous',command=navigateprev,font=("Poppins",16),background='#A3D0FF',foreground='#000000',activeforeground="#A3D0FF",activebackground="#262626",bd=0,highlightthickness=0,relief='sunken')
            b1.place(x=400,y=490,width=150,height=42)
            b2=Button(queryframe,text='Next',command=navigatenext,font=("Poppins",16),background='#A3D0FF',foreground='#000000',activeforeground="#A3D0FF",activebackground="#262626",bd=0,highlightthickness=0,relief='sunken')
            b2.place(x=560,y=490,width=150,height=42)

        Button(menuframe,text='Manage Accounts',command=manage_accounts,font=("Poppins",16),background='#262626',foreground='#FFFFFF',activeforeground="#A3D0FF",activebackground="#262626",bd=0,highlightthickness=0,relief='sunken').place(x=0,y=200,width=280,height=42)
        Button(menuframe,text='Support Dashboard',command=contact,font=("Poppins",16),background='#262626',foreground='#FFFFFF',activeforeground="#A3D0FF",activebackground="#262626",bd=0,highlightthickness=0,relief='sunken').place(x=0,y=260,width=280,height=42)
        Button(menuframe,text='Logout',command=logout,font=("Poppins",16),background='#262626',foreground='#FFFFFF',activeforeground="#A3D0FF",activebackground="#262626",bd=0,highlightthickness=0,relief='sunken').place(x=0,y=550,width=240,height=42)
        Label(menuframe,text="Admin ID",font=("Poppins",16),background='#262626',foreground='#A3D0FF').place(x=0,y=10)
        Label(menuframe,text=login.admin_mailid,font=("Poppins",12),background='#262626',foreground='#FFFFFF').place(x=0,y=40)
        window.mainloop()