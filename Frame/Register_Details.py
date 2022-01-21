import mysql.connector
from tkinter import *
from Frame import common, list_method
from tkinter.messagebox import askokcancel, showinfo, WARNING
from Frame import reg
from Frame import login
from datetime import date


class Reg_details:
    state_name=''
    def updateState(item):
        state_name.state_txtbox.configure(state='normal')
        state_name.state_txtbox.delete(0, END)
        state_name.state_txtbox.insert(0, item)
        state_name.state_txtbox.configure(state='disabled')

    def __init__(self):
        global state_name
        state_name=self
        window = Tk()
        def drop_downstates():
            list_method.trosa(window)
        def btn_clicked():
            name=fname.get()
            try:
                contact=int(cnumber.get())
            except:
                print('Enter valid contact number!')
            aadh=aadhar.get()
            state=self.state_txtbox.get()
            mail=email.get()
            mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="dbms")
            mycursor = mydb.cursor()
            mycursor.execute("select email from user_details where email='"+mail+"'")
            if(name=='' or contact=='' or aadh=='' or state=='' or mail==''):
                answer=showinfo(title='Error',message='Fields Missing!',icon=WARNING)
            elif len(str(contact))!=10 or len(aadh)!=12:
                answer=showinfo(title='Error',message='Contact/Aadhar number invalid!',icon=WARNING)
                cnumber.delete(0, END)
                aadhar.delete(0, END)
            else:
                # swiftid=name.replace(" ","")+'@swift'
                mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="dbms")
                mycursor = mydb.cursor()
                try:    
                    mycursor.execute("update user_details set name='"+name+"',aadhar_no='"+aadh+"',mobile='"+str(contact)+"',state='"+state+"',balance='"+str(2500)+"' where email='"+mail+"'")
                    mydb.commit()

                except:
                    answer=showinfo(title='Error',message='Details entered not unique!',icon=WARNING)
                else:
                    answer=showinfo(title='Suceesful',message='Registration succesful!Redirecting to login page...',icon=WARNING)
                    mycursor.execute("select account_no from user_details where email='"+mail+"'")
                    acno=mycursor.fetchone()
                    acc_no=acno[0]
                    mycursor.execute("select deb_no from debit_card")
                    result=mycursor.fetchall()
                    list=[]
                    for i in range(len(result)):
                        list.append(result[i][0])
                    value=max(list)+13
                    today = date.today()
                    d4 = today.strftime("%m %Y")
                    month=int(d4[0:2])
                    year=int(d4[3:7])+5
                    exp_date=str(month)+'/'+str(year)
                    domes=True
                    intpay=False
                    status='Enabled'
                    mycursor.execute("insert into debit_card values('"+name+"','"+str(acc_no)+"','"+str(value)+"','"+exp_date+"','"+str(domes)+"','"+str(intpay)+"','"+status+"')")
                    mydb.commit()
                    
                    mycursor.execute("select cred_no from cred_card")
                    result=mycursor.fetchall()
                    list=[]
                    for i in range(len(result)):
                        list.append(result[i][0])
                    value=max(list)+17
                    today = date.today()
                    d4 = today.strftime("%m %Y")
                    month=int(d4[0:2])
                    year=int(d4[3:7])+5
                    exp_date=str(month)+'/'+str(year)
                    domes=True
                    intpay=False
                    status='Enabled'
                    mycursor.execute("insert into cred_card values('"+name+"','"+str(acc_no)+"','"+str(value)+"','"+exp_date+"','"+str(domes)+"','"+str(intpay)+"','"+status+"')")
                    mydb.commit()
                    mycursor.close()
                    mydb.close()

                    window.destroy()
                    login.Login_Frame()

        window.geometry("1000x600")
        window.configure(bg = "#ffffff")
        window.title("Swift Bank Online Portal")
        window.iconbitmap(r'Frame/RegDetails_img/icon.ico')

        common.center(window)
        canvas = Canvas(
            window,
            bg = "#ffffff",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"Frame/RegDetails_img/background.png")
        background = canvas.create_image(
            500.0, 300.0,
            image=background_img)

        entry0_img = PhotoImage(file = f"Frame/RegDetails_img/img_textBox0.png")
        entry0_bg = canvas.create_image(
            743.5, 156.5,
            image = entry0_img)

        email = Entry(
            bd = 0,
            bg = "#FCE6E6",
            cursor="arrow",
            disabledbackground="#FCE6E6",
            disabledforeground="#000000",
            font=("Poppins",15),
            highlightthickness = 0)

        email.place(
            x = 574.5, y = 122,
            width = 338.0,
            height = 67)
        a=reg.email_2
        email.insert(0,a)
        email.configure(state='disabled')

        entry1_img = PhotoImage(file = f"Frame/RegDetails_img/img_textBox1.png")
        entry1_bg = canvas.create_image(
            263.5, 156.5,
            image = entry1_img)

        fname = Entry(
            bd = 0,
            bg = "#c4c4c4",
            font=("Poppins",15),
            highlightthickness = 0)

        fname.place(
            x = 94.5, y = 122,
            width = 338.0,
            height = 67)

        entry2_img = PhotoImage(file = f"Frame/RegDetails_img/img_textBox2.png")
        entry2_bg = canvas.create_image(
            263.5, 299.5,
            image = entry2_img)

        cnumber = Entry(
            bd = 0,
            bg = "#c4c4c4",
            font=("Poppins",15),
            highlightthickness = 0)

        cnumber.place(
            x = 94.5, y = 265,
            width = 338.0,
            height = 67)

        entry3_img = PhotoImage(file = f"Frame/RegDetails_img/img_textBox3.png")
        entry3_bg = canvas.create_image(
            506.5, 442.5,
            image = entry3_img)

        aadhar = Entry(
            bd = 0,
            bg = "#c4c4c4",
            font=("Poppins",15),
            highlightthickness = 0)

        aadhar.place(
            x = 337.5, y = 408,
            width = 338.0,
            height = 67)

        entry4_img = PhotoImage(file = f"Frame/RegDetails_img/img_textBox4.png")
        entry4_bg = canvas.create_image(
            719.5, 299.5,
            image = entry4_img)

        self.state_txtbox = Entry(
            bd = 0,
            bg = "#FCE6E6",
            disabledbackground="#FCE6E6",
            disabledforeground="#000000",
            cursor='arrow',
            font=("Poppins",15),
            highlightthickness = 0)

        self.state_txtbox.configure(state='disabled')

        self.state_txtbox.place(
            x = 574.5, y = 265,
            width = 295.0,
            height = 67)
        

        img0 = PhotoImage(file = f"Frame/RegDetails_img/img0.png")
        list_state = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = drop_downstates,
            background="#686565",
            activebackground="#686565",
            relief = "flat")

        list_state.place(
            x = 905, y = 286,
            width = 37.5,
            height = 30)

        img1 = PhotoImage(file = f"Frame/RegDetails_img/img1.png")
        rdsubmit = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked,
            background="#D2E6FB",
            activebackground="#D2E6FB",
            relief = "flat")

        rdsubmit.place(
            x = 413, y = 517,
            width = 175,
            height = 60)
        

        window.resizable(False, False)
        window.mainloop()