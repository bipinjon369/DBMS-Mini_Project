from tkinter.ttk import Progressbar
from tkinter import *
from tkinter import ttk
from Frame import start
def splash():
    w=Tk()
    width_of_window = 430
    height_of_window = 250
    screen_width = w.winfo_screenwidth()
    screen_height = w.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))


    w.overrideredirect(1)


    s = ttk.Style()
    s.theme_use('clam')
    s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
    progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate')




    def bar():

        l4=Label(w,text='Loading...',fg='white',bg=a)
        lst4=('Poppins',13)
        l4.config(font=lst4)
        l4.place(x=18,y=200)
        
        import time
        r=0
        for i in range(100):
            progress['value']=r
            w.update_idletasks()
            time.sleep(0.01)
            r=r+1
        
        w.destroy()
        start.Main_window()
            
        
    progress.place(x=-10,y=236)


    a='#249794'
    Frame(w,width=430,height=241,bg=a).place(x=0,y=0)  

    img0 = PhotoImage(file = f"Frame/splashscreen_img/Button.png")
    getstarted = Button(
                w,
                image = img0,
                borderwidth = 0,
                highlightthickness = 0,
                command = bar,
                background="#249794",
                activebackground="#249794",
                relief = "flat")

    getstarted.place(
        x = 128, y = 180,
        width = 175,
        height = 60)


    l1=Label(w,text='Swift',fg='white',bg=a)
    lst1=('Poppins',24)
    l1.config(font=lst1)
    l1.place(x=133,y=80)

    l2=Label(w,text='Bank',fg='white',bg=a)
    lst2=('Poppins',24)
    l2.config(font=lst2)
    l2.place(x=215,y=80)

    l3=Label(w,text='Financial Services',fg='white',bg=a)
    lst3=('Poppins',12)
    l3.config(font=lst3)
    l3.place(x=140,y=120)

    w.mainloop()