class Node:
    def __init__(self,item=None,next=None):
        self._item=item
        self._next=next
class LinkedQueue:
    def __init__(self):
        self._head=self._end=Node()
        self._size=0
    def __str__(self):
        strg="["
        c=self._head._next
        if c==None:
            strg+="]"
            return strg
        for i in range(self._size):
            strg+=str(c._item)+","
            c=c._next
        strg=strg[:-1]+"]"
        return strg
    def enqueue(self,item):
        self._end._next=Node(item,self._end._next)
        self._end=self._end._next
        self._size+=1
    def dequeue(self):
        if self._head._next is None:
            return None
        x=self._head._next._item
        self._head._next=self._head._next._next
        self._size-=1
        return x
    def retrieve(self):
        p=self._head
        while p._next is not None:
            print(p._item)
        else:
            return None
