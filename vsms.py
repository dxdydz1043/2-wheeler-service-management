from concurrent.futures.process import _python_exit
from custclass import Customer
from serviceclass import service
from datetime import *
import json
from tkcalendar import Calendar

# from PIL import ImageTk,Image

from tkinter import *

root=Tk()
root.title("Vehicle service management")
root.geometry("1920x1080")
frame=Frame(root)

def homepage(frame):

    frame.destroy()
    frame=Frame(root)
    frame.pack()

    custsign=Button(frame,text="customer sign in",command=lambda:custsignup(frame),fg="white",bg="blue")
    custsign.pack()
    adlog=Button(frame,text="admin login")
    adlog.pack()
    mechlog=Button(frame,text="mechanic login")
    mechlog.pack()

def custsignup(frame):

    frame.destroy()
    frame=Frame(root)
    frame.pack()

    global custname
    global custemail
    global custphone
    global custpass

    custname=Entry(frame)
    label1=Label(frame,text="First name")
    label1.pack()
    custname.pack()
    custemail=Entry(frame)
    label2=Label(frame,text="Email")
    label2.pack()
    custemail.pack()
    custphone=Entry(frame)
    label3=Label(frame,text="Mobile number")
    label3.pack()
    custphone.pack()
    custpass=Entry(frame)
    label4=Label(frame,text="Set password")
    label4.pack()
    custpass.pack()
    custsubmit=Button(frame,text="sign up",command=lambda:signin_next(frame))
    custsubmit.pack()
    label5=Label(frame,text="already a customer?")
    label5.pack()
    custlog=Button(frame,text="customer login",command=lambda:custlogin(frame))
    custlog.pack()
    back1butt=Button(frame,text="back",command=lambda:homepage(frame))
    back1butt.pack()

def signin_next(frame):
    
    cust=Customer(custname.get(),custemail.get(),custphone.get(),custpass.get())
    dict1=cust.createdict()
    cust.writefile('data.json',dict1)
    
    custlogin(frame)

def custlogin(frame):

    frame.destroy()

    frame=Frame(root)
    frame.pack()

    global custcred
    global custpwd

    custcred=Entry(frame)
    label1=Label(frame,text="Mobile number")
    label1.pack()
    custcred.pack()
    custpwd=Entry(frame,show='*')
    label2=Label(frame,text="password")
    label2.pack()
    custpwd.pack()
    logbutt=Button(frame,text="login",command=lambda:login_check(frame))
    logbutt.pack()
    backbutt4=Button(frame,text="back",command=lambda:custsignup(frame))
    backbutt4.pack()

def login_check(frame):

    with open('data.json','r') as file:
        cust_data=json.load(file)
        global phone
        phone=custcred.get()
        for data in cust_data:
            if str(data.get('phone')) == custcred.get():
                if data.get('pwd') == custpwd.get():
                    login_next(frame,phone)

def login_next(frame,phone):

    frame.destroy()

    frame=Frame(root)
    frame.pack()

    edits=Button(frame,text='Edit profile',command=lambda:view_editpage(frame,phone))
    edits.pack()

    book=Button(frame,text='Book a service',command=lambda:view_servicepage(frame,phone))
    book.pack()

    back=Button(frame,text='back',command=lambda:custlogin(frame))
    back.pack()

def view_editpage(frame,phone):

    frame.destroy()
    frame=Frame(root)
    frame.pack()

    global newname
    global newemail
    global newpass

    newname=Entry(frame)
    label1=Label(frame,text="Name")
    label1.pack()
    newname.pack()
    newemail=Entry(frame)
    label2=Label(frame,text="Email")
    label2.pack()
    newemail.pack()
    newpass=Entry(frame)
    label4=Label(frame,text="Set password")
    label4.pack()
    newpass.pack()

    submit=Button(frame,text='submit',command=lambda:update_data(frame,phone))
    submit.pack()

    back=Button(frame,text='back',command=lambda:login_next(frame,phone))
    back.pack()

def update_data(frame,phone):

    newcust=Customer(newname.get(),newemail.get(),phone,newpass.get())
    dict1=newcust.createdict()

    newcust.updatefile('data.json',phone,dict1)

    login_next(frame,phone)

def view_servicepage(frame,phone):

    frame.destroy()
    frame=Frame(root)
    frame.pack()

    button1=Button(frame,text='periodic maintenace',command=lambda:periodic_maintenance(frame,phone))
    button2=Button(frame,text='running repairs')
    button3=Button(frame,text='accidental repairs')
    button4=Button(frame,text='inspection')
    button5=Button(frame,text='batteries & tyres')
    button1.pack()
    button2.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    
    back=Button(frame,text='back',command=lambda:login_next(frame,phone))
    back.pack()

def periodic_maintenance(frame,phone):

    frame.destroy()
    
    frame=Frame(root)
    frame.pack()

    text1="this is a general maintenance service which includes oil change and washing "
    label=Label(frame,text=text1)
    label.pack()

    Label(frame,text='599 Rs only').pack()

    next1=Button(frame,text='book service',command=lambda:know_about_vehicle(frame,phone))
    next1.pack()

    back=Button(frame,text='Back',command=lambda:view_servicepage(frame,phone))
    back.pack()


def know_about_vehicle(frame,phone):

    frame.destroy()
    frame=Frame(root)
    frame.pack()

    global entry1
    global entry2
    global entry3
    global cal

    label_head=Label(frame,text='enter details')
    label1=Label(frame,text='brand')
    label2=Label(frame,text='model')
    label3=Label(frame,text='registration number')
    entry1=Entry(frame)
    entry2=Entry(frame)
    entry3=Entry(frame)
    label_head.pack()
    label1.pack()
    entry1.pack()
    label2.pack()
    entry2.pack()
    label3.pack()
    entry3.pack()
    cal = Calendar(frame, selectmode = 'day',
               year = 2022, month = 8,
               day = 9)
    cal.pack()
    button1=Button(frame,text='book slot',command=lambda:book_slot(frame,phone))
    button1.pack()

def book_slot(frame,phone):
    cust_service=service(entry1.get()+entry2.get(),entry3.get(),cal.selection_get())
    
    cust_service.addServicetype('periodic maintenance')

    cust_service.writefile('service.json',phone)

    frame.destroy()
    frame=Frame(root)
    frame.pack()

    Label(frame,text='slot booked').pack()


homepage(frame)


root.mainloop()