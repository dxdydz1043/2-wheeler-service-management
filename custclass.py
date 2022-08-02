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

c=Customer('harish','@gmail.com',98456,'123@abc')
print(c)
c.changemail('rmharish2017@gmail.com')
print(c)
print(c.mail)
a=c.login_cred()
print(a)
print(c.getdetails())

