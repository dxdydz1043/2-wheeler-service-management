from tkinter import *
from lqproj import LinkedQueue
from llproj import LinkedList
from llproj import LinkedList
from lqproj import LinkedQueue
class Customer():

    __slots__=['name','mail','phone','pwd']

    def __init__(self,name,mail,phone,pwd):
        self.name=name
        self.mail=mail
        self.phone=phone
        self.pwd=pwd
    
    def changename(self,newname):
        self.name=newname
    
    def changemail(self,newmail):
        self.mail=newmail
    
    def changephone(self,newphone):
        self.phone=newphone
    
    def changepwd(self,newpwd):
        self.pwd=newpwd

    '''incase the customer wants to edit his/her profile,
       the customer details are stored in a list '''
    
    def custdetails(self):
        return [self.name,self.mail,self.phone,self.pwd]
    
    def login_cred(self):
        return [self.mail,self.phone,self.pwd]

    '''to print the entire customer details'''

    def getdetails(self):
        details=self.custdetails()
        info=''
        for i in details:
            info+=str(i)+'\n'
        return info
llcust=LinkedList()
'''c=Customer('harish','@gmail.com',98456,'123@abc')
print(c)
c.changemail('rmharish2017@gmail.com')
print(c)
print(c.mail)
a=c.login_cred()
print(a)
print(c.getdetails())'''
class Admin:
    def __init__(self):
        self.custlist=LinkedList()
        self.totalservices=LinkedList()
        self.pendingservices=LinkedQueue()
    def addbike(self,service,customer):
        self.totalservices.insert(service)
        self.pendingservices.enqueue(service)
        self.assignworks(service)
    def addcustomer(self,customer):
        self.custlist.insert(customer)
    def removefinishedservice(self):
        self.pendingservices.dequeue()
    def viewservicedetails(self):
        strg=""
        for i in self.totalservices:
            strg+=i.__str__()+"\n"
        return strg
    def viewcustomerdetails(self):
        strg=""
        for i in self.custlist:
            strg+=i.getdetails()+"\n"
        return strg
    def assignworks(self,service):
        if self.totalservices.length()%5==1:
            w1._works.enqueue(service)
        elif self.totalservices.length()%5==2:
            w2._works.enqueue(service)
        elif self.totalservices.length()%5==3:
            w3._works.enqueue(service)
        elif self.totalservices.length()%5==4:
            w4._works.enqueue(service)
        elif self.totalservices.length()%5==0:
            w5._works.enqueue(service)
        
ad=Admin()
class Worker:
    def __init__(self,id,name):
        self._name=name
        self._id=id
        self._works=LinkedQueue()
    def __str__(self):
        strg="Name:"+str(self._name)+"\nID  :"+str(self._id)
        return strg
    def addservice(self,service):
        self._works.enqueue(service)
    def removeservice(self):
        self._works.dequeue()
w1=Worker("W01","Ram")
w2=Worker("W02","Krish")
w3=Worker("W03","Shiv")
w4=Worker("W04","Balaji")
w5=Worker("W05","Vicky")
WorkersList=LinkedList()
WorkersList.insert(w1)
WorkersList.insert(w2)
WorkersList.insert(w3)
WorkersList.insert(w4)
WorkersList.insert(w5)


#screen1()
#mainloop()
rt=Tk()
rt.title("Vehicle service management")
rt.geometry("1920x1080")


def frame(r):
    def bk():
       
        screen1(f)
    def deli():
        work(f)
    def cd():
        custd(f)
    r.destroy()
    f=Tk()
    f.title("Admin Page")
    f.geometry('1500x1020')
    l1=Button(f,text="Customer details",command=cd)
    l1.grid(row=0,column=0)
    l2=Button(f,text="Services details")
    l2.grid(row=1,column=0)
    l3=Button(f,text="Pending services details")
    l3.grid(row=2,column=0)
    l4=Button(f,text="Workers details",command=deli).grid(row=3,column=0)
    l5=Button(f,text="Back",command=bk).grid(row=5,column=0)
def custd(f):
    def searchc():
        for i in ad.custlist:
            if c11.get()==i.phone:
                cl=Label(c,text=i.getdetails()).grid(row=5,column=1)
    def bk2():
        frame(c)
    f.destroy()
    c=Tk()
    c.title("Customer")
    c.geometry("1500x1080")
    ck=Label(c,text="Enter the customer id")
    ck.grid(row=1,column=0)
    c11=Entry(c)
    c11.grid(row=1,column=1)
    search_btn=Button(c,text="SEARCH",command=searchc).grid(row=3,column=1)
    back=Button(c,text="Back",command=bk2).grid(row=6,column=1)
    exit=Button(c,text="EXIT",command=c.destroy).grid(row=7,column=1)   
