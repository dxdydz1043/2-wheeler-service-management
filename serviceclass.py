from datetime import *

class service():
    
    __slots__=['model','reg','regdate','servicetype']
    
    def __init__(self,model,reg,date=date.today()):
        self.model=model
        self.reg=reg
        self.regdate=date
    
    def addServicetype(self,type):
        self.servicetype=type.split(',')
    
    # general service,oil maintenance,clutch repair,engine maintenace,break system maintenace
    
    def price(self):
        price=0
        for i in self.servicetype:
            if i=='general service':
                price+=1000
            elif i=='oil service':
                price+=500
            elif i=='clutch repair':
                price+=700
            elif i=='engine maintenace':
                price+=900
            else:
                price+=500
        return price
    
    def assignworker(self,worker=None):
        self.worker=worker
    
    def servicedetails(self):
        retdate=self.regdate+timedelta(2)
        return [self.model,self.reg,self.servicetype,self.regdate,retdate,self.price()]
    
    def getservicedetails(self):
        details=self.servicedetails()
        info=''
        for data in details:
            info+=str(data)+'\n'
        return info

s=service('Yamaha RX100','TN55AD1555')
s.addServicetype('general service,oil maintenance,clutch repair,engine maintenace,break system maintenace')
print(s.getservicedetails())

