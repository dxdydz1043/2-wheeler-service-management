from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Vehicle service management")
root.geometry("1920x1080")

path = "logo.jpg"
load = Image.open(path)
render = ImageTk.PhotoImage(load)
root.iconphoto(False, render)


canvas = Canvas(
    root,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = ImageTk.PhotoImage(Image.open("imagetwo.jpg"))
image_1 = canvas.create_image(300.0,280.0,image=image_image_1)

image_image_2 = ImageTk.PhotoImage(Image.open("admin.jpg"))
image_2 = canvas.create_image(924.0,382.0,image=image_image_2)
   
def clickcustsign():
    global custfname
    global custlname
    global custphone
    global custemail
    global custpass
    top2=Toplevel()
    top2.geometry("1920x1080")
    
    
    #image=Image.open("mahadev.jpg")
    #img=image.resize((450, 350))
    #my_img = ImageTk.PhotoImage(img) 

    

    custfname=Entry(top2)
    label1=Label(top2,text="First name -")
    label1.place(x=595.0,y=50.0)
    custfname.place(x=600.0,y=75.0,width=114.0,height=25.0)

    custlname=Entry(top2)
    label2=Label(top2,text="Last name -")
    label2.place(x=595,y=150)
    custlname.place(x=600,y=175,width=114.0,height=25.0)

    custemail=Entry(top2)
    label3=Label(top2,text="Email -")
    label3.place(x=595,y=250)
    custemail.place(x=600,y=275,width=114.0,height=25.0)

    custphone=Entry(top2)
    label4=Label(top2,text="Mobile number -")
    label4.place(x=595.0,y=350.0)
    custphone.place(x=600,y=375,width=114.0,height=25.0)

    custpass=Entry(top2)
    label5=Label(top2,text="Set password -")
    label5.place(x=595.0,y=450.0)
    custpass.place(x=600,y=475,width=114.0,height=25.0)
    
    #button_image_5 = ImageTk.PhotoImage(Image.open("button_4-Copy.png"))
    '''custsubmit=Button(top2,
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    text="customer sign in",command=clicksignup)'''
    custsubmit=Button(top2,text="sign up",command=clicksignup)
    custsubmit.place(x=595,y=570,width=114.0,height=30.0)

    label5=Label(top2,text="already a customer?")
    label5.place(x=595.0,y=650.0)

    custlog=Button(top2,text="Login",command=clickcustlog)
    custlog.place(x=630.0,y=680.0)

    
    
    
    

def jobcard():
    global services
    top3=Toplevel()
    top3.geometry("1920x1080")
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

    label1=Label(top3,text=services[:-1])
    label1.pack()
global clicksubmit


def clicksignup():
    global var1
    global var2
    global var3
    global var4
    global var5

    global services
    services="The services are"
    top1=Toplevel()
    top1.geometry("1920x1080")
    label1=Label(top1,text="Welcome !! "+" "+custfname.get())
    label1.place(x=630.0,y=50.0)

    label2=Label(top1,text="Vehicle Brand and Model -")
    label2.place(x=595,y=100) 
    vbrand=Entry(top1)
    vbrand.place(x=600,y=125,width=114.0,height=25.0)

    label3=Label(top1,text="Vehicle Reg no. -")
    label3.place(x=595,y=175) 
    vreg=Entry(top1)
    vreg.place(x=600,y=200,width=114.0,height=25.0)

    label4=Label(top1,text="Enter your vehicle details and pick the services you want :")
    label4.place(x=510,y=250)

    var1=IntVar()
    gen=Checkbutton(top1,text="general service",variable=var1)
    gen.place(x=595,y=270)

    var2=IntVar()
    oils=Checkbutton(top1,text="oil service",variable=var2)
    oils.place(x=595,y=290)

    var3=IntVar()
    br=Checkbutton(top1,text="break system maintanance",variable=var3)
    br.place(x=595,y=310)

    var4=IntVar()
    eng=Checkbutton(top1,text="engine maintanance",variable=var4)
    eng.place(x=595,y=330)

    var5=IntVar()
    cl=Checkbutton(top1,text="oil service",variable=var5)
    cl.place(x=595,y=350)
    
    subbut=Button(top1,text="submit",command=jobcard)
    subbut.place(x=630,y=450)
    

    
#general checkup oil maintenace break system maintanance engine maintanance clutch repair battery
    
global clickcustlog

def clickcustlog():
    custemail=Entry(root)
    label1=Label(root,text="Email/Mobile number")
    label1.pack()
    custemail.pack()
    custpass=Entry(root)
    label2=Label(root,text="password")
    label2.pack()
    custpass.pack()
    
    canvas.place(x = 0, y = 0)
    image_image_3 = ImageTk.PhotoImage(Image.open("background.jpg"))
    global xyz
    xyz = canvas.create_image(924.0,382.0,image=image_image_3)


#custsign=Button(root,text="customer sign in",command=clickcustsign,fg="white",bg="blue")
#button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_image_1 = ImageTk.PhotoImage(Image.open("button_3.png"))

custsign = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    text="customer sign in",command=clickcustsign
)
custsign.place(
    x=880.0,
    y=315.0,
    width=114.0,
    height=41.0
)


adlog=Button(root,text="admin login")
adlog.place(
    x=880.0,
    y=375.0,
    
)
mechlog=Button(root,text="mechanic login")
mechlog.place(
    x=880.0,
    y=430.0,
    
)
#custsign.pack()
#adlog.pack()
#mechlog.pack()
#root.resizable(False, False)

mainloop()