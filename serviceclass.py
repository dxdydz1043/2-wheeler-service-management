from datetime import *
import json

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
    
    def writefile(self,file,phone):
        servicedict={phone:self.servicedetails()}
        with open(file,'r') as servicefile:
            servicedata=json.load(servicefile)
            servicedata.append(servicedict)
        with open(file,'w') as servicefile:
            json.dump(servicedata,servicefile)
    
    def assignworker(self,worker=None):
        self.worker=worker
    
    def servicedetails(self):
        retdate=self.regdate+timedelta(2)
        print(retdate)
        return {'model':self.model,
                'regno':self.reg,
                'type':self.servicetype,
                'bdate':str(self.regdate),
                'rdate':str(retdate),
                'worker':''}
    
    def getservicedetails(self):
        details=self.servicedetails()
        info=''
        for data in details:
            info+=str(data)+'\n'
        return info

# s=service('Yamaha RX100','TN55AD1555')
# s.addServicetype('general service,oil maintenance,clutch repair,engine maintenace,break system maintenace')
# print(type(s.regdate))
# print(s.getservicedetails())