def work(f):
    def bk1():
        frame(w)
    def search():
        if w11.get()=="w1":
            s=Label(w,text=w1.__str__()).grid(row=5,column=1)
        elif w11.get()=="w2":
            s=Label(w,text=w2.__str__()).grid(row=5,column=1)
        elif w11.get()=="w3":
            s=Label(w,text=w3.__str__()).grid(row=5,column=1)
        elif w11.get()=="w4":
            s=Label(w,text=w4.__str__()).grid(row=5,column=1)
        elif w11.get()=="w5":
            s=Label(w,text=w5.__str__()).grid(row=5,column=1)
        else:
            s=Label(w,text="Enter valid id").grid(row=5,column=1)                      
    f.destroy()
    w=Tk()
    w.title("Workers")
    w.geometry("1500x1020")
    wk=Label(w,text="Enter the worker id")
    wk.grid(row=1,column=0)
    w11=Entry(w)
    w11.grid(row=1,column=1)
    search=Button(w,text="SEARCH",command=search).grid(row=3,column=1)
    back=Button(w,text="Back",command=bk1).grid(row=6,column=1)
    exit=Button(w,text="EXIT",command=w.destroy).grid(row=7,column=1)
def wpage(p,w):
    if p is not None:
        p.destroy()
    wviewpage=Tk()
    wviewpage.title("Workers page")
    wviewpage.geometry('1920x1080')
    wl1=Label(wviewpage,text=w.__str__())
    wl1.grid(row=1,column=1)
def workerlogin(p):
    def submitw():
        if llbl11.get()=="w1" and llbl21.get()=="w1":
            wpage(root1,w1)
        elif llbl11.get()=="w2" and llbl21.get()=="w2":
            wpage(root1,w2)  
        elif llbl11.get()=="w3" and llbl21.get()=="w3":
            wpage(root1,w3)
        elif llbl11.get()=="w4" and llbl21.get()=="w4":
            wpage(root1,w4)
        elif llbl11.get()=="w5" and llbl21.get()=="w5":
            wpage(root1,w5)    
        else:
            l=Label(root,text="Invalid Login or password")
            l.grid(row=2,column=1)
    if p is not None:
        p.destroy()
    root1 = Tk()
    root1.title("Worker Login")
    root1.geometry('1920x1080')
    lbl1 = Label(root1, text = "User Name: ")
    lbl1.grid(row=0,column=0)
    llbl11 = Entry(root1)
    llbl11.grid(row=0,column=1)
    lbl2 = Label(root1, text = "PASSWORD")
    lbl2.grid(row=1,column=0)
    llbl21 = Entry(root1)
    llbl21.grid(row=1,column=1)
    sub_btn=Button(root1,text="PROCEED",command=submitw).grid(row=6,column=1)

    exit_btn=Button(root1,text="EXIT",command=root1.destroy).grid(row=8,column=1)

def screen1(p=None):
    def submit():
        if lbl11.get()=="Bike24/7" and lbl21.get()=="Bk@7":
            frame(root)
        else:
            l=Label(root,text="Invalid Login or password")
            l.grid(row=2,column=1)
    if p is not None:
        p.destroy()
    root = Tk()
    root.title("Admin Login")
    root.geometry('1920x1080')
    lbl1 = Label(root, text = "User Name: ")
    lbl1.grid(row=0,column=0)
    lbl11 = Entry(root)
    lbl11.grid(row=0,column=1)
    lbl2 = Label(root, text = "PASSWORD")
    lbl2.grid(row=1,column=0)
    lbl21 = Entry(root)
    lbl21.grid(row=1,column=1)
    l=[lbl11,lbl21]
    sub_btn=Button(root,text="PROCEED",command=submit).grid(row=6,column=1)

    exit_btn=Button(root,text="EXIT",command=root.destroy).grid(row=8,column=1)





def s1():
    screen1(rt)
def ww():
    workerlogin(rt)


def back1(frame):
    frame.destroy()
    homepage()

def clickcustsign(frame):
    def submitting():
        s=Customer(str(custfname.get())+" "+str(custlname.get()), custemail.get(), custphone.get(),custpass.get())
        print(s)
        print(s.getdetails())
        llcust.insert(s)
        ad.addcustomer(s)
        clicksignup(frame)
    frame.destroy()
    frame=Frame(rt)
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
    custsubmit=Button(frame,text="sign up",command=submitting)
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
    frame=Frame(rt)
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
    frame=Frame(rt)
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
def back4(frame):
    frame.destroy()
    clickcustsign(frame)
def clickcustlog(frame):
    frame.destroy()
    frame=Frame(rt)
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
    frame=Frame(rt)
    frame.pack()
    custsign=Button(frame,text="customer sign in",command=lambda:clickcustsign(frame),fg="white",bg="blue")
    custsign.pack()
    adlog=Button(frame,text="admin login",command=s1)
    adlog.pack()
    mechlog=Button(frame,text="mechanic login",command=ww)
    mechlog.pack()
homepage()
rt.mainloop()