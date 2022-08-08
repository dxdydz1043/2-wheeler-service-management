import json

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
    
    def createdict(self):
        datadict={'name':self.name,'mail':self.mail,'phone':self.phone,'pwd':self.pwd}
        return datadict

    def writefile(self,file,datadict):
        with open(file,'r') as data:
            cust_list=json.load(data)
            cust_list.append(datadict)
        with open(file,'w') as data:
            json.dump(cust_list,data)
    
    def updatefile(self,file,phone,datadict):

        with open(file,'r') as data:
            cust_list=json.load(data)
        for i in cust_list:
            if i.get('phone')==phone:
                cust_list.remove(i)
                cust_list.append(datadict)
                break
        with open(file,'w') as data:
            json.dump(cust_list,data)

# c=Customer('harish','@gmail.com',98456,'123@abc')
# print(c)
# c.changemail('rmharish2017@gmail.com')
# print(c)
# print(c.mail)
# a=c.login_cred()
# print(a)
# print(c.getdetails())

# c=Customer('harsh','bansal@gmail.com','2222222222','3333')
# a=c.createdict()
# c.updatefile('data.json','2222222222',a)
# print('updated successfully')