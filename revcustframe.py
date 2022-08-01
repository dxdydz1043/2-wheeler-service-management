from tkinter import *
from tkinter import messagebox

custwindow =Tk()
custwindow.title("Vehicle service management",)
custwindow.geometry("1920x1080")  

custwindow['bg']='#A6E6F8' #lblue

def clickcustlog(frame):
    frame.destroy()
    
    frame=Frame(custwindow)
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


class CSwindow:
    def __init__(self,frame):
        #frame.destroy()
        #custwindow.quit()
        swindow=Tk()
        swindow.title("Customer - Login/Sign-Up")
        swindow.geometry("400x300+10+10")
        swindow['bg']='#008F96'
        #swindow.mainloop()
  
        self.b1=Button(swindow, text='Login',height=2,width=15,command=self.login)
        self.b2=Button(swindow, text='Sign-Up',height=2,width=15,command=self.sign_up)
        #self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=85, y=120)
        self.b2.place(x=230, y=120)
        swindow.mainloop()

    def login(self):
       # frame.destroy()
        frame=Frame(custwindow)
        frame.pack()
        clickcustlog(frame)

    def sign_up(self):
        #frame.destroy()
        #swindow.destroy()
        frame=Frame(custwindow)
        frame.pack()  
        clickcustsign(frame)
    

def back1(frame):
    frame.destroy()
    #homepage()

def clickcustsign(frame):
    
    frame.destroy()
    frame=Frame(custwindow)
    frame.pack()
    custfname=Entry(frame)
    label1=Label(frame,text="First name",justify=LEFT)
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
    '''label5=Label(frame,text="already a customer?")
    label5.pack()
    custlog=Button(frame,text="customer login",command=lambda:clickcustlog(frame))
    custlog.pack()'''
    back1butt=Button(frame,text="back",command=lambda:back1(frame))
    back1butt.pack()

    
def back3(frame):
    clicksignup(frame)

def jobcard(frame):
    frame.destroy()
    global services
    frame=Frame(custwindow)
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
    frame=Frame(custwindow)
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
#    clickcustsign(frame)


x = IntVar()
x.set("2")

    
def click():
     messagebox.showwarning(title='WARNING!',message='No options have been selected!')


def homepage():
    frame=Frame(custwindow)
    frame.pack()

    #for index in range (len(options)):
    radiobutton1 = Radiobutton(frame,text ="Admin",variable=x,value=1,padx = 25,pady = 25,font=("Times",20),command=print("Admin"))                                 
    radiobutton1.pack(anchor=W)
    radiobutton2 = Radiobutton(frame,text = "Mechanic",variable=x,value=2,padx = 25,pady = 25,font=("Times",20),command=print('Mechanic'))                                 
    radiobutton2.pack(anchor=W)
    radiobutton3 = Radiobutton(frame,text = "Customer",variable=x,value=3,padx = 25,pady = 25,font=("Times",20),command=lambda:CSwindow(frame))                                 
    radiobutton3.pack(anchor=W)

    '''def homepage():
    frame=Frame(custwindow)
    frame.pack()

    for index in range (len(options)):
        print('inside loop)', index)
        radiobutton = Radiobutton(frame,text = options[index],variable=x,value=index,padx = 25,pady = 25,font=("Times",20),command=order)                                 
        radiobutton.pack(anchor=W)'''
        
        

homepage()

custwindow.mainloop()

