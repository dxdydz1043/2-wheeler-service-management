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