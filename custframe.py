from tkinter import *
root=Tk()
root.title("Vehicle service management")
root.geometry("1920x1080")

def back1(frame):
    frame.destroy()
    homepage()

def clickcustsign(frame):
    frame.destroy()
    frame=Frame(root)
    frame.pack()
    custfname=Entry(frame)
    label1=Label(frame,text="First name")
    label1.pack()
    custfname.pack()
    custlname=Entry(frame)
    label2=Label(frame,text="Last name")
    label2.pack()
    custlname.pack()
    custemail=Entry(frame)
    label3=Label(frame,text="Email")
    label3.pack()
    custemail.pack()
    custphone=Entry(frame)
    label4=Label(frame,text="Mobile number")
    label4.pack()
    custphone.pack()
    custpass=Entry(frame)
    label5=Label(frame,text="Set password")
    label5.pack()
    custpass.pack()
    custsubmit=Button(frame,text="sign up",command=lambda:clicksignup(frame))
    custsubmit.pack()
    label5=Label(frame,text="already a customer?")
    label5.pack()
    custlog=Button(frame,text="customer login",command=lambda:clickcustlog(frame))
    custlog.pack()
    back1butt=Button(frame,text="back",command=lambda:back1(frame))
    back1butt.pack()

    
def back3(frame):
    clicksignup(frame)
def jobcard(frame):
    frame.destroy()
    global services
    frame=Frame(root)
    frame.pack()
    if var1.get()==1:
        services+=" genaral services,"
    if var2.get()==1:
        services+=" oil service,"
    if var3.get()==1:
        services+=" break system maintanance,"
    if var4.get()==1:
        services+=" engine maintanance,"
    if var5.get()==1:
        services+=" oil service,"

    label1=Label(frame,text=services[:-1])
    label1.pack()
    backbutt3=Button(frame,text="back",command=lambda:back3(frame))
    backbutt3.pack()
def back2(frame):
    frame.destroy()
    clickcustsign(frame)


def clicksignup(frame):
    frame.destroy()
    
    global var1
    global var2
    global var3
    global var4
    global var5
    global services
    frame=Frame(root)
    frame.pack()
    services="The services are"
    label1=Label(frame,text="welcome,enter your vehicle details and pick the services you want")
    label1.pack()
    label2=Label(frame,text="Vehicle Brand and Model")
    label2.pack() 
    vbrand=Entry(frame)
    vbrand.pack()
    label3=Label(frame,text="Vehicle Reg no.")
    label3.pack() 
    vreg=Entry(frame)
    vreg.pack()
    var1=IntVar()
    gen=Checkbutton(frame,text="general service",variable=var1)
    gen.pack()
    var2=IntVar()
    oils=Checkbutton(frame,text="oil service",variable=var2)
    oils.pack()
    var3=IntVar()
    br=Checkbutton(frame,text="break system maintanance",variable=var3)
    br.pack()
    var4=IntVar()
    eng=Checkbutton(frame,text="engine maintanance",variable=var4)
    eng.pack()
    var5=IntVar()
    cl=Checkbutton(frame,text="oil service",variable=var5)
    cl.pack()
    subbut=Button(frame,text="submit",command=lambda:jobcard(frame))
    subbut.pack()
    backbutt2=Button(frame,text="back",command=lambda:back2(frame))
    backbutt2.pack()

    
#general checkup oil maintenace break system maintanance engine maintanance clutch repair battery
    
def back4(frame):
    frame.destroy()
    clickcustsign(frame)
def clickcustlog(frame):
    frame.destroy()
    frame=Frame(root)
    frame.pack()
    custemail=Entry(frame)
    label1=Label(frame,text="Email/Mobile number")
    label1.pack()
    custemail.pack()
    custpass=Entry(frame)
    label2=Label(frame,text="password")
    label2.pack()
    custpass.pack()
    logbutt=Button(frame,text="login")
    logbutt.pack()
    backbutt4=Button(frame,text="back",command=lambda:back4(frame))
    backbutt4.pack()


def homepage():
    frame=Frame(root)
    frame.pack()
    custsign=Button(frame,text="customer sign in",command=lambda:clickcustsign(frame),fg="white",bg="blue")
    custsign.pack()
    adlog=Button(frame,text="admin login")
    adlog.pack()
    mechlog=Button(frame,text="mechanic login")
    mechlog.pack()
homepage()
root.mainloop()