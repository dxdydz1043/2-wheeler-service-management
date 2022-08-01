from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox

logwin= Tk()
logwin.title("Customer - Login/Sign-Up")
logwin.geometry("400x300+10+10")
#logwin['bg']='#008F96'
    
def submit():
    e_m=e1.get()
        #print(e_m)
    if len(e_m) == 0:
        messagebox.showwarning(title='WARNING!',message='Email/Mobile number has not been entered!')
    password=e2.get()
    if len(password) == 0:
        messagebox.showwarning(title='WARNING!',message='Password has not been entered!')

   
submit_button=Button(logwin,text='Submit',command=submit)
#backbutt4=Button(custwindow,text="back",command=lambda:back4(custwindow))

l1 = Label(logwin, text = "Email/Mobile number: ",font=('Times',15))
l2 = Label(logwin, text = "Password: ",font=('Times',15))

l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)
submit_button.grid(row = 2, column = 1,sticky=E,pady=2)
#backbutt4.grid(row=3,column=2,sticky=E,pady=2)

e1 = Entry(logwin,font=('Times',15))
e2 = Entry(logwin,font=('Times',15),show='*')


e1.grid(row = 0, column = 1, pady = 2)

e2.grid(row = 1, column = 1, pady = 2)

logwin.mainloop()


