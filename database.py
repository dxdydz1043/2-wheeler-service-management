class cust_node:

    __slots__=['customer','service','next']

    def __init__(self,customer=None,service=None,next=None):
        self.customer=customer
        self.service=service
        self.next=next
    
class service_node:
    
    __slots__=['vehicle','next']

    def __init__(self,vehicle=None,next=None):
        self.vehicle=vehicle
        self.next=next

class Cust_database:
    
    def __init__(self):
        self.start=self.end=cust_node()
        self.users=0
    
    def addCustomer(self,customer):
        if self.users==0:
            self.end=cust_node(customer)
            self.start.next=self.end
        else:
            self.end.next=cust_node(customer)
            self.end=self.end.next
        self.users+=1

    def addcustservice(self,customer,vehicle):
        s=self.start.next
        while s.customer!=customer:
            s=s.next
        else:
            s.service=vehicle
    
    def __len__(self):
        return self.users
    
    def __iter__(self):
        s=self.start
        while s!=self.end:
            temp=s.next
            s=s.next
            yield temp
            

class Service_database:

    def __init__(self):
        self.start=self.end=service_node()
        self.services=0
    
    def addService(self,vehicle):
        if self.services==0:
            self.end=service_node(vehicle)
            self.start.next=self.end
        else:
            self.end.next=service_node(vehicle)
            self.end=self.end.next
        self.services+=1
    
    def __len__(self):
        return self.services
    
    def __iter__(self):
        s=self.start
        while s!=self.end:
            temp=s.next
            s=s.next
            yield temp

data=Cust_database()
data.addCustomer('ram')
data.addCustomer('ravi')
data.addCustomer('rahul')
sdata=Service_database()
sdata.addService('maruthi')
sdata.addService('TVS')
s1data=Service_database()
s1data.addService('RX100')
data.addcustservice('ram',sdata)
data.addcustservice('rahul',s1data)
for i in data:
    if i.customer=='rahul':
        i.service.addService('Honda cb-shine')
for i in data:
    print(i.customer)
    if i.service==None:
        print(' no services')
    else:
        for k in i.service:
            print(' '+k.vehicle)






