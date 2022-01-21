from cgitb import text
import profile
from tkinter import *
from tkinter import font
from tkinter import scrolledtext
from turtle import update
from PIL import ImageTk,Image
from Frame import login
import mysql.connector
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import askokcancel, showinfo, WARNING
import tkinter.ttk as ttk
import mysql.connector
from datetime import datetime
from tkinter import ttk
acno=''
class home:
    def __init__(self):
        email=login.mail_id
        w=Tk()
        w.geometry('1400x700') 
        w.configure(bg='#000000')
        w.resizable(False, False) 
        w.title("Swift Bank Online Portal")
        w.iconbitmap(r'Frame/RegDetails_img/icon.ico')
        def default_home():
            email=login.mail_id
            mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="dbms")
            mycursor = mydb.cursor()
            mycursor.execute("select name,account_no,balance from user_details where email='"+email+"'")
            res=mycursor.fetchone()
            fullname=res[0]
            global acno
            account_no=res[1]
            acno=account_no
            balance=res[2]
            f2=Frame(w,width=1400,height=658,bg='#262626')
            glabel=Label(w,text='Home',font=("Poppins",24),background='#000000',foreground='#FFFFFF').place(x=400,y=0,width=600,height=42) 
            ###################
            fullname_true="Hello, "+fullname
            Label(f2,text=fullname_true,font=("Poppins",30),background='#262626',foreground='#8AF8FF').place(x=0,y=0)  
            Label(w,text="Here's a short overview of your Account",font=("Poppins",26),background='#262626',foreground='#FFFFFF').place(x=344,y=215)
            Label(f2,text='Account Number: ',font=("Poppins",22),background='#262626',foreground='#8AF8FF').place(x=424,y=280)
            Label(f2,text=account_no,font=("Poppins",22),background='#262626',foreground='#FFFFFF').place(x=700,y=280)
            Label(f2,text='Balance:   ₹',font=("Poppins",22),background='#262626',foreground='#8AF8FF').place(x=554,y=340)
            Label(f2,text=balance,font=("Poppins",22),background='#262626',foreground='#FFFFFF').place(x=728,y=340)          
            f2.place(x=0,y=42)

        def toggle_win():
            global f1
            f1=Frame(w,width=300,height=700,bg='#D2E6FB')
            f1.place(x=0,y=0)

            def bttn(x,y,text,bcolor,fcolor,cmd):
                def on_entera(e):
                    myButton1['background']=bcolor
                    myButton1['foreground']='#262626'
                
                def on_leavea(e):
                    myButton1['background']=fcolor
                    myButton1['foreground']='#262626'

                myButton1= Button(f1,text=text,
                                width=25,
                                height=1,
                                fg='#262626',
                                border=0,
                                font=("Poppins",15),
                                bg=fcolor,
                                activebackground='#262626',
                                activeforeground=bcolor,
                                command=cmd)
                myButton1.bind("<Enter>",on_entera)
                myButton1.bind("<Enter>",on_leavea)

                myButton1.place(x=x,y=y)


            def home():
                f1.destroy()
                default_home()

            def funds():
                def btransfer_click():
                    def btsubmit():
                        acc_no=btaccnoentry.get()
                        amt=btamountentry.get()
                        passw=btpassentry.get()
                        if(acc_no=='' or amt=='' or passw==''):
                            answer=showinfo(title='Error',message='Empty fields!',icon=WARNING)
                        else:
                            amt=int(btamountentry.get())
                            mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="dbms")
                            mycursor = mydb.cursor()
                            mycursor.execute("select pwd,account_no from user_details where email='"+email+"'")
                            resp=mycursor.fetchone()
                            passwd=resp[0]
                            acno=resp[1]
                            if int(acc_no)==int(acno):
                                answer = showinfo(title='Error',message='Self Transfer not allowed!',icon=WARNING)
                                btaccnoentry.delete(0,END)
                            else:    
                                if passwd!=passw:
                                    answer = showinfo(title='Error',message='Invalid Password!',icon=WARNING)
                                else:    
                                    mycursor.execute("select account_no,balance from user_details where account_no='"+acc_no+"'")
                                    result = mycursor.fetchone()
                                    if result == None:
                                        answer = showinfo(title='Error',message='Account number not found!',icon=WARNING)
                                    else:
                                        cred_bal=result[1]
                                        mycursor.execute("select balance from user_details where email='"+email+"'")
                                        result=mycursor.fetchone()
                                        bal=result[0]
                                        if bal<=amt :
                                            answer = showinfo(title='Error',message='Insufficient balance!',icon=WARNING)
                                        else:
                                            now = datetime.now()
                                            dt_string = now.strftime("%b-%d-%Y %H:%M:%S")
                                            mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="dbms")
                                            mycursor = mydb.cursor()
                                            mycursor.execute("select trans_id from trans_his")
                                            result=mycursor.fetchall()
                                            if result==[]:
                                                value=10100
                                            else:    
                                                list=[]
                                                for i in range(len(result)):
                                                    list.append(result[i][0])
                                                value=max(list)+7
                                            mycursor.execute("select account_no from user_details where email='"+email+"'")
                                            res1=mycursor.fetchone()
                                            acno=res1[0]
                                            mycursor.execute("insert into trans_his values('"+str(value)+"','"+acc_no+"','"+str(acno)+"','"+dt_string+"','"+str(amt)+"')")
                                            mydb.commit()
                                            answer = showinfo(title='Succesfull',message='Transfer Succesfull!',icon=WARNING)
                                            rem=bal-amt
                                            mycursor.execute("UPDATE user_details set balance = '"+str(rem)+"' WHERE email='"+email+"'")
                                            mydb.commit()
                                            cur_cred=cred_bal+amt
                                            mycursor.execute("UPDATE user_details set balance = '"+str(cur_cred)+"' WHERE account_no='"+acc_no+"'")
                                            mydb.commit()
                                            mycursor.close()
                                            mydb.close()
                                            btransfer_click()

                                    
                                    
                    #frame created when btransfer button is clicked
                    btransfer_frame=Frame(w,width=800,height=658,bg='#262626')
                    btransfer_frame.place(x=600,y=42)
                    
                    #creating a canvas
                    btrnfscanvas = Canvas(btransfer_frame, width=800, height=658,bd = 0,bg = "#262626",highlightthickness = 0,relief = "ridge")
                    btrnfscanvas.place(x = 0, y = 0)
                    accountno_img = PhotoImage(file = f"Frame/home_img/accountno.png")

                    #creating a reference so that the image of button doesnt disappear
                    label3 = Label(image=accountno_img)
                    label3.image=accountno_img
                    entry0_bg = btrnfscanvas.create_image(400, 210,image = accountno_img)
                    entry1_bg = btrnfscanvas.create_image(400, 340,image = accountno_img)
                    entry3_bg = btrnfscanvas.create_image(400, 470,image = accountno_img)

                    #ACCOUNT NO INPUT
                    Label(btrnfscanvas,text='Account Number',font=("Poppins",20),background='#262626',foreground='#8AF8FF').place(x=150,y=140,width=350,height=42)
                    btaccnoentry = Entry(btrnfscanvas,bd = 0,bg = "#FFFFFF",font=("Poppins",15),highlightthickness = 0)
                    btaccnoentry.place(x=230,y=190,width=340)

                    #AMOUNT INPUT
                    Label(btrnfscanvas,text='Amount',font=("Poppins",20),background='#262626',foreground='#8AF8FF').place(x=90,y=270,width=350,height=42)
                    btamountentry = Entry(btrnfscanvas,bd = 0,bg = "#FFFFFF",font=("Poppins",15),highlightthickness = 0)
                    btamountentry.place(x=230,y=320,width=340)

                    #PASSWORD INPUT
                    Label(btrnfscanvas,text='Password',font=("Poppins",20),background='#262626',foreground='#8AF8FF').place(x=100,y=400,width=350,height=42)
                    btpassentry = Entry(btrnfscanvas,bd = 0,bg = "#FFFFFF",font=("Poppins",15),highlightthickness = 0,show='*')
                    btpassentry.place(x=230,y=450,width=340)
                    btsubmit_img = PhotoImage(file = f"Frame/home_img/btsubmit.png")
                    label3 = Label(image=btsubmit_img)
                    label3.image=btsubmit_img

                    #submit button
                    btsubmitbtn = Button(btrnfscanvas,image = btsubmit_img,borderwidth = 0,highlightthickness = 0,command = btsubmit,background="#262626",activebackground="#262626",relief = "flat").place(x=330,y=540,width=146,height=60)

                f1.destroy()
                glabel=Label(w,text='Transfer Funds',font=("Poppins",24),background='#000000',foreground='#FFFFFF').place(x=400,y=0,width=600,height=42)
                #f3 frame for selecting payment options
                f3=Frame(w,width=600,height=658,bg='#ACD6FF')
                f3.place(x=0,y=42)
                Label(f3,text='Quick Bank Transfer',font=("Poppins",28),background='#ACD6FF',foreground='#000000').place(x=20,y=100,width=550,height=52)
                btrnfs=PhotoImage(file=f'Frame/home_img/btransfer.png')
                stag=PhotoImage(file=f'Frame/home_img/swifttag.png')

                #creating a reference so that the image of button doesnt disappear
                label = Label(image=btrnfs)
                label.image=btrnfs
                btransfer=Button(f3,command=btransfer_click,image=btrnfs,border=0,background='#ACD6FF',activebackground='#ACD6FF',relief='flat').place(x=200,y=300)              
                btransfer_click()

            def trans_history():
                f1.destroy()
                sty=ttk.Style()
                f4=Frame(w,width=1400,height=658,bg='#262626')
                glabel=Label(w,text='Transaction History',font=("Poppins",24),background='#000000',foreground='#FFFFFF').place(x=400,y=0,width=600,height=42)
                f4.place(x=0,y=42)
                tcanvas = Canvas(f4, width=1200, height=658,bd = 0,bg = "#262626",highlightthickness = 0,relief = "ridge")
                tcanvas.place(x =0, y =0)
                sty.theme_use("default")
                trv=ttk.Treeview(tcanvas,columns=(1,2,3,4,5),selectmode='none',show='headings')
                sty.configure("Treeview",rowheight=60,font=("Poppins"),background="#262626",borderwidth=0,foreground="white",fieldbackground='#262626')
                sty.configure("Treeview.Heading",font=("Poppins",25),foreground="#8AF8FF",borderwidth=0,background="#262626",fieldbackground="red")
                sty.map("Treeview.Heading",background=[('selected','#262626')])
                trv.column("# 1",anchor=CENTER, stretch=NO, width=276)
                trv.column("# 2",anchor=CENTER, stretch=NO, width=276)
                trv.column("# 3",anchor=CENTER, stretch=NO, width=276)
                trv.column("# 4",anchor=CENTER, stretch=NO, width=277)
                trv.column("# 5",anchor=CENTER, stretch=NO, width=277)
                trv.pack(side=LEFT)
                trv.heading(1,text="Transaction ID")
                trv.heading(2,text="Credited To")
                trv.heading(3,text="Debited From")
                trv.heading(4,text="Amount")
                trv.heading(5,text="Date/Time")
                def update(result):
                    for i in result:
                        trv.insert('','end',values=i)
                
                mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="dbms")
                mycursor = mydb.cursor()
                mycursor.execute("select account_no from user_details where email='"+email+"'")
                rest=mycursor.fetchone()
                ac_no=rest[0]
                arg="select trans_id,cr_acc,deb_acc,amount,date_time from trans_his where cr_acc='"+str(ac_no)+"' or deb_acc='"+str(ac_no)+"'"
                mycursor.execute(arg)
                result=mycursor.fetchall()
                update(result)
                mydb.commit()
                mycursor.close()
                mydb.close()
                yscrollbar=Scrollbar(tcanvas,orient='vertical',command=trv.yview)
                yscrollbar.pack(side=RIGHT,fill="y")
                trv.configure(yscrollcommand=yscrollbar.set)

            def manage_cards():
                f1.destroy()
                debitframe=Frame(w,width=700,height=599,bg='#262626')
                glabel=Label(w,text='Manage Cards',font=("Poppins",24),background='#000000',foreground='#FFFFFF').place(x=400,y=0,width=600,height=42)
                debitframe.place(x=0,y=42)
                
                mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="dbms")
                arg1="select * from debit_card where acc_no='"+str(acno)+"'"
                mycursor = mydb.cursor()
                mycursor.execute(arg1)
                resdeb=mycursor.fetchone()
                cards_name=resdeb[0]
                debit_card_no=resdeb[2]
                debit_card_expiry=resdeb[3]
                debdomes=resdeb[4]
                debintl=resdeb[5]
                arg2="select * from cred_card where acc_no='"+str(acno)+"'"
                mycursor = mydb.cursor()
                mycursor.execute(arg2)
                rescred=mycursor.fetchone()
                creditdomes=rescred[4]
                creditintl=rescred[5]
                credit_card_no=rescred[2]
                credit_card_expiry=rescred[3]
                dbstatus=resdeb[6]
                cdstatus=rescred[6]
                mydb.commit()
                mycursor.close()
                mydb.close()

                def getvalues():
                    debit_img = PhotoImage(file = f"Frame/home_img/debit_card.png")
                    dlabel = Label(debitframe,image=debit_img,background='#262626')
                    dlabel.image=debit_img
                    dlabel.place(x=30,y=30)
                    accountlabel = Label(debitframe,text=cards_name,background='#FFFFFF',foreground="#262626",font=("Poppins",19)).place(x=50,y=320)
                    cardnolabel = Label(debitframe,text=debit_card_no,background='#FFFFFF',foreground="#262626",font=("Poppins",19)).place(x=50,y=280)
                    dbexpirylabel = Label(debitframe,text="Expiry: "+str(debit_card_expiry),background='#FFFFFF',foreground="#262626",font=("Poppins",19)).place(x=340,y=280)
                    #debit freeze toggle switch
                    global debitstatus
                    debitstatus=dbstatus
                    def Test(event): 
                        global debitstatus 
                        if debitstatus == "Enabled": 
                            debitbtn.config(image=debittoggleoff_img) 
                            dbstatusprint.set("Disabled") 
                            debitstatus = "Disabled"
                        else: 
                            debitbtn.config(image=debittoggleon_img) 
                            dbstatusprint.set("Enabled") 
                            debitstatus = "Enabled" 
                    debittoggleoff_img = PhotoImage(file="Frame/home_img/winbtn0.png")
                    debittoggleon_img = PhotoImage(file="Frame/home_img/winbtn1.png")
                    dbstatusprint = StringVar()
                    dbstatusprint.set(debitstatus) 
                    debitbtn = Button(debitframe, image=debittoggleoff_img,relief="sunken",highlightthickness=0,bd=0,background='#262626',activebackground='#262626')
                    debitbtn.place(x=200,y=550,width=52,height=32)
                    count=0
                    if count==0:
                        count+=1
                        if debitstatus == "Disabled":
                            debitbtn.config(image=debittoggleoff_img) 
                            dbstatusprint.set("Disabled")
                        else:
                            debitbtn.config(image=debittoggleon_img) 
                            dbstatusprint.set("Enabled")
                    debitbtn.bind("<Button-1>", Test) 
                    #credit card
                    credit_img = PhotoImage(file = f"Frame/home_img/credit_card.png")
                    creditframe=Frame(w,width=700,height=599,bg='#262626')
                    creditframe.place(x=700,y=42)
                    clabel = Label(creditframe,image=credit_img,background='#262626')
                    clabel.image=credit_img
                    clabel.place(x=30,y=30)
                    cdaccountlabel = Label(creditframe,text=cards_name,background='#FFFFFF',foreground="#262626",font=("Poppins",19)).place(x=50,y=320)
                    cdcardnolabel = Label(creditframe,text=credit_card_no,background='#FFFFFF',foreground="#262626",font=("Poppins",19)).place(x=50,y=280)
                    cddbexpirylabel = Label(creditframe,text="Expiry: "+str(credit_card_expiry),background='#FFFFFF',foreground="#262626",font=("Poppins",19)).place(x=340,y=280)

                    #credit freeze toggle switch
                    global creditstatus
                    creditstatus = cdstatus
                    def Test(event): 
                        global creditstatus 
                        if creditstatus == "Enabled": 
                            creditbtn.config(image=credittoggleoff_img) 
                            cdstatusprint.set("Disabled") 
                            creditstatus = "Disabled"
                        else: 
                            creditbtn.config(image=credittoggleon_img) 
                            cdstatusprint.set("Enabled") 
                            creditstatus = "Enabled" 
                    credittoggleoff_img = PhotoImage(file="Frame/home_img/winbtn0.png")
                    credittoggleon_img = PhotoImage(file="Frame/home_img/winbtn1.png")
                    cdstatusprint = StringVar()
                    cdstatusprint.set(creditstatus)
                    creditbtn = Button(creditframe, image=credittoggleoff_img,relief="sunken",highlightthickness=0,bd=0,background='#262626',activebackground='#262626')
                    count=0
                    if count==0:
                        count+=1
                        if creditstatus == "Disabled":
                            creditbtn.config(image=credittoggleoff_img) 
                            cdstatusprint.set("Disabled")
                        else:
                            creditbtn.config(image=credittoggleon_img) 
                            cdstatusprint.set("Enabled")
                    creditbtn.bind("<Button-1>", Test) 
                    creditbtn.place(x=200,y=550,width=52,height=32)
                    submitbtnframe=Frame(w,width=1400,height=59,bg='#262626')
                    submitbtnframe.place(x=0,y=640)
                    cardsubmit_img = PhotoImage(file = f"Frame/home_img/applychanges.png")
                    label16 = Label(image=cardsubmit_img)
                    label16.image=cardsubmit_img
                    
                    
                    #checkbox for debit card domestic and international payments
                    self.debitdomestic= StringVar()
                    dbdom = Checkbutton(debitframe,variable=self.debitdomestic,onvalue='True', offvalue='False', text="Domestic", bg='#262626', fg='white', activebackground='#262626', activeforeground='white',selectcolor="#262626",font=("Poppins",19))
                    self.debitdomestic.set(debdomes)
                    
                    # print(self.debitdomestic.get())
                    # print('self.debitdom.get()')

                    
                    dbdom.place(x=100,y=490)
                    self.debitint= StringVar()
                    dbint = Checkbutton(debitframe,variable=self.debitint,onvalue='True', offvalue='False', text="International", bg='#262626', fg='white', activebackground='#262626', activeforeground='white',selectcolor="#262626",font=("Poppins",19))
                    
                    
                    self.debitint.set(debintl)
                    dbint.place(x=260,y=490)
                    #checkbox for credit card domestic and international payments
                    self.creditdomestic= StringVar()
                    crddom = Checkbutton(creditframe,variable=self.creditdomestic,onvalue='True', offvalue='False', text="Domestic", bg='#262626', fg='white', activebackground='#262626', activeforeground='white',selectcolor="#262626",font=("Poppins",19))
                    self.creditdomestic.set(creditdomes)
                    crddom.place(x=100,y=490)
                    self.creditint= StringVar()
                    crdint = Checkbutton(creditframe,variable=self.creditint,onvalue='True', offvalue='False', text="International", bg='#262626', fg='white', activebackground='#262626', activeforeground='white',selectcolor="#262626",font=("Poppins",19))
                    self.creditint.set(creditintl)
                    crdint.place(x=260,y=490)
                    # APply changes function
                    def apply_changes():
                        mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="dbms")
                        arg1="update debit_card set domestic_payments='"+self.debitdomestic.get()+"',international_payments='"+self.debitint.get()+"' where acc_no='"+str(acno)+"'"
                        arg2="update cred_card set domestic_payments='"+self.creditdomestic.get()+"',international_payments='"+self.creditint.get()+"' where acc_no='"+str(acno)+"'"
                        mycursor = mydb.cursor()
                        mycursor.execute(arg1)
                        mycursor.execute(arg2)
                        mydb.commit()
                        answer = showinfo(title='Successfull',message='Changes Updated Succesfully!',icon='info')
                        

                    # Apply changes button
                    cardsubmitbtn = Button(submitbtnframe,image = cardsubmit_img,borderwidth = 0,highlightthickness = 0,command = apply_changes,background="#262626",activebackground="#262626",relief = "flat").place(x=620,y=0,width=146,height=60)
                getvalues()

            def manage_profile():
                f1.destroy()
                profile=Frame(w,width=1400,height=658,bg='#262626')
                Label(w,text='Profile',font=("Poppins",24),background='#000000',foreground='#FFFFFF').place(x=400,y=0,width=600,height=42)
                profile.place(x=0,y=42)
                canvas = Canvas(
                profile,
                bg = "#262626",
                height = 658,
                width = 1400,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge")
                canvas.place(x = 0, y = 0)
                
                Label(canvas,text="Full Name",font=("Poppins",20),background='#262626',foreground='#FFFFFF').place(x = 364.5, y = 22)
                Label(canvas,text="Email Address",font=("Poppins",20),background='#262626',foreground='#FFFFFF').place(x = 774.5, y = 22)
                Label(canvas,text="Contact Number",font=("Poppins",20),background='#262626',foreground='#FFFFFF').place(x = 364.5, y = 165)
                Label(canvas,text="Aadhar Number",font=("Poppins",20),background='#262626',foreground='#FFFFFF').place(x = 774.5, y = 165)

                email = Entry(
                    bd = 0,
                    cursor="arrow",
                    disabledbackground="#FCE6E6",
                    disabledforeground="#000000",
                    font=("Poppins",15),
                    highlightthickness = 0)

                email.place(
                    x = 774.5, y = 122,
                    width = 338.0,
                    height = 42)

                fname = Entry(
                    bd = 0,
                    font=("Poppins",15),
                    disabledbackground="#FCE6E6",
                    disabledforeground="#000000",
                    highlightthickness = 0)

                fname.place(
                    x = 364.5, y = 122,
                    width = 338.0,
                    height = 42)

                cnumber = Entry(
                    bd = 0,
                    font=("Poppins",15),
                    disabledbackground="#FCE6E6",
                    disabledforeground="#000000",
                    highlightthickness = 0)

                cnumber.place(
                    x = 364.5, y = 265,
                    width = 338.0,
                    height = 42)

                aadhar = Entry(
                    bd = 0,
                    font=("Poppins",15),
                    disabledbackground="#FCE6E6",
                    disabledforeground="#000000",
                    highlightthickness = 0)

                aadhar.place(
                    x = 774.5, y = 265,
                    width = 338.0,
                    height = 42)

                def submit():
                    try:
                        contact=int(cnumber.get())
                    except:
                        print('Enter valid contact number!')
                    aadh=aadhar.get()
                    mail=email.get()
                    name=fname.get()
                    mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="dbms")
                    mycursor = mydb.cursor()
                    if(fname=='' or contact=='' or aadh=='' or mail==''):
                        answer=showinfo(title='Error',message='Fields Missing!',icon=WARNING)
                    elif len(str(contact))!=10 or len(aadh)!=12:
                        answer=showinfo(title='Error',message='Contact/Aadhar number invalid!',icon=WARNING)
                        cnumber.delete(0, END)
                        aadhar.delete(0, END)
                    else:
                        mycursor.execute("update user_details set name='"+name+"',email='"+mail+"',mobile='"+str(contact)+"',aadhar_no='"+str(aadh)+"' where account_no='"+str(acno)+"'")
                        mycursor.execute("update debit_card set name='"+name+"' where acc_no='"+str(acno)+"'")
                        mycursor.execute("update cred_card set name='"+name+"' where acc_no='"+str(acno)+"'")
                        mydb.commit()
                        
                        mydb.commit()
                        showinfo(title='Success',message='Details Updated Successfully',icon='info')
                        email.configure(state='disabled')
                        fname.configure(state='disabled')
                        aadhar.configure(state='disabled')
                        cnumber.configure(state='disabled')

                rdsubmit = Button(
                    text="Submit",
                    borderwidth = 0,
                    highlightthickness = 0,
                    command = submit,
                    font=("Poppins",16),
                    background="#D2E6FB",
                    activebackground="#D2E6FB",
                    relief = "flat")

                rdsubmit.place(
                    x = 650, y = 357,
                    width = 175,
                    height = 42)
                def edit():
                    email.configure(state='normal')
                    fname.configure(state='normal')
                    aadhar.configure(state='normal')
                    cnumber.configure(state='normal')

                mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="dbms")
                mycursor = mydb.cursor()
                mycursor.execute("select name,email,aadhar_no,mobile from user_details where account_no='"+str(acno)+"'")
                res=mycursor.fetchone()
                fname.insert(0,res[0])
                aadhar.insert(0,res[2])
                email.insert(0,res[1])
                cnumber.insert(0,res[3])

                email.configure(state='disabled')
                fname.configure(state='disabled')
                aadhar.configure(state='disabled')
                cnumber.configure(state='disabled')
                Button(canvas,text='Edit Profile',command=edit,font=("Poppins",16),background='#FFFFFF',foreground='#000000',activeforeground="#000000",activebackground="#FFFFFF",bd=0,highlightthickness=0,relief='flat').place(x=1200,y=20,width=150,height=42)

            def contact_us():
                def contactsubmit():
                    accountno=acno
                    subj=contactsubentry.get("1.0",END)
                    issue=contactdescentry.get("1.0",END)
                    if count==0 or count_2==0 or subj.isspace==True or issue.isspace()==True:
                        answer=showinfo(title='Error',message='Fields cannot be empty')
                    else: 
                        mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="dbms")
                        arg="insert into contact_form values("+str(accountno)+",'"+str(subj)+"','"+str(issue)+"')"
                        mycursor = mydb.cursor()
                        mycursor.execute(arg)
                        mydb.commit()
                        mycursor.close()
                        mydb.close()
                        contactdescentry.delete("1.0",END)
                        contactsubentry.delete("1.0",END)
                        answer=showinfo(title='Success',message='Complaint Raised Successfully!')
                        contact_us()

                f1.destroy()
                f7=Frame(w,width=1400,height=658,bg='#262626')
                f7.place(x=0,y=42)
                glabel=Label(w,text='Contact Us',font=("Poppins",24),background='#000000',foreground='#FFFFFF').place(x=400,y=0,width=600,height=42)
                contactcanvas = Canvas(f7, width=1400, height=658,bd = 0,bg = "#262626",highlightthickness = 0,relief = "ridge")
                contactcanvas.place(x = 0, y = 0)
                Label(contactcanvas,text='Subject',font=("Poppins",24),background='#262626',foreground='#8AF8FF').place(x=330,y=0)
                contactsub_img = PhotoImage(file = f"Frame/home_img/contactsubject.png")
                label4 = Label(image=contactsub_img)
                label4.image=contactsub_img
                entry0_bg = contactcanvas.create_image(700, 110,image = contactsub_img)
                global count
                count=0
                def clear_entry(event, entry):
                    global count
                    if count==0:
                        entry.delete("1.0",END)
                        count+=1
                def max_limit(event,entry):
                    a=entry.get("1.0",'end-1c')
                    if len(a)>90:
                        entry.delete('%s - 2c' % 'end')
                #text is similar to entry box it provides multiline entry
                contactsubentry = Text(contactcanvas,bd = 0,bg = "#FFFFFF",font=("Poppins",15),highlightthickness = 0)
                contactsubentry.place(x=350,y=70,width=700,height=80)
                contactsubentry.insert("1.0",'Max 90 Characters')
                contactsubentry.bind("<Button-1>", lambda event: clear_entry(event, contactsubentry))
                contactsubentry.bind("<KeyPress>", lambda event: max_limit(event, contactsubentry))

                #describe issue entry
                Label(contactcanvas,text='Describe your issue',font=("Poppins",24),background='#262626',foreground='#8AF8FF').place(x=330,y=180)
                contactdesc_img = PhotoImage(file = f"Frame/home_img/contactdesc.png")
                label5 = Label(image=contactdesc_img)
                label5.image=contactdesc_img
                entry0_bg = contactcanvas.create_image(700, 410,image = contactdesc_img)
                #similar to entry but with a scrollbar
                contactdescentry = ScrolledText(contactcanvas,bd = 0,bg = "#FFFFFF",font=("Poppins",15),highlightthickness = 0)
                contactdescentry.place(x=350,y=260,width=700,height=300)
                contactdescentry.insert("1.0",'Max 255 Characters')
                global count_2
                count_2=0
                def clear_entry_2(event, entry):
                    global count_2
                    if count_2==0:
                        entry.delete("1.0",END)
                        count_2+=1
                def max_limit_2(event,entry):
                    a=entry.get("1.0",'end-1c')
                    if len(a)>255:
                        entry.delete('%s - 2c' % 'end')
                contactdescentry.bind("<Button-1>", lambda event: clear_entry_2(event, contactdescentry))
                contactdescentry.bind("<KeyPress>", lambda event: max_limit_2(event, contactdescentry))
                contactsubmit_img = PhotoImage(file = f"Frame/home_img/contactsubmit.png")
                label6 = Label(image=contactsubmit_img)
                label6.image=contactsubmit_img
                contsubmitbtn = Button(contactcanvas,image = contactsubmit_img,borderwidth = 0,highlightthickness = 0,command = contactsubmit,background="#262626",activebackground="#262626",relief = "flat").place(x=620,y=590,width=146,height=60)

            def logout():
                w.destroy()
                login.Login_Frame()

            bttn(0,80,'Home','#D2E6FB','#D2E6FB',home)
            bttn(0,150,'Transfer Funds','#D2E6FB','#D2E6FB',funds)
            bttn(0,220,'Transaction History','#D2E6FB','#D2E6FB',trans_history)
            bttn(0,290,'Manage Cards','#D2E6FB','#D2E6FB',manage_cards)
            bttn(0,360,'Manage Profile','#D2E6FB','#D2E6FB',manage_profile)
            bttn(0,430,'Contact Us','#D2E6FB','#D2E6FB',contact_us)
            bttn(0,650,'Logout','#D2E6FB','#D2E6FB',logout)
                
            def dele():
                f1.destroy()

                
            global img2
            img2=ImageTk.PhotoImage(Image.open('Frame/home_img/close.png'))

            Button(f1,image=img2,command=dele,border=0,background='#D2E6FB',activebackground='#D2E6FB').place(x=5,y=10)

        default_home()

        img1=ImageTk.PhotoImage(Image.open('Frame/home_img/open.png'))
        Button(w,command=toggle_win,image=img1,border=0,bg='#000000',activebackground='#000000').place(x=5,y=5)

        app_width=1400 
        app_height=700
        screen_width = w.winfo_screenwidth()
        screen_height = w.winfo_screenheight()
        x=(screen_width / 2) - (app_width/2)
        y=(screen_height / 2) - (app_height/2)
        w.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        w.deiconify()
        w.mainloop()